from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return render(request, 'prototype/index.html')
def polttopallo(request):
    return render(request, 'prototype/polttopallo.html')
