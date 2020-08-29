from django.contrib import admin
from .models import Articles_model,Category
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'creade_date')
    list_filter = ("status", )
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(Articles_model, PostAdmin)
admin.site.register(Category)