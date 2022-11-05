from django.urls import path
from . import views




urlpatterns = [
    path('solve',views.arithmetic,name="arithmetic")
]