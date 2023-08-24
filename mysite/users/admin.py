from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    # ProfileAdmin의 내용을 정의하거나 수정할 수 있습니다.
    pass

# Profile 모델을 등록
admin.site.register(Profile, ProfileAdmin)
