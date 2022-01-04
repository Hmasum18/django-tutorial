from django.urls import path

from tasks import views

app_name = "tasks"  # by this we can access the urls like "tasks:add" for example
urlpatterns = [
    path("", views.index, name="index"),
    path("add", views.add_task, name="add"),
]