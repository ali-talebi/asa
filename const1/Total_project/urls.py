from django.urls import path 
from .views import contact_us_view , detail_Services , message_save_successfully  , blog_filter_category , blog_filter_tag ,  Home , detail_project , detail_blog , search_form 

app_name = "project"
urlpatterns = [
    
    path("" , Home , name="Home") ,
    path("detail_project/<int:id>/" , detail_project , name = "detail_project" ) , 
    path("detail_blog/<int:id>/" , detail_blog , name="detail_blog" ) ,
    path("search/" , search_form , name="search_form" ) , 
    path('tag/<slug:tag>/' , blog_filter_tag , name = "blog_filter_tag" ) , 
    path('category/<slug:category>/' , blog_filter_category , name = "blog_filter_category" ) , 
    path("save_idead/" , message_save_successfully , name='save_message_idea') , 
    path('detail_Services/' , detail_Services , name="d_services" ) , 
    path("detail_Services/<int:id>" , detail_Services , name="detail_Services" ) , 
    path('contact_us_view' , contact_us_view , name="contact_us" ) , 
]