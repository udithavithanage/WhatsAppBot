from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

# Initialize Flask app
app = Flask(__name__)

# Route to handle WhatsApp messages
@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    # Get the incoming message and media information
    incoming_msg = request.form.get("Body", "").strip().lower()
    num_media = int(request.form.get("NumMedia", 0))  # Number of media files sent
    response = MessagingResponse()
    message = response.message()

    # Check if the user sent media
    if num_media > 0:
        # Get the media URL (first media in case of multiple files)
        media_url = request.form.get("MediaUrl0")
        content_type = request.form.get("MediaContentType0")  # e.g., image/jpeg
        
        # Respond with the image the user sent
        message.body("Thank you for the image! Sending it back to you:")
        message.media(media_url)
    else:
        # Handle text responses
        if incoming_msg == "hello":
            message.body("Hi there! How can I assist you today?")
        elif incoming_msg == "help":
            message.body("Here are some things you can ask:\n1. Services\n2. Support\n3. Contact Us")
        else:
            message.body("I'm sorry, I didn't understand that. Type 'help' for options.")

    return str(response)

# Run the app
if __name__ == "__main__":
    app.run(port=5000)
