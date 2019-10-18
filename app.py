from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from own import prntTest, imagef

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/testing")
def testing():
    prntTest()
    imagef('funtion testing', 'works')
    return 'The Page works'

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    keyword = request.form.get('Body')

    # Create reply
    resp = MessagingResponse()

    if keyword == 'help':
        resp.message('''
        Stundenplan
        Dör
        lb
        Ferien
        ''')

    if keyword == 'Stundenplan':
        resp.message('''
        Dein Stundenplan ist wie folgt:
        https://tipo.webuntis.com/WebUntis/api/public/printpreview/timetable?type=1&id=10667&date=20191016&formatId=1&filter.departmentId=-1
        ''')
        return str(resp)

    elif keyword == 'Dör':
        resp.message('LEEEEEGII')
        return str(resp)

    elif keyword == 'lb':
        resp.message('''
        ——————————DIENSTAG————————————
        29.10 M947 Test w 100% (Unit 1)
        22.10 WR Test 1 50%
        10.12 WR Test 2 50%
        12.11 M926 Test 2
        17.12 M926 Test 3
        ——————————MITTWOCH———————————
        13.11 M157 LB2 50%
        08-15.01 M157 LB3 35%
        16.10 M146 LB1 40%
        08.01 M146 LB2 60%
        ——————————————————————————
        ''')
        return str(resp)
    elif keyword == 'Ferien':
        resp.message('''
        Ferien & freie Arbeitstage:
        23.09.2019 - 12.10.2019 Herbstferien (gibb)
        Winterferien 23.12.2019 - 04.01.2020
        ''')

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
