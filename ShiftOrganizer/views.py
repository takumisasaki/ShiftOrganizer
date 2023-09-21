from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
from django.http import JsonResponse

@csrf_exempt
def receive_data(request):
    if request.method == 'POST':
        value = request.POST.get('value', '')
        print('start-date',request.POST.get('start-date'))
        print('end-date',request.POST.get('end-date'))
        data = {
            'start-date': request.POST.get('start-date'),
            'end-date': request.POST.get('end-date')
        }
        with open('schedule.json', 'w')as file:
            json.dump(data, file)
        
        with open('schedule.json', 'r') as file:
            read_data = json.load(file)
        print('--------',read_data)

        return JsonResponse({"status": "success", "value": value})
    return JsonResponse({"status": "error"}, status=400)

@csrf_exempt
def get_schedule(request):
    with open('schedule.json', 'r') as file:
            read_data = json.load(file)
    if (read_data):
         print('dateあり')
         return JsonResponse({"status": "success", "read_data": read_data})
    return JsonResponse({'read_data': ''})