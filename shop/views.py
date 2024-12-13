from django.shortcuts import render

from .models import Course


def index(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': courses})
