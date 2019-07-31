from .models import Post
from django import forms

# Forms

class PostForm(forms.ModelForm):
    """Form definition for Post."""

    class Meta:
        """Meta definition for Postform."""

        model = Post
        fields = ('profile', 'title', 'photo')
