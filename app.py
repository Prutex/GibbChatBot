from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from own import prntTest, imagef
import time
import random

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
        Can Now play Rock, Papers, Scissors(Type your move: "Stein" or "Papier" or "Schere"  
        ''')
        return str(resp)

    if keyword == 'Stundenplan':

        txt = time.asctime()
        xtime = txt.split()
        etime = xtime[3].split(':')

        if xtime[0] == 'Tue':
            if int(etime[0]) < 10:
                resp.message('08:45 - 09:30 Englisch(947) – Reist Daniela')
            elif int(etime[0]) < 12:
                resp.message('10:00 - 11:30 Wirtschaft und Recht(915) – Pieren Benno')
            elif int(etime[0]) < 15:
                resp.message('13:30 - 15:00 Naturwiss. Grundlagen(926) – Nydegger Martin')
            elif int(etime[0]) < 17:
                resp.message('15:30 - 17:00 ABU – Gerber Simone')

        elif xtime[0] == 'Wed':
            if int(etime[0]) < 10:
                resp.message(' 08:00 - 09:30 Hardware(157) – Jäggi Thomas')
            elif int(etime[0]) < 12:
                resp.message('10:00 - 11:30 Internetanbindung(146) – Kratzer Michael')
            elif int(etime[0]) < 14:
                resp.message('12:30 - 14:00 IT-Kleinprojekt(306) – Yilmaz Günel')
            elif int(etime[0]) < 17:
                resp.message('14:15 - 15:45 Teamverhalten(213) – Yilmaz Günel')
        else:
            resp.message('Heute hast du keine Schule weil heute ist:' + xtime[0])
        return str(resp)

    elif keyword == 'Dör':
        resp.message('LEEEEEGII')
        return str(resp)
    elif keyword == 'Schere' or 'Stein' or 'Papier':
        moves = ['Schere', 'Stein', 'Papier']
        move = moves[random.randrange(0, 2)]
        resp.message(move)
        if keyword == move:
            resp.message("it's a draw")
        elif keyword == 'Schere' and move == "Papier":
            resp.message("You Won!")
        elif keyword == 'Schere' and move == "Stein":
            resp.message('Suck it, I Won!')
        elif keyword == 'Stein' and move == 'Papier':
            resp.message('Suck it, I won!')
        elif keyword == 'Stein' and move == 'Schere':
            resp.message('You Won!')
        elif keyword == 'Papier' and move == 'Schere':
            resp.message('Suck it, I won!')
        elif keyword == 'Papier' and move == 'Stein':
            resp.message('You won!')





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
    else:
        resp.message("I don't know this Command, you said: " + keyword)
        return str(resp)

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
