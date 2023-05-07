from django import forms
from django.core.exceptions import ValidationError
from blog.models import Post

class PostForm(forms.Form):
    title = forms.CharField(required=True, max_length=50)
    body = forms.CharField(required=True, widget=forms.Textarea)

    # this is custom validation. this is a hook, will call after clean function standard from django run for extended validation
    # must prefixed with clean_ function name
    def clean_title(self):
        title = self.cleaned_data.get('title')

        if Post.objects.filter(title=title).exists() :
            raise forms.ValidationError('Title already exists.')

        return title


# def email_not_admin(value):
#         print(value)

#         # email = self.cleaned_data.get('email')
#         email = value
#         if email=='admin@gmail.com' :
#             print('in exception')
#             raise ValidationError('email cannot be admin')

# this is another way to generate form by model, class Meta
class PostModelForm(forms.ModelForm):
    def email_not_admin(value):
        print(value)

        # email = self.cleaned_data.get('email')
        email = value
        # here running well but validation error not raised, not yet why it is
        if email=='admin@gmail.com' :
            print('in exception')
            raise ValidationError('email cannot be admin')

        return email

    email = forms.EmailField(
        validators=[
            email_not_admin
        ]
    )

    class Meta:
        model = Post
        fields = [
            'title',
            'body',
            'email',
        ]

        # fields = '__all__'



