<<<<<<< HEAD
from django.forms import ModelForm
# API
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout


class MyForm(forms.Form):
    # 폼 필드들 정의
    # ...

    helper = FormHelper()
    helper.layout = Layout(
        # 폼 레이아웃을 정의하거나 crispy_forms 템플릿 태그를 사용
        # ...
    )
=======
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','content']
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'content' : forms.Textarea(attrs={'class' : 'col-sm-12'})
        }
>>>>>>> f94a81f13bd7c43718db3fa3f21787a8696e46f5
