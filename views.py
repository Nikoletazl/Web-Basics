import random

from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views
from django.urls import reverse_lazy
from django.views.generic import TemplateView


def home(request):
    print(reverse_lazy('index'))
    print(reverse_lazy('go to home'))
    print(reverse_lazy('list departments'))
    rand_number = random.randint(0, 1024)
    context = {
        "number": rand_number,
    }
    # if request.method == 'POST':
    #     return HttpResponse(f"{request.method}: This is home",
    #                         status=201,
    #                         content_type='text/plain',
    #                         headers={
    #                             "x-nikoleta-header": "Django"
    #                         })
    # else:
    #     return HttpResponse(f"{request.method} This is home")
    #
    return render(request, 'index.html', context)


def department_details(request, id):
    if not isinstance(id, int):
        pass
    return HttpResponse(f"This is department {id}")


def departments_list(request):
    return HttpResponse("This is a list of departments")


def go_to_home(request):
    return redirect('department details', id=random.randint(1, 1024))


def not_found(request):
    return HttpResponseNotFound()