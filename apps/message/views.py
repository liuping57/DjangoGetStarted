from django.shortcuts import render
from message.models import UserMessage


def getfrom(request):
    all_message = UserMessage.objects.all()
    for message in all_message:
        print(message.name)

    if  request.method == "POST":
        name=request.POST.get("name", '')
        message = request.POST.get("message", '')
        address = request.POST.get("address", '')
        email = request.POST.get("email", '')

        user_message = UserMessage()
        user_message.name = name
        user_message.message = message
        user_message.address = address
        user_message.email = email
        user_message.object_id = "agadc"
        user_message.save()

    return render(request, "form.html")


# Create your views here.
