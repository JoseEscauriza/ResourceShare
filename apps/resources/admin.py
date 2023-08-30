from django.contrib import admin
from apps.resources import models
# Register your models here.


class CustomResources(admin.ModelAdmin):
    list_display = (
        'title',
        'link',
        'description',
        'user_title'
    )


admin.site.register(models.Tag)
admin.site.register(models.Category)
admin.site.register(models.Resources, CustomResources)
admin.site.register(models.Review)
admin.site.register(models.Rating)
