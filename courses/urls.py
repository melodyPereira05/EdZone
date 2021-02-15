from django.urls import path
from  . import views

app_name='course'
urlpatterns = [
    
    
   path('', views.home , name="home-page"),
    path('about/',views.about, name="about-page"),
    path('contact-us/',views.contact_us,name="contact-us"), 
    path('contact/<int:id>',views.contact_submit,name='contact'),
    #path(minecourse);    
    #path('contact/',views.contact_submit,name="contact-submit"),
    path('wishlist/',views.wishlist_submit,name="wishlist-submit"),    
    path('create/', views.coursecreate,name='create-course'),
    path('<int:id>/', views.coursedetail, name='retrive-course'),
    path('<int:id>/edit/', views.courseupdate,name='update-course'),
    path('<int:id>/delete/', views.coursedelete,name='delete-course'),
    #path('<int:instructor>/',views.instructor_page,name="instructor-page"),
    path('<int:course_id>/<slug:slug>/',views.wishlist_submit, name="single-course"),
    
    
    
]