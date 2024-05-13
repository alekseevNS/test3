from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index_page(request: HttpRequest) -> HttpResponse:
    context = {"page_name": "Главная"}

    return render(request, "ajax_site/index_page.html", context)