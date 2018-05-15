from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from . import models
# Register your models here.


admin.site.register(models.Party, MarkdownxModelAdmin)
admin.site.register(models.Places, MarkdownxModelAdmin)