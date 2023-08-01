from django.contrib import admin
from .models import contact_us ,  ADDRESS,  Services ,  Testimonials ,  project , Category , Slider_Index , Send_Data_Quote 

# Register your models here.


@admin.register(contact_us)
class contact_us_admin(admin.ModelAdmin): 
    list_display = ("name" , "email" , "subject" , "message" )
    fields = (("name" , "email" ) , "subject" , "message" ) 

@admin.register(ADDRESS)
class ADDRESS_admin(admin.ModelAdmin) : 
    list_display = ("address" , "email" , "phone1" , "phone2" )


@admin.register(Services) 
class Services_Admin(admin.ModelAdmin) :
    list_display = ("title" , "type_service" ) 
    list_editable = ("type_service" , )

@admin.register(project)
class project_admin(admin.ModelAdmin) : 
    list_display = ("title" , "customer" , "date" , "slug" , "type_project" , "category" , "author" )
    list_editable = ("type_project" , "author" )

    fields = ( ("pic1" ,"pic2" , "pic3" ),  ("title" ,"customer") , ("slug" , "type_project" ) , ("category" , "author" ) , "body" , "message_creator"  ) 

@admin.register(Category)
class Category_admin(admin.ModelAdmin) : 
    list_display = ("title" , )


@admin.register(Slider_Index)
class Slider_Index_admin(admin.ModelAdmin) : 
    list_display = ("sentence"  , )

@admin.register(Send_Data_Quote)
class Send_Data_Quote_admin(admin.ModelAdmin) : 
    list_display = ("name" , "email" , "phone" , "message" ) 

    

@admin.register(Testimonials)
class Testimonials_admin(admin.ModelAdmin) : 
    list_display = ("author" , "sentence"  )
    