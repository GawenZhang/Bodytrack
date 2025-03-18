from django.shortcuts import render

# Create your views here.


def plan(request):
    return render(request, 'plan.html')


def report(request):
    return render(request, 'report.html')