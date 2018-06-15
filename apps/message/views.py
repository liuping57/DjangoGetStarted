from django.shortcuts import render
from message.models import UserMessage


def getfrom(request):
    message = None
    all_message = UserMessage.objects.filter(name="xinjie")

    if all_message:
        message = all_message[0]

    # if  request.method == "POST":
    #     name=request.POST.get("name", '')
    #     message = request.POST.get("message", '')
    #     address = request.POST.get("address", '')
    #     email = request.POST.get("email", '')
    #
    #     user_message = UserMessage()
    #     user_message.name = name
    #     user_message.message = message
    #     user_message.address = address
    #     user_message.email = email
    #     user_message.object_id = "agadc"
    #     user_message.save()

    return render(request, "form.html",
                  {"my_message": message})


# Create your views here.
