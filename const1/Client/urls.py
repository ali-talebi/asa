
from .views import team_introduction
from django.urls import path 

app_name = "client"
urlpatterns = [
    path('about_us/' , team_introduction , name="team_introduction")

]