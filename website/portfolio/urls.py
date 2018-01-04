from django.urls import path
from django.views.generic import TemplateView
from . import views 

app_name = 'portfolio'
urlpatterns = [
	path('home/', views.IndexView.as_view()),
]
