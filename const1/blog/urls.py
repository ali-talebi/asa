from django.urls import path 
from .views import show_Blog  , detail_blog 


app_name = "blog"
urlpatterns = [
    path("" , show_Blog , name = "show_Blog" ) , 
    path('details/<int:id>/' , detail_blog , name="detail_blog" ) , 
]
