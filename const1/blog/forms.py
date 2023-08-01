from django import forms 

class Comments_Form(forms.Form) : 
    name = forms.CharField(max_length=100 ) 
    email = forms.EmailField(max_length=254)
    website = forms.SlugField(max_length=13 )
    comment = forms.CharField(widget=forms.Textarea)
