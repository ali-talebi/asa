from django.contrib import admin
from .models import client_register , History_website 
# Register your models here.


@admin.register(client_register)
class client_register_admin(admin.ModelAdmin) : 
    list_display = ("user" , "position" , "instagram" , "faceboob" , "linkedin" , "fields" )

@admin.register(History_website)
class History_website_admin(admin.ModelAdmin) : 
    list_display = ("title" , "time"  , )