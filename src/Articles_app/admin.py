from django.contrib import admin
from .models import Articles_model,Category,Comments,Comments_comment
# Register your models here.
admin.site.register(Articles_model)
admin.site.register(Category)
admin.site.register(Comments)
admin.site.register(Comments_comment)