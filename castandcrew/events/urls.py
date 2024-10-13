from django.urls import path
from . import views


urlpatterns = [
path('', views.dashboard, name='event_dashboard'),
path('<int:id>/', views.event_details, name='event_details'),

]