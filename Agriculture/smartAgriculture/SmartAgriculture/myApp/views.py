from django.shortcuts import render
from . models import Agriculture
import joblib
from twilio.rest import Client
from time import sleep

account_sid = "AC65e62960f555601d67c82221acd7001d"
auth_token = "6520ac05419262908cb65c784dcb7038"
client = Client(account_sid, auth_token)


def home(request):
    last_agriculture_data = Agriculture.objects.order_by('-id').first()

    if last_agriculture_data.motor == 'ON':
        sendsms()
    return render(request, 'home.html', {'last_agriculture_data': last_agriculture_data})

def predect(request):
    return render(request, 'predect.html')


def result(request):
    cls = joblib.load('crop_app.pkl')

    lis = []

    lis.append(request.GET['N'])
    lis.append(request.GET['P'])
    lis.append(request.GET['K'])
    lis.append(request.GET['temp'])
    lis.append(request.GET['humid'])
    lis.append(request.GET['ph'])
    lis.append(request.GET['rainfall'])

    out = cls.predict([lis])

    return render(request, 'result.html', {'ans': out})



def sendsms():
    message = client.messages.create(
        messaging_service_sid="MG18c4481c6e42eebdabd4b4c5b097b507",
        body="Hello, Water is very low..! Dont worry i just turned on the motor",
        to="+916305151632"
    )

    # Check the status of the message
    status = client.messages(message.sid).fetch().status
    print(f"Message Status: {status}")

    if status == "failed":
        print("Message failed to send.")
    else:
        print("Message sent successfully.")

    sleep(2)
