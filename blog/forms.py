from .models import Comment, Submission
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ('name', 'title', 'body',)