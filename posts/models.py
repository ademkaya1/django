from PIL import Image
from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify

# Her yeni alan oluşturmada eklemede migration yapılmalıdır

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug =models.SlugField(default="slug")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def post_count(self):
        return self.posts.all().count()


class Post(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    publishing_date = models.DateTimeField(auto_now_add=True)  # auto now add otomatik kendisi eklemesi için
    image = models.ImageField(blank=True, null=True, upload_to='uploads/', default='uploads/bilisimm.jpg')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)                      # djangoda user modeli zaten mevcut
    slug = models.SlugField(default="slug")    # burada url adresimizi içeriğin kendi başlığıyla oluşturmak için kullandık
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1, related_name="posts")         #bir kategorinin bir sürü postu olabilir. (one to many)


    def __str__(self):
        return self.title   #admin panelinde title gösterecek



    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args,**kwargs)

        img =Image.open(self.image.path)
        if img.height > 340 or img.width > 770:
            new_size = (340, 770)
            img.thumbnail(new_size)     # Küçük resim
            img.save(self.image.path)