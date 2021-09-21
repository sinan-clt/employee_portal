from django.db.models import fields
from rest_framework import serializers
from employees.models import employee

class employee_serializer(serializers.ModelSerializer):
    class Meta:
        model=employee
        fields=('id','first_name','last_name','contact','department','email')