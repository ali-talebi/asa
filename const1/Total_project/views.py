from django.shortcuts import render
from .models import   contact_us , ADDRESS , Services , project , Slider_Index , Send_Data_Quote , Testimonials 
from .forms import Send_Data , contact_us_form 
from blog.models import Blogs , comments , dasteh_bandy_model 
from blog.forms import Comments_Form


# Create your views here.




def contact_us_view(request) : 

    

    if request.method == "POST" : 
        form  = contact_us_form(request.POST)

        if form.is_valid() : 
            new_name = form.cleaned_data["name"]
            new_email = form.cleaned_data["email"]
            new_subject = form.cleaned_data["subject"]
            new_message = form.cleaned_data["message"]

            g = contact_us( name = new_name , email = new_email , subject = new_subject , message = new_message  )
            g.save()

            






    content = {
        'info' : ADDRESS.objects.first() , 
    }
    return render(request , 'contact.html' , content )



def detail_Services(request , id ) : 
    now_service = Services.objects.get( id = id )
    total_services =  Services.objects.all()
    context = {
        'info' : now_service , 
        'info_total_sercies' : total_services , 
    }

    
    return render(request , 'service-details.html' , context )







def Home(request) : 

    if request.method == "POST" : 
        forms_quote = Send_Data(request.POST) 

        if forms_quote.is_valid()  :
            pass 
            #forms_quote.save() 





    data = project.objects.all() 
    pictures = Slider_Index.objects.all()
    testimonials = Testimonials.objects.all()  
    services_total = Services.objects.all()
    
    content = {
        'info_project' :data , 
        'info_pictures' : pictures , 
        'testimonials' : testimonials , 
        'recent_blogs' : Blogs.objects.all().order_by("-time") , 
        'services_total':services_total , 
    }

    return render(request  , 'index.html' , content )

def detail_project(request , id ) : 
    data = project.objects.get(id = id )
    content = {
        'info' : data 
    }
    return render(request , 'project-details.html' , content )


def detail_blog(request , id ) : 
    recent_post = Blogs.objects.all().order_by("-time")
    post_now = Blogs.objects.get(id = id )
    

    if request.method == "POST" : 
        form_comment = Comments_Form(request.POST)
        if form_comment.is_valid() : 
            new_name = form_comment.cleaned_data["name"]
            new_email = form_comment.cleaned_data["email"]
            new_website = form_comment.cleaned_data["website"]
            new_message = form_comment.cleaned_data["comment"]

            new_comment = comments(blog = post_now , name = new_name , email = new_email , website = new_website , message= new_message )
            new_comment.save()


    data_comments = comments.objects.all().filter(blog = post_now )
    content = {
        'info' : post_now  , 
        'recent':recent_post , 
        'comments' : data_comments , 
        'total_category':dasteh_bandy_model.objects.all() ,
    }
    return render(request , 'blog-details.html' , content )


def search_form(request  ) : 
    if request.method == "GET" : 
        q = request.GET.get("text") 

    
    blog_searched = Blogs.objects.filter( title__icontains = q )
    return render(request , 'search.html' , {'info' : blog_searched  } )


def blog_filter_tag(request, tag ) : 
    data = Blogs.objects.filter(tags__slug = tag )
    return render(request , 'test1.html' , {'info':data , 'tag':tag } )

def blog_filter_category(request , category  ) : 
    data = Blogs.objects.filter(dasteh_bandy_model__slug = category )
    single = data[0].category 
    return render(request , 'test2.html' , {'info' : data , 'category' : single })
    


def message_save_successfully(request) : 
    return render(request , 'successfully_register_idea.html' , {})