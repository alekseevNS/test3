"""
URL configuration for ajax_server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path

import ajax_site.views

urlpatterns = [
    path("", ajax_site.views.index_page),
    path("json_test/", ajax_site.views.json_answer),
    path("blog/", ajax_site.views.blog_page),
    path("get_blog/", ajax_site.views.get_blog),
]
