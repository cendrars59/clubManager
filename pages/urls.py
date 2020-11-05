from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = "pages"

urlpatterns = [
    path("", views.home, name="home"),
    path("mentions", views.mentions, name="mentions"),

]
