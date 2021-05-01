import json
from django.http import HttpResponse

data = {
    "Name": "Meg",
    "Track": "Backend(Python)",
    "Message": "Hello, you are awesome! Keep up the incredible work!!"
}

# Create your views here.

def index(request):
    # return HttpResponse(data)
    return HttpResponse(json.dumps(data))