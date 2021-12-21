from . import views
from django.urls import path


urlpatterns = [
    path('create/',views.laptopcreateview.as_view(),name='create_laptop'),
    path('list/',views.laptoplistview.as_view(),name='list_laptop'),
    path('update/<int:pk>/',views.laptopupdateview.as_view(),name='update_laptop'),
    path('delete/<int:pk>/',views.laptopdeleteview.as_view(),name='delete_laptop'),
]