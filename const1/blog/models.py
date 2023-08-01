from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User 
from Client.models import client_register 

# Create your models here.



class Blogs(models.Model) : 
    head_picture = models.FileField(verbose_name="عکس سر تیتر " , upload_to="Images_Blog/" , null = True )
    title = models.CharField(verbose_name='عنوان' , max_length=100 )
    time = models.DateTimeField(verbose_name="زمان" , auto_now=False , auto_now_add= True )
    author = models.ForeignKey(client_register , on_delete=models.CASCADE , verbose_name="نویسنده")
    text = RichTextField(verbose_name = "محتوا" ) 
    dasteh_bandy = models.ForeignKey( 'dasteh_bandy_model'  , related_name="blog" , verbose_name="دسته بندی " , on_delete=models.CASCADE )
    tags = models.ManyToManyField('Tag' ,   verbose_name="تگ ها "  )




    def __str__(self ) : 
        return self.title 
    

    class Meta : 
        db_table = "Blogs"
        verbose_name_plural = "بلاگ ها "

    
class dasteh_bandy_model(models.Model) : 
    title = models.CharField(verbose_name="عنوان"  , max_length= 100 ) 
    slug = models.SlugField(verbose_name="آدرس اینترنتی " , unique= True )

    

    def __str__(self) : 
        return self.title 
    
    class Meta : 
        db_table = "dasteh_bandy"
        verbose_name_plural = "دسته بندی ها "


    

class Tag(models.Model) : 
    title = models.CharField(verbose_name="عنوان"  , max_length= 100 )
    slug = models.SlugField(verbose_name="آدرس اینترنتی " , unique= True  )


    def __str__(self  ) : 
        return self.title 
    
    class Meta : 
        db_table = "Tag"
        verbose_name_plural = "تگ ها "
 



class comments(models.Model) :
    blog = models.ForeignKey(Blogs , verbose_name="بلاگ" , on_delete=models.CASCADE )  
    name = models.CharField(verbose_name="نام "  , max_length= 100 ) 
    email = models.EmailField(verbose_name="ایمیل" ) 
    website = models.SlugField(verbose_name="وب سایت" , null=True , blank = True   )
    message = models.TextField(verbose_name="پیام " )
    #time = models.DateTimeField(verbose_name="زمان ساخت" , auto_now=False , auto_now_add=True , null = True )


    class Meta : 
        db_table = "comments"
        verbose_name_plural = "کامنت ها "
