from django.urls import path
from  . import views

app_name='course'
urlpatterns = [
    
    
   path('', views.home , name="home-page"),
    path('about/',views.about, name="about-page"),
    path('contact-us/',views.contact_us,name="contact-us")   
    path('contact/',views.contact_submit,name="contact-submit"),
    path('wishlist/',views.wishlist_submit,name="wishlist-submit"),
    
    
    
    
]