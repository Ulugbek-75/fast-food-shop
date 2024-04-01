from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Category title'))
    slug = models.SlugField(max_length=255, verbose_name='Category slug',
                            unique=True)
    image = models.ImageField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Food(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='food', null=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    character = models.TextField()
    UZ = "so'm"
    RU = "&"
    ENG = "$"
    the_price = (
        (UZ, "so'm"),
        (RU, "&"),
        (ENG, "$"),
    )
    price_type =models.CharField(max_length=10,
                                 choices=the_price,
                                 default="so'm")
    price = models.IntegerField()
    image = models.ImageField(null=True)

    def __str__(self):
        return self.name





class Contact(models.Model):
    your_name = models.CharField(max_length=255)
    your_email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=255)

    def __str__(self):
        return self.your_name