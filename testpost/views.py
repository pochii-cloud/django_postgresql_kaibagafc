from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from django.views.generic import TemplateView, FormView

from testpost.forms import JoinForm


def base(request):
    return render(request, 'base.html')


def fixtures(request):
    return render(request, 'fixtures.html')


def squad(request):
    return render(request, 'squad.html')


def stats(request):
    return render(request, 'stats.html')


def results(request):
    return render(request, 'results.html')


def finance(request):
    return render(request, 'finance.html')


def join(request):
    form =JoinForm()
    if request.POST:
        form = JoinForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('request sent successfully')
    return render(request, 'join us.html', {'form': form})


def footer(request):
    return render(request, 'footer.html')
