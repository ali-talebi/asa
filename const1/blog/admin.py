from django.contrib import admin
from .models import Blogs , dasteh_bandy_model , Tag , comments 


# Register your models here.
@admin.register(Blogs)
class Blogs_admin(admin.ModelAdmin) : 
    list_display = ("title" , "time" , "author" , "dasteh_bandy" , "Func_tags")
    fields = ( "head_picture" , ("title" , "author" ) , ("dasteh_bandy" , "tags" )  , "text"  ) 
    list_editable = ("author" , )

    def  Func_tags(self , obj ) : 
        return ' - '.join([i.title for i in obj.tags.all() ])
    
    Func_tags.short_description = "تگ ها "

@admin.register(dasteh_bandy_model)
class dasteh_bandy_model_admin(admin.ModelAdmin) : 
    list_display = ("title" , "slug" )
    prepopulated_fields = {'slug' : ("title" , )}


@admin.register(Tag)
class Tag_admin(admin.ModelAdmin) : 
    list_display = ("title" , "slug" ) 
    prepopulated_fields = {'slug':("title" , )}
    
@admin.register(comments)
class comments_admin(admin.ModelAdmin) : 
    list_display = ("blog" , "name" , "email" , "website" , "message" )
