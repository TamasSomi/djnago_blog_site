from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin


# it will register both post model and the post admin class with our admin site
@admin.register(Post) 
class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('content')


