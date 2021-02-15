from django.contrib import admin
from .models import Subject, Course, Module,Wishlist,Contact


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}
    


    
    
class ModuleInline(admin.StackedInline):
    model = Module
 
    

    
    
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'created']
    list_filter = ['created', 'subject']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ModuleInline]

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ['course', 'name', 'wishlisted_date']
    list_filter = ['course', 'name']    
    prepopulated_fields = {'slug': ('course',)}
  
@admin.register(Contact)

class ContactAdmin(admin.ModelAdmin):
    list_display = ['course', 'name', 'email']
    list_filter = ['email', 'name']    
    prepopulated_fields = {'slug': ('course',)}  
