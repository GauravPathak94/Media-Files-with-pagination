from django.urls import URLPattern, path
from .import views

urlpatterns = [
    path('ev/', views.EmployeeView, name='form_url'),
    path('sv/', views.ShowEmployeeView, name='show_url'),
    path('sv/<int:page>/',views.ShowEmployeeView, name="Show_url"),
    path('uv/<int:id>/',views.UpdateEmployeeView, name='update_url'),
    path('dl/<int:id>/',views.DeleteEmployeeView, name='delete_url')
]