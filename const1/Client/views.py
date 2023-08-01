from django.shortcuts import render
from .models import client_register , History_website 
from Total_project.models import project 

# Create your views here.

def team_introduction(request) : 

    team = client_register.objects.all()
    history = History_website.objects.first() 
    len_projects = len(project.objects.all())
    content = {
        'info':team , 
        'len_project' : len_projects ,
        'len_project_client' : len_projects  *15 , 
        'len_project_support':len_projects  * 175 ,  
        'len_info' : len(team) , 
        'hinfo' : history , 
    }

    return render(request , 'about.html' , content )



