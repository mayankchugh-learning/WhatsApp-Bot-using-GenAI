# WhatsApp Chatbot Using Flask and Twilio

### Overview
A chatbot is a computer program designed to simulate conversation through voice commands or text chats (or both) with human users, especially over the internet. The level of intelligence among chatbots vary immensely, some (like the one used here) are very basic, while others can be very sophisticated by employing machine learning algorithms and artificial intelligence in order to attain near human-level conversation.

This application makes use of the [Flask](https://flask.palletsprojects.com/en/1.1.x/) framework and [Twilio API for WhatsApp](https://www.twilio.com/whatsapp) while working with Python.

To use it, ensure you have an active phone number and WhatsApp installed in your smartphone. Create an account with Twilio then register your smartphone with your account(see technical details for more info). You will need to send the code given for your smartphone as a message to the number provided in your account.

![WhatsApp Chatbot Architechture](https://github.com/mayankchugh-learning/WhatsApp-Bot-using-GenAI/blob/main/WhatsApp%20CHAT%20GPT%20Architechture.gif)

### Tools Used
* Python for programming (Python 3.8.19)
* Flask web framework (Flask 3.0.2 & Werkzeug 3.0.2)
* Twilio API for WhatsApp
* Ngrok for temporary provision of Twilio URL
* Visual Studio Code
* OpenAI

### Features
* Real-time automated WhatsApp responses
* Multi-device access to application provided by Ngrok URL


### Testing Locally

To successfully test this application, there are two requirements you will need:
* A smartphone with WhatsApp installed, with an active phone number
* A Twilio Account. You can create a [free Twilio account now](https://www.twilio.com/try-twilio?promo=WNPWrR).

If you do not want to create your own project but would prefer to use this project, you will need to do the following:

1. Clone this repo:

```python
$ git clone https://github.com/mayankchugh-learning/WhatsApp-Bot-using-GenAI.git
```

2. Move into the cloned directory:

```python
$ cd WhatsApp-Bot-using-GenAI
```

3. Create and activate your virtual environment:

```python
$ conda create -p WhatsAppVenv python=3.8 -y
```

```python
$ source activate ./WhatsAppVenv
```

4. Install used dependencies

```python
(WhatsAppVenv)$ pip3 install -r requirements.txt
```

5. Before you can run your server, remember to create a `.env` file following the guidance seen in the `.env.template`. Create a `.env` file in the root directory:

```python
(whatsapp-chatbot)$ touch .env
```

6. Update the `.env` file with all the necessary details.

```python
OPENAI_API_KEY = 
TWILIO_ACCOUNT_SID=
TWILIO_AUTH_TOKEN=
TWILIO_PHONE_NUMBER=
WHATSAPP_PHONE_NUMBER=
```

7. Run the application:

```python
(whatsapp-chatbot)$ python app.py
```

Once your application is running, you can access your localhost on http://127.0.0.1:5000/. Additionally, if you look carefully in your terminal, you will see * Tunnel URL: NgrokTunnel: "https://4209c9af6d43.ngrok.io" -> "http://localhost:5000"

The HTTP value may be different from the one shown here because I am using the free tier package of `ngrok`.

8. Ensure you are still logged in to your Twilio Account: 

    - Go back to the [Twilio Console](https://www.twilio.com/console), 

    - Click on [Programmable Messaging](https://www.twilio.com/console/sms/dashboard), then on [Settings](https://www.twilio.com/console/sms/settings), and finally on [WhatsApp Sandbox Settings](https://www.twilio.com/console/sms/whatsapp/sandbox). 

    - Copy the `https://` URL from the ngrok output and then paste it on the “When a message comes in” field.

    - Our chatbot is exposed in the URL ending with `/bot`. You will need to append `/bot` to the `https://` URL from `ngrok`. 

    - Be certain to set your request method to `HTTP POST`.

    - Click the Save button to apply your changes
    - From _Try It Out/_[Try Whatsapp](https://www.twilio.com/console/sms/whatsapp/learn), you will see a code assigned to you. This code begins with the word `join-`. You will need to use this code to start sending and receiving messages.

From your smartphone, or the WhatsApp Web App, you can try sending messages with sentences including the words 'cat' and 'quote'. Also, try excluding those words.

### Start Sending and Receiving Messages

* Add the phone number +1 415 523 8886  to your contact list.
* Send the code `join-<code>` to the number above. If you have WhatsApp installed, you can [click here](http://wa.me/+14155238886?text=join%20who-smoke).

You can invite your friends to your Sandbox. Ask them to send a WhatsApp Message to the number above with the code shown.

### References

[WhatsApp Bot Documentation.pdf](https://github.com/mayankchugh-learning/WhatsApp-Bot-using-GenAI/blob/main/WhatsApp%20Bot%20Documentation.pdf)