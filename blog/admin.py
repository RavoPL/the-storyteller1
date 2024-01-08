from django.contrib import admin
from .models import Post, Comment, Submission
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    # Automatically populates the slug field with the value in the title field
    prepopulated_fields = {'slug': ('title',)}
    # Allows the admin to filter through dates of post creation
    list_filter = ('status', 'created_on')
    # Displays the title, slug, status and date of creation of a post
    list_display = ('title', 'slug', 'status', 'created_on')
    # Allows the admin to search for posts by title or content
    search_fields = ['title', 'content']
    # Enables Summernote features in the content section
    summernote_fields = ('content')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # Allows the admin to filter through dates and approval status of comment creation
    list_filter = ('approved', 'created_on')
    # Displays the user name, body of comment, date of creation and approval status
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    # Allows the admin to search for comments by name, user e-mail or body of comment
    search_fields = ['name', 'email', 'body']
    # Allows the admin to approve and reject comments
    actions = ['approve_comments']
    # Changes the approval status of a comment from False to True
    def approve_comments(self, request, queryset):
        queryset.update(approved=True)

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    # Allows the admin to filter through the author's name and titles of short story submissions
    list_filter = ('name', 'title')
    # Displays the name of the author, title of the submission and the body of the text
    list_display = ('name', 'title', 'body')
    # Allows the admin to search for short stories by name of author and their title
    search_fields = ['name', 'title']