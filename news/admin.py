from django.contrib import admin # type: ignore
from .models import Articles


admin.site.register(Articles)