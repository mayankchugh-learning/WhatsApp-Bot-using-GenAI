import openai
from openai import OpenAI
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from dotenv import load_dotenv
import os
import sys


load_dotenv()
app = Flask(__name__)

anyscale_api_key=os.getenv("ANY_SCALE_API_KEY")
anyscale_base_url = os.getenv("ANY_SCALE_API_BASE")
MODEL_NAME = 'meta-llama/Meta-Llama-3-8B-Instruct'

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

app = Flask(__name__)
@app.route ("/",methods=["GET", "POST"])
def index():
    return "hello from flask"  

# Create a Twilio client object with your account SID and auth token
client =  Client(account_sid, auth_token)
#clientopenAi = OpenAI()
clientopenAi = OpenAI(
     base_url="https://api.endpoints.anyscale.com/v1",
     api_key=anyscale_api_key 
)
# Create a list to store the last 10 conversations/queries
history = []

# Handle incoming messages
@app.route('/sms', methods=['POST'])
def handle_incoming_message():

    try:
        
        incoming_message = request.form['Body']
        
        if incoming_message.lower() == 'restart':
            print('Restarting app...')
            # You can replace the command with the appropriate command to restart your app
            os.execv(sys.executable, ['python'] + sys.argv)
        else:
            # Add the new message to the history list
            history.append(f"user query: {incoming_message}")
            
            # Remove the oldest message if the history list size is greater than 10
            if len(history) > 10:
                history.pop(0)
            
            # Pass the history list to ChatGPT with message indicating it's previous user messages
            prompt = incoming_message+"\nThese messages below are my previous messages:\n" + "\n".join(history) + "\nPlease use these as a backup when the current message is not sufficient or more information is needed.\n"
            print(prompt)

            response = clientopenAi.chat.completions.create(
            model=MODEL_NAME,
            response_format={ "type": "json_object" },
            messages=[
                {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
                {"role": "user", "content": prompt}
            ]
            ).choices[0].message.content
            print(response)

            print("before append history :",history)
            # Add the ChatGPT response to the history list
            history.append(f"{MODEL_NAME} response: {response}")

            print("HISTORY:\n",history)
            # Remove the oldest message if the history list size is greater than 10
            if len(history) > 10:
                history.pop(0)
            
            # Create a Twilio MessagingResponse object
            twilio_response = MessagingResponse()

            # Add the response to the Twilio MessagingResponse object
            msg = twilio_response.message()
            msg.body(response)

            # Send the response back to the user
            print("twilio_response :",twilio_response)

            # Return the Twilio MessagingResponse object
            return str(twilio_response)
    except:
        pass
    return 'OK',200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
    