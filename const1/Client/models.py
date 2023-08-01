from django.db import models
from django.contrib.auth.models import User 
from ckeditor.fields import RichTextField
from django.utils import timezone 



# Create your models here.


class client_register(models.Model) : 
    position_level = (
        ('مدیر فنی' , 'مدیر فنی' )  , 
        ('کارمند' , 'کارمند') , 
        ( 'مدیر اجرایی', 'مدیر اجرایی')
    )
    user = models.ForeignKey(User , on_delete=models.CASCADE , verbose_name="کاربر" ) 
    picture = models.FileField(verbose_name="عکس" , upload_to = "Image/Client" ) 
    position = models.CharField(verbose_name="سمت " , null = True   , choices=position_level , max_length= 100 ) 
    instagram = models.CharField(verbose_name="لینک اینستاگرام", blank = True , null = True , max_length= 100 )
    faceboob = models.CharField(verbose_name="لینک فیسبوک" , blank = True , null = True , max_length= 100 )
    twitter = models.CharField(verbose_name="لینک توئیتر" , blank = True , null = True , max_length= 100  )
    fields = models.CharField(verbose_name="زمینه تخصصی" , max_length=100 , null = True )
    linkedin = models.CharField(verbose_name="لینک توئیتر" , blank = True , null = True , max_length= 100  )
    about_user = models.CharField(verbose_name="درباره عضو" , max_length= 300 , null = True )
    def __str__(self) : 
        return f'{self.user}' 
    

    class Meta : 
        db_table = "client_register"
        verbose_name_plural = "ثبت نام کاربران "





class History_website(models.Model) : 
    title = models.CharField(verbose_name="عنوان" , max_length= 100 , null = True )
    data = RichTextField(verbose_name = "اطلاعات تاریخچه" )
    time = models.DateTimeField(verbose_name="زمان شکل گیری" , default=timezone.now )
    picture = models.FileField(verbose_name="عکس" , upload_to = "Image_History/" ) 
    class Meta : 
        db_table = "History_website"
        verbose_name_plural = "تاریخچه وبسایت و شرکت"



    def __str__(self) : 
        return self.title 
    
