import random

from django.http import HttpResponseNotFound, JsonResponse
from django.shortcuts import redirect, render
from rest_framework import status
from django.db import IntegrityError
from .models import URL
from rest_framework.decorators import api_view
import hashlib
from .serializers import URLSerializer
from rest_framework.response import Response


def simple_ui(request):
    urls = URL.objects.all()
    return render(request, 'url/index.html', {'urls': urls})


def redirect_original_url(request, hash):
    try:
        url = URL.objects.get(hash=hash)
        url.visits += 1
        url.save()
        return redirect(url.url)
    except URL.DoesNotExist:
        return HttpResponseNotFound("Short URL not found.")


@api_view(["POST"])
def create_short_url(request):
    if 'url' in request.data:
        original_url = request.data['url']

        while True:
            # Генерация хеша с SHA-256 и добавлением случайности
            hash_value = hashlib.sha256((original_url + str(random.random())).encode()).hexdigest()[:10]

            # Попытка создать новый URL объект
            try:
                url, created = URL.objects.get_or_create(hash=hash_value, defaults={'url': original_url})
                if created:
                    # Если URL успешно создан и сохранен
                    return JsonResponse({'short_url': f'/url/{hash_value}/'}, status=status.HTTP_201_CREATED)
            except IntegrityError:
                # Если происходит ошибка целостности, цикл продолжится
                continue

    return JsonResponse({'error': 'Invalid request data'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_url_stats(request, hash):
    try:
        url = URL.objects.get(hash=hash)
        serializer = URLSerializer(url)
        return Response(serializer.data)
    except URL.DoesNotExist:
        return Response({'error': 'Short URL not found.'}, status=status.HTTP_404_NOT_FOUND)
