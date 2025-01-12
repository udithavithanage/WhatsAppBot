from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

# Initialize Flask app
app = Flask(__name__)

# Route to handle WhatsApp messages
@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    # Get the incoming message from the user
    incoming_msg = request.form.get("Body").strip().lower()

    # Initialize Twilio response
    response = MessagingResponse()
    message = response.message()

    # Define chatbot responses
    if incoming_msg == "hello":
        message.body("Hi there! How can I assist you today?")
    elif incoming_msg == "help":
        message.body("Here are some things you can ask:\n1. Services\n2. Support\n3. Contact Us")
    elif incoming_msg == "services":
        message.body("We offer the following services:\n- Service 1\n- Service 2\n- Service 3")
    else:
        message.body("I'm sorry, I didn't understand that. Type 'help' for options.")
    
    return str(response)

# Run the app
if __name__ == "__main__":
    app.run(port=5000)
