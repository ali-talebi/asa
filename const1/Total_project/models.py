from django.db import models
from django.contrib.auth.models import User 
from Client.models import client_register 
from ckeditor.fields import RichTextField


# Create your models here.


class Slider_Index(models.Model) : 
    picture = models.FileField(verbose_name="عکس " , upload_to="Image_slider/") 
    sentence = models.CharField(verbose_name="جمله" , max_length= 300 )


    def __str__(self) : 
        return self.sentence  
    
    class Meta : 
        db_table = "Slider_Index"
        verbose_name_plural = "عکس های اسلایدر "





class project(models.Model):

    type_project_selection = (
        ('filter-design'  , 'طراحی') , 
        ('filter-repairs' , 'تعمیرات' ) , 
        ('filter-construction' , 'ساخت ' ) , 
        ('filter-remodeling' , 'بازسازی' ) , 
        

    )
    pic1 = models.FileField(verbose_name="عکس سر تیتر 1 " , upload_to="Images_project/")
    pic2 = models.FileField(verbose_name="عکس سر تیتر 2 " , upload_to="Images_project/")
    pic3 = models.FileField(verbose_name="عکس سر تیتر 3 " , upload_to="Images_project/")

    title = models.CharField(verbose_name="نام پروژه" , max_length= 100 )
    customer = models.CharField(verbose_name="مشتری" , max_length= 100 )
    date = models.DateField(verbose_name="تاریخ" , auto_now= False , auto_now_add=True ) 
    body = models.TextField(verbose_name="متن ")
    slug = models.SlugField(verbose_name="آدرس اینترنتی " )
    type_project = models.CharField(verbose_name="نوع پروژه" , max_length=20 , choices= type_project_selection )
    category = models.ForeignKey('Category' , verbose_name="دسته بندی " , related_name="project"  , on_delete=models.CASCADE )
    author = models.ForeignKey(client_register ,verbose_name="نویسنده" , null = True  , on_delete=models.CASCADE )
    message_creator = models.TextField(verbose_name=" متن نویسنده " , null= True )


    class Meta : 
        db_table = "project"
        verbose_name_plural = "پروژه های شرکت "




    def __str__(self) : 
        return self.title 
    

class Category(models.Model) : 
    title = models.CharField(verbose_name="نام دسته بندی " , max_length=100  )
    slug  = models.CharField(verbose_name=" آدرس اینترنتی  " , max_length=100  )
    published_at = models.DateTimeField(verbose_name="زمان انتشار" , auto_now=False , auto_now_add= True )


    def __str__(self) : 
        return self.title 
    
    class Meta : 
        db_table = "Category"
        verbose_name_plural = "دسته بندی ها "




class Send_Data_Quote(models.Model) : 
    name = models.CharField(verbose_name="نام" , max_length=100 ) 
    email = models.EmailField(verbose_name="ایمیل" )
    phone = models.CharField(verbose_name="تلفن"  , max_length= 12 )
    message = models.TextField(verbose_name="متن"  )


    class Meta : 
        db_table = "Send_Data_Quote"
        verbose_name_plural = "ارسال نظر " 

    def __str__(self) : 
        return self.name 
    
    
class Testimonials(models.Model) : 
    author = models.ForeignKey(client_register    , null = True , verbose_name="نام نویسنده" , on_delete=models.CASCADE ) 
    sentence = models.TextField(verbose_name="جمله " , null  =True )


    class Meta : 
        db_table = "Testimonials" 
        verbose_name_plural = "جملات برای نظر در مورد سایت "


    def __str__(self  ) : 
        return f'{self.author}'  


    

class Services(models.Model) :

    TYPE_SERVICES_CATEGORY = (
        ('طراحی'  , 'طراحی') , 
        ( 'تعمیرات', 'تعمیرات' ) , 
        ('ساخت ' , 'ساخت ' ) , 
        ( 'بازسازی', 'بازسازی' ) , 
    )

    picture = models.FileField(verbose_name="تصویر " , upload_to="Images_Service/" )  
    title = models.CharField(verbose_name="عنوان خدمت" , max_length= 100 )
    text = RichTextField(verbose_name = "متن اصلی" )
    text_slide = models.TextField(verbose_name="متن کناری"  )
    type_service = models.CharField(verbose_name="دسته خدمت" , max_length= 100 , choices= TYPE_SERVICES_CATEGORY )



    def __str__(self) : 
        return self.title 
    
    class Meta : 
        db_table = "Services"
        verbose_name_plural = "خدمات شرکت"




class ADDRESS(models.Model) : 
    address = models.CharField(verbose_name="آدرس ما " , max_length= 200 )
    email = models.EmailField(verbose_name="آدرس ایمیل ما") 
    phone1 = models.CharField(verbose_name="1تلفن ما " , max_length= 13 , null = True  )
    phone2 = models.CharField(verbose_name="2تلفن ما " , max_length= 13  , null = True )


    class Meta : 
        db_table = "ADDRESS"
        verbose_name_plural = "آدرس ما "



class contact_us(models.Model) : 
    name = models.CharField(verbose_name="نام و نام خانوادگی" , max_length= 200 )
    email = models.EmailField(verbose_name="ایمیل" )
    subject = models.CharField(verbose_name="موضوع" , max_length= 100  )
    message = models.TextField(verbose_name="پیام"   )


    class Meta : 
        db_table = "contact_us"
        verbose_name_plural = "پیام های ارسال شده از طریق فرم ارتباط با ما"

