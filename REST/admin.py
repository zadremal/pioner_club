from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from . import models
# Register your models here.


admin.site.register(models.Party, MarkdownxModelAdmin)
admin.site.register(models.Places, MarkdownxModelAdmin)
admin.site.register(models.Deals, MarkdownxModelAdmin)
admin.site.register(models.MenuCategories)
admin.site.register(models.DishCategories)
admin.site.register(models.Units)
admin.site.register(models.Dish)
@admin.register(models.Leads)
class LeadsAdmin(admin.ModelAdmin):
    readonly_fields = ["name", "phone", "email", "date"]

@admin.register(models.Birthdays)
class LeadsAdmin(admin.ModelAdmin):
    readonly_fields = ["name", "phone", "email"]

@admin.register(models.Bankets)
class LeadsAdmin(admin.ModelAdmin):
    readonly_fields = ["name", "phone", "email"]
