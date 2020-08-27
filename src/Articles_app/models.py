from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from _datetime import timezone
from django.utils.timezone import now
from ckeditor.fields import RichTextField





'''
METHODS
'''
# JOB_TYPE = (
#     ('Full Time','Full Time'),
#     ('Part Time','Part Time'),
# )
CATEGORY_TYPE = (
    ('PERSONAL ACTIVITIES', 'PERSONAL ACTIVITIES'),
    ('PROJECTS', 'PROJECTS'),
    ('vvs', 'المشاريع '),
    ('BLOG', 'BLOG'),
    ('EDUCATION', 'EDUCATION'),
)

def image_upload(instance,filename):
    imagename , extension = filename.split(".")
    return "articles/%s.%s"%(instance.id,extension)

'''
MODELS

'''
# Create your models here.
class Articles_model(models.Model):
    title = models.CharField(max_length = 50)
    intro=models.CharField(max_length = 60)
    main=models.CharField(max_length = 60)
    text=RichTextField()
    creade_date = models.DateField(auto_now=True,
                                   blank=True,
                                   auto_now_add=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    article_type=models.CharField(max_length = 150,choices=CATEGORY_TYPE)
    published_date = models.DateField()

    slug = models.SlugField(blank=True, null=True)

    image=models.ImageField(upload_to=image_upload)
    # files=
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.published_date = now()
        super(Articles_model, self).save(*args, **kwargs)

    def __str__(self):
        return self.title





class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name