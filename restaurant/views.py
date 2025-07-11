from http import HTTPStatus
from django.shortcuts import render
from django.http import HttpResponse
from .models import Meal


# Create your views here.
def index(request):
    if request.method == "GET":
        meals = Meal.objects.all()

        return render(request, template_name='restaurant/index.html', context={'meals': meals})

    return HttpResponse(HTTPStatus.BAD_REQUEST)
