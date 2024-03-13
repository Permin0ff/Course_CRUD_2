from django.contrib import admin
from django.urls import path
from crud import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path("create/", views.create),
    path("edit/<int:id>/", views.edit),
    path("delete/<int:id>/", views.delete),
]
