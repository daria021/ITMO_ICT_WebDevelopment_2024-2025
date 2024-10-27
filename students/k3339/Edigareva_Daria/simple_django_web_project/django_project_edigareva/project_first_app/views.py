from django.http import Http404
from django.shortcuts import render

from .models import CarOwner  # Импорт модели CarOwner


def owner_detail(request, owner_id):
    try:
        owner = CarOwner.objects.get(pk=owner_id)  # Получаем владельца по ID
    except CarOwner.DoesNotExist:
        raise Http404("Владелец автомобиля не найден")
    return render(request, 'owner.html', {'owner': owner})  # Передаем объект "owner" в шаблон
