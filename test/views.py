from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(request):
    #return HttpResponse("Hello, world. You're at test.")# Create your views here.
    return render_to_response("base.html", {'message' : "Data not available for this user"})


def detail(request, test_id):
    return HttpResponse("You're looking at test %s." % test_id)

def results(request, test_id):
    return HttpResponse("You're looking at the test %s." % test_id)