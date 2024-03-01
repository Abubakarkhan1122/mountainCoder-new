from django.contrib import admin
from blog.models import Blog,Contact
# Register your models here.
admin.site.register(Contact)

class BlogAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all': ('css/main.css',)
        }
        js = ('js/blog.js',)
admin.site.register(Blog,BlogAdmin)