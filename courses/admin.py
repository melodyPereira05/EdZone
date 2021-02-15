from django.contrib import admin
from .models import Subject, Course, Module,Wishlist,Contact,Text,File,Image,Video,Content

#admin.site.register(Instructor)
# admin.site.register(Subject)
# admin.site.register(Course)
# admin.site.register(Module)
# admin.site.register(Wishlist)
# admin.site.register(Contact)
# admin.site.register(Text)
# admin.site.register(File)
# admin.site.register(Image)
# admin.site.register(Video)
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
