from django.shortcuts import render
from twilio.rest import Client
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

account_sid = 'AC532a984a34288ea2d3e317f0e22091f8'
auth_token = '8ba942ab84e07ed7399d7f88a791650c'
client = Client(account_sid, auth_token)

@csrf_exempt
def bot(request):
    message = request.POST["message"]

    if message == "Bom dia":
        client.messages.create(
                                from_='whatsapp:+14155238886',
                                body='Pfvr, audios com menos de 5 mins. Obg',
                                to='whatasapp:+353830071098'
                            )
    return HttpResponse('Hello')