from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render


def get_base_menu() -> list:
    return [
        {"link": "/", "text": "Главная"},
        {"link": "/json_test/", "text": "Проверка получения JSON"},
    ]


def index_page(request: HttpRequest) -> HttpResponse:
    context = {"page_name": "Главная", "menu_items": get_base_menu()}

    return render(request, "ajax_site/index_page.html", context)


def json_answer(request: HttpRequest) -> JsonResponse:
    context = {"status": "success", "data": "Всем привет!"}

    return JsonResponse(context)
