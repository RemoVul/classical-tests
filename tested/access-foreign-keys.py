from django.http import HttpResponse
from models import User

def cool_view(request):
    return HttpResponse({'user_id': request.user.id})

def other():
    print(User.user.id)
def other():
    print(User.user.id)
def other():
    print(User.user.id)
