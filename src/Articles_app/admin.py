from django.contrib import admin
from .models import Articles_model,Category,Comments
# Register your models here.
admin.site.register(Articles_model)
admin.site.register(Category)
admin.site.register(Comments)