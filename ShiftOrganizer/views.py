from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
from django.http import JsonResponse
from .models import Schedule
from django.db import connection
from django.http import HttpResponse
from django.core import serializers
from datetime import datetime

@csrf_exempt
def receive_data(request):
    if request.method == 'POST':
        value = request.POST.get('value', '')
        print('start-date',request.POST.get('start-date'))
        print('end-date',request.POST.get('end-date'))
        start_time = change_format(request.POST.get('start-date'))
        end_time = change_format(request.POST.get('end-date'))
        print(start_time, end_time)
        table_name = Schedule._meta.db_table
        sql = "INSERT INTO {} (start_time, end_time) VALUES (%s, %s)".format(table_name)
        with connection.cursor() as cursor:
            cursor.execute(sql, [start_time, end_time])
                
 
        # data = {
        #     'start-date': request.POST.get('start-date'),
        #     'end-date': request.POST.get('end-date')
        # }
        return JsonResponse({"status": "success", "value": value})
    return JsonResponse({"status": "error"}, status=400)

def change_format(data):
    cleaned_str = data.split(" (")[0]

    dt_obj = datetime.strptime(cleaned_str, "%a %b %d %Y %H:%M:%S GMT%z")

    # datetime オブジェクトを目的の形式の文字列に変換
    formatted_str = dt_obj.strftime("%Y-%m-%d %H:%M:%S")

    return formatted_str  # 2023-10-06 06:00:00


@csrf_exempt
def get_schedule(request):
    # GETリクエストのみを受け入れる
    if request.method != 'GET':
        return JsonResponse({'error': 'Only GET requests are allowed'}, status=405)

    select_date = change_format(request.GET.get('date'))
    # select_date = select_date.replace('-', ',')
    dt = datetime.strptime(select_date, "%Y-%m-%d %H:%M:%S")
    target_date = dt.date()
    schedules = Schedule.objects.filter(start_time__date=target_date)
    print(schedules.query)  # 実行されるSQLクエリを表示

    for schedule in schedules:
        print(f"ID: {schedule.id}, Start Time: {schedule.start_time}, End Time: {schedule.end_time}")

    schedules_json = serializers.serialize('json', schedules)
    return JsonResponse(schedules_json, safe=False)