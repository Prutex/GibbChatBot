from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from own import prntTest, imagef
import time
import random

app = Flask(__name__)
version = 'Version 0.1.2.6'
url = "https://chatgibbbot.azurewebsites.net/"


@app.route("/")
def hello():
    return version


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
        resp.message(version + ' ' + url + '' + '''
        Stundenplan
        Dör
        lb
        Ferien
        Roll
        Can Now play Rock, Papers, Scissors(Type your move: "Stein" or "Papier" or "Schere"  
        ''')
        return str(resp)

    if keyword == 'Stundenplan':

        txt = time.asctime()
        xtime = txt.split()
        etime = xtime[3].split(':')

        if xtime[0] == 'Tue':
            if int(etime[0]) < 10:
                resp.message('08:45 - 09:30 Englisch(947) – Reist Daniela - 106')
            elif int(etime[0]) < 12:
                resp.message('10:00 - 11:30 Wirtschaft und Recht(915) – Pieren Benno - 307')
            elif int(etime[0]) < 15:
                resp.message('13:30 - 15:00 Naturwiss. Grundlagen(926) – Nydegger Martin - U03')
            elif int(etime[0]) < 17:
                resp.message('15:30 - 17:00 ABU – Gerber Simone - 215')

        elif xtime[0] == 'Wed':
            if int(etime[0]) < 10:
                resp.message(' 08:00 - 09:30 Hardware(157) – Jäggi Thomas - 303')
            elif int(etime[0]) < 12:
                resp.message('10:00 - 11:30 Internetanbindung(146) – Kratzer Michael - 146')
            elif int(etime[0]) < 14:
                resp.message('12:30 - 14:00 IT-Kleinprojekt(306) – Yilmaz Günel - 309')
            elif int(etime[0]) < 17:
                resp.message('14:15 - 15:45 Teamverhalten(213) – Yilmaz Günel - 209')
        else:
            if xtime[0] == "Mon":
                today = "Montag"
            elif xtime[0] == "Tue":
                today = "Donnerstag"
            elif xtime[0] == "Fri":
                today = "Freitag"
            resp.message('Heute hast du keine Schule weil heute ist:' + today)
        return str(resp)

    if keyword == 'Dör':
        resp.message('LEEEEEGII')
        return str(resp)

    if keyword == 'Schere' or keyword == 'Stein' or keyword == 'Papier':
        moves = ['Schere', 'Stein', 'Papier']
        time.sleep(5)
        move = moves[random.randrange(0, 2)]
        resp.message(move)

        if keyword == move:
            time.sleep(2)
            resp.message("it's a draw")
            time.sleep(2)
            return str(resp)
        elif keyword == 'Schere' and move == "Papier":
            time.sleep(2)
            resp.message("You Won!")
            time.sleep(2)
            return str(resp)
        elif keyword == 'Schere' and move == "Stein":
            time.sleep(2)
            resp.message('Suck it, I Won!')
            time.sleep(2)
            return str(resp)
        elif keyword == 'Stein' and move == 'Papier':
            time.sleep(2)
            resp.message('Suck it, I won!')
            time.sleep(2)
            return str(resp)
        elif keyword == 'Stein' and move == 'Schere':
            time.sleep(2)
            resp.message('You Won!')
            time.sleep(2)
            return str(resp)
        elif keyword == 'Papier' and move == 'Schere':
            time.sleep(2)
            resp.message('Suck it, I won!')
            time.sleep(2)
            return str(resp)
        elif keyword == 'Papier' and move == 'Stein':
            time.sleep(2)
            resp.message('You won!')
            time.sleep(2)
            return str(resp)

    if keyword == 'lb':
        resp.message('''
      ——————————DIENSTAG————————————
    04.02 M947 Unit 3 - Network (Unit 3 - halb)
    11.02 M915 Test 3 (FIBU / Budget - ganz)
    10.03 M915 Test 4 (Kennzahlen - ganz)
    02.06 M915 Test 5 (Rechtsformen - ganz)
    18.02 M926 LB1 (ganz)
    24.03 M926 LB2 (ganz)
    16.06 M926 LB3 (ganz)
    ——————————MITTWOCH———————————
    08-15.01 M157 LB3 35%
    15.01 M146 LB2 60%
    ——————————————————————————
        ''')
        return str(resp)

    if keyword == 'Ferien':
        resp.message('''
        Ferien & freie Arbeitstage:
        Frühling 2020	30.03.2020 - 18.04.2020 (KW14 - KW16)
        Sommer 2020	29.06.2020 - 08.08.2020 (KW27 - KW32)
        BMS: Teilabschluss- und Abschlussklassen ab 06.07.2020
        ''')
        return str(resp)
    if keyword == 'Roll':
        resp.message(str(random.randrange(0, 100)))
        return str(resp)

    if keyword == 'Version':
        resp.message(version)
        return str(resp)

    else:
        resp.message("I don't know this Command, you said: " + keyword)
        return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
