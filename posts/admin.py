from django.contrib import admin
from .models import Posts
# Register your models here.




@admin.register(Posts)   #if used this dont use code at line 14
class PostAdmin(admin.ModelAdmin):
    list_display=["id","post_title","updated_at"]
    list_display_links=['id',"post_title"]
    list_filter=["updated_at"]
    search_fields=["post_title"]
    
admin.site.site_header= "My Blog"
admin.site.index_title = "My Blog Controller"



# admin.site.register(Posts, PostAdmin)  #we can use code at line 7 except this line