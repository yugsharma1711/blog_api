from django.db import models
from django_random_id_model import RandomIDModel
from django.conf import settings
from django.utils import timezone
from django.utils.translation  import gettext_lazy as _

def upload_to(instance, filename):
    return 'posts/{filename}'.format(filename = filename)
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Post(RandomIDModel):
    options = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default = 1)
    title = models.CharField(max_length=250)
    image = models.ImageField(_("Image"), upload_to= upload_to, default= 'posts/default.jpg')
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=options, default='published')
    objects = models.Manager()
    class Meta:
        ordering = ('-published', )
    def __str__(self):
        return self.title