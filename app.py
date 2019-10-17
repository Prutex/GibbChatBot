from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    keyword = request.form.get('Body')

    # Create reply
    resp = MessagingResponse()

    if keyword == 'Stundenplan':
        resp.message('''
        Dein Stundenplan ist wie folgt:
        https://tipo.webuntis.com/WebUntis/api/public/printpreview/timetable?type=1&id=10667&date=20191016&formatId=1&filter.departmentId=-1
        ''')
        return str(resp)

    elif keyword == 'Dör':
        resp.message('LEEEEEGII')
        return str(resp)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
