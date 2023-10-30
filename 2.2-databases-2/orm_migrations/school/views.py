from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    template = 'school/students_list.html'
    students = Student.objects.all()
    context = {'students': students}

    # была проблема с учителями пришлось вручную связывать их с учениками
    ordering = 'group'

    return render(request, template, context)
