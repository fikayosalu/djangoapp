from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello, world.This is my second django app.")
