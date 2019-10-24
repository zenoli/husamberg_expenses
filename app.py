from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from commands import commands
import command_ids
import re

app = Flask(__name__)

@app.route("/")
def hello():

    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    sender = request.form.get('From')

    cmd, args = parse_msg(msg)
    response_msg = commands[cmd](*args)
    # Create reply
    resp = MessagingResponse()
    resp.message(response_msg)
    
    return str(resp)



# Flatmates



def parse_msg(msg):
    words = msg.split()
    n = len(words)
    app.logger.info(f'Number of words are: {n}')
    command = words[0]
    if re.match(command_ids.HELP, command, re.IGNORECASE):
        return (command_ids.HELP, [])
    elif re.match(command_ids.INIT, command, re.IGNORECASE):
        return (command_ids.INIT, [words[1]]) if n > 1 else (command_ids.UNKNOWN, [])
    else:
        return (command_ids.UNKNOWN, [])


if __name__ == "__main__":
    app.run(debug=True)