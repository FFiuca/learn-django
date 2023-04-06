from django import forms
from django.core.exceptions import ValidationError
from blog.models import Post

class PostForm(forms.Form):
    title = forms.CharField(required=True, max_length=50)
    body = forms.CharField(required=True, widget=forms.Textarea)

    # this is custom validation. this is a hook, will call after clean function standard from django run for extended validation
    def clean_title(self):
        title = self.cleaned_data.get('title')

        if Post.objects.filter(title=title).exists() :
            raise forms.ValidationError('Title already exists.')

        return title

# this is another way to generate form by model, class Meta
class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'body',
            'email',
        ]

