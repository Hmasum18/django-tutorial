from django.urls import path
from test_app import views

urlpatterns = [
    path("", views.test_index, name="test_index"),
    path("masum", views.masum, name="masum"),
    path("<str:user_name>",views.greet, name="greet"),
    #path("<str:name>",views.greetings, name="greetings"),
]