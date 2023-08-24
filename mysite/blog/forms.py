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
