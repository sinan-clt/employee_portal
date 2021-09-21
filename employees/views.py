from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.http.response import JsonResponse
from employees.serializers import employee_serializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from . models import *



# Create your views here.

@csrf_exempt
def select_datas(request,id=0):
    if request.method=='GET':
        emp_datas=employee.objects.all()
        serializer_data=employee_serializer(emp_datas, many='True')
        return JsonResponse(serializer_data.data, safe=False)

    elif request.method=='POST':
        datas=JSONParser().parse(request)
        serlzrdata=employee_serializer(data=datas)
        if serlzrdata.is_valid():
            serlzrdata.save()
            return JsonResponse('Employee added Succesfully :)', safe=False)
        return JsonResponse('Failed to add Employee', safe=False)

    elif request.method=='DELETE':
        del_data=employee.objects.get(id=id)
        del_data.delete()
        return JsonResponse('Employeee removed :(', safe=False)

    elif request.method=='PUT':
        userdata=JSONParser().parse(request)
        user=employee.objects.get(id=userdata['id'])
        serializerdata=employee_serializer(user,userdata)
        if serializerdata.is_valid():
            serializerdata.save()
            return JsonResponse('Data updated Succesfully', safe=False)
        return JsonResponse('Failed to Update', safe=False)
        
        

    
