from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def endpoints(request):
    data = ['/advocates', 'advocates/:username']
    return JsonResponse(data, safe=False)

def advocates_list(request):
    data = ['kailesh','andrej','andrew ng']
    return JsonResponse(data, safe=False)
