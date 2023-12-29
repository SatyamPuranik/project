from django.urls import path
from app import views

app_name = 'app'

urlpatterns = [
    path('', views.home,name="home"),
    path('ask/', views.ask,name="ask"),
    path('icecream/', views.icecream,name="icecream"),
    path('thankyou/', views.thankyou, name='thankyou')
]