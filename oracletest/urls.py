from django.urls import path

from oracletest import views

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

api_info =  openapi.Info(
      title="Hr api docs",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="MIT License"),
   )

schema_view = get_schema_view(
   api_info,
   public=True,
   permission_classes=(permissions.AllowAny,),
)

app_name = "oracletest"  # by this we can access the urls like "tasks:add" for example
urlpatterns = [
    path("employee", views.index, name="index"),
    path("employee/<int:employeeId>", views.employeeById, name="employeeById"),
    path("api/employee", views.api_employee),
    path("api/employee/<int:employeeId>", views.api_employeeById),
    path("api/job", views.api_jobs),
    path('api/docs', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]