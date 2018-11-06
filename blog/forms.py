from django import forms
from .models import Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25, widget=forms.TextInput(
        attrs={
            'class': 'input',
            'placeholder': 'enter name'
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'blog-input',
            'placeholder': 'enter email'
        }))
    to = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'blog-input',
            'placeholder': 'enter email',
        }
    ))
    comments = forms.CharField(required=False, widget=forms.Textarea(
        attrs={
            'class': 'textarea',
            'placeholder': 'Share your comments'
        }
    ))


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class SearchForm(forms.Form):
    query = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'enter search term'
        }
    ))


