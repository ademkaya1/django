from django.conf import settings
from django.db import models

# Create your models here.
from django.template.defaultfilters import slugify


class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    publishing_date = models.DateTimeField(auto_now_add=True)  # auto now add otomatik kendisi eklemesi için
    image = models.ImageField(blank=True, null=True, upload_to='uploads/')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)                      # djangoda user modeli zaten mevcut
    slug = models.SlugField(default="slug")    # burada url adresimizi içeriğin kendi adıyla oluşturmak için kullandık


    def __str__(self):
        return self.title   #admin panelinde title gösterecek



    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)