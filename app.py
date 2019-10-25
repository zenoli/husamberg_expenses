from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from command_list import command_list, find_command
from commands import flatmates
import command_ids
import re


flatmates.load()
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
    cmd, arg_str = parse_cmd(msg)
    response_msg = command_list[cmd](parse_number(sender), arg_str)
    # Create reply
    resp = MessagingResponse()
    resp.message(response_msg)
    
    return str(resp)



# Flatmates

def parse_number(number):
    prefix = 'whatsapp:'
    return number.split(prefix, 1)[1]




def parse_cmd(msg):
    splits = msg.split(maxsplit=1)
    if not splits: return command_ids.UNKNOWN

    if len(splits) > 0: cmd_str = splits[0]
    if len(splits) > 1: arg_str = splits[1].strip()
    else: arg_str = ""

    return find_command(cmd_str), arg_str


if __name__ == "__main__":
    app.run(debug=True)