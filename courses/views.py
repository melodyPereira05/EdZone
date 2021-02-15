from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404,redirect
from .models import Course
from django.http import HttpResponse
from math import ceil
from django.contrib.auth.decorators import login_required


# def enrollcourse(request):
#     pass

def home(request):   
    queryset = Course.objects.all()
    context = { 
        "CourseList": queryset, 
        
    }    
    return render(request,'home.html',context)
 
def about(request):
    return render(request,'about.html')

def contact_us(request):
    return render(request,'contact_us.html')

# Create your views here. FBvs (Crud for Courses)
#this implements CRUD functionality on the courses 

# login required and has to be instructor
@login_required(login_url='/accounts/login/')
def coursecreate(request):    
    #form goes here
    if form.is_valid():        
        fm = form.save(commit=False)
        fm.save()
       
        messages.success(request,"course has been created sucessfully!!!")
        return HttpResponseRedirect(fm.get_absolute_url())
    else:
        messages.error(request, "Course has not been created, try again later")
    
    context = {
        "form":form,
    }
    return render(request, "courseform.html", context)

#Show Course Details
@login_required(login_url='/accounts/login/')
def coursedetail(request,id=None):
    fm = get_object_or_404(Course, id=id)
    context ={
        "title": "Course Detail",
        "form": fm,
    }
    return render(request, "coursedetail.html", context) 
  
# login required and has to be instructor
@login_required(login_url='/accounts/login/')
def courseupdate(request,id=None):
    fm =get_object_or_404(Course, id=id)
    if(request.user == fm.instructor): 
        #updated form here
        if form.is_valid():
            fm = form.save(commit=False)
            fm.save()            
            messages.success(request,"course has been updated")
            return HttpResponseRedirect(fm.get_absolute_url())  
        else:        
            messages.error(request, "You cannot update course you have not created.")
          
        return HttpResponseRedirect(fm.get_absolute_url())

    context = {
        "updatedForm":fm,
        "form": form,
    }
    return render(request, "course_form.html",context)
    
    
# login required and has to be instructor who has created the form
@login_required(login_url='/accounts/login/')
def coursedelete(request,id=None):
    
    fm= get_object_or_404(Course, id=id)
    if(request.user == fm.instructor):        
        fm.delete()
        messages.success(request, "Course has been deleted successfully")
    else:
        messages.error(request, "You cannot delete course you have not created.") 
    return redirect("home-page")

#page of individual instructor
# def instructor_page(request,instructor):
     
#     instructor=Instructor.objects.get(id=instructor)
#     courses=Course.objects.all()  
    
    
#     return render(request,'instructor-page.html',{ 'courses':courses,'instructor':instructor } )

def contact_submit(request):
    if request.method =='POST':
        print("Post")
        course_id=request.POST['course_id']
        slug=request.POST['slug']
        course=request.POST.get('course')
        name=request.POST['name']
        email=request.POST.get('email')
        #phone=request.POST.get('phone')
        message=request.POST.get('message')
        user_id=request.POST['user_id']
        #seller_email=request.POST['seller_email']
        print(slug)
        
        if request.user.is_authenticated:
            user_id=request.user.id
            has_contacted=Contact.objects.all().filter(course_id=course_id,user_id=user_id)
            if has_contacted:
                messages.add_message(request, messages.ERROR,'You have already made an enquiry for this course')
                return redirect('/courses/contact/'+course_id)
        
        contact=Contact(course =course,course_id=course_id,name=name,email=email,slug=slug,message=message,user_id=user_id)
        
        contact.save()
        #sending email
        send_mail(
            course,
                message,
                'melzpereira0509@gmail.com',
                [email,'melodypereira05@gmail.com'],#'sukhadamorgaonkar28@gmail.com','chetna.nihalani@yahoo.in'],
        )
        
       
        
        messages.add_message(request, messages.SUCCESS, 'Your query has been submitted,we will get back to you soon')
        
        
        return redirect('dashboard')
        
    return redirect('dashboard')


def wishlist_submit(request):
    if request.method =='POST':
        
        course_id=request.POST['course_id']
        slug=request.POST['slug']
        course=request.POST['course']
        name=request.POST['name']        
        user_id=request.POST['user_id']
        
        if request.user.is_authenticated:
            user_id=request.user.id
            is_wishlisted=Wishlist.objects.all().filter(course_id=course_id,user_id=user_id)
            if is_wishlisted:
                messages.add_message(request, messages.ERROR,'You have already wishlisted this course')
                return redirect('wishlist')
        
        wishlist=Wishlist( course=course,course_id=course_id,name=name,slug=slug,user_id=user_id)
        
        wishlist.save()
       
        return redirect('wishlist')
   
    return redirect('wishlist')

