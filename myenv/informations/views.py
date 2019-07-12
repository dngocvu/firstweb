from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

from .models import Course
# Create your view here


def index(request):
    informations = Course.objects
    return render(request, 'informations/index.html', {'courses': informations})


def detail(request, course_id):
    course_detail = get_object_or_404(Course, pk=course_id)
    return render(request, 'informations/detail.html', {'course': course_detail})
