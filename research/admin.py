from django.contrib import admin
import models

class ImageInline(admin.StackedInline):
    readonly_fields = ('markdown_tag',)
    model = models.Image
    extra = 3

@admin.register(models.Field)
class FieldAdmin(admin.ModelAdmin):
    exclude = ('slug',)

# Register your models here.
@admin.register(models.Group)
class GroupAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    exclude = ('slug',)