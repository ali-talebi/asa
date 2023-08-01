from django import forms 
from .models import Send_Data_Quote 


class Send_Data(forms.Form) : 
    class Meta : 
        model = Send_Data_Quote 
        fields = "__all__"


class contact_us_form(forms.Form) : 
    name = forms.CharField(max_length= 200 )
    email = forms.SlugField()
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea) 

    







