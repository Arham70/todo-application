from django.contrib import admin
from django.urls import path
from todo_app import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Todo Application",
        default_version='v1',
        description="Test Swagger First app",
        terms_of_service="http://www.ourapp.com/policies/terms/",
        contact=openapi.Contact(email="contact@todo.local"),
        license=openapi.License(name="Test License")
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/GetTodo/', views.GetApi),
    path('api/GetSpecificTodo/<int:pk>', views.GetApi),
    path('api/CreateTodo/', views.CreateApi),
    path('api/CompleteUpdateTodo/<int:pk>', views.UpdateApi),
    path('api/PartialUpdateTodo/<int:pk>', views.PartialUpdateApi),
    path('api/DeleteTodo/<int:pk>', views.DeleteApi),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
