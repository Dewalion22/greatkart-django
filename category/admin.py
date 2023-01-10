from django.contrib import admin

# Register your models here.

from .models import Category

# register your model
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('category_name',)}
    list_display = ('category_name', 'slug',)



admin.site.register(Category, CategoryAdmin)