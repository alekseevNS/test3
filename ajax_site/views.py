from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render

from ajax_site.models import BlogModel


def get_base_menu() -> list:
    return [
        {"link": "/", "text": "Главная"},
        {"link": "/json_test/", "text": "Проверка получения JSON"},
        {"link": "/blog/", "text": "Блог"},
    ]


def index_page(request: HttpRequest) -> HttpResponse:
    context = {"page_name": "Главная", "menu_items": get_base_menu()}

    return render(request, "ajax_site/index_page.html", context)


def blog_page(request: HttpRequest) -> HttpResponse:
    context = {
        "page_name": "Блог",
        "menu_items": get_base_menu(),
        "blog_items": BlogModel.objects.all(),
    }

    return render(request, "ajax_site/blog_page.html", context)


def get_blog(request: HttpRequest) -> JsonResponse:
    blog_item = BlogModel.objects.get(id=request.GET.get("blog_id"))
    context = {"status": "success", "data": {"title": blog_item.title, "text": blog_item.text}}

    return JsonResponse(context)


def json_answer(request: HttpRequest) -> JsonResponse:
    context = {"status": "success", "data": "Всем привет!"}

    return JsonResponse(context)
