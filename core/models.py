from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=1)
    created_at = models.DateTimeField(
        verbose_name='Дата и время создания заказа',
        auto_now_add=True,

    )
    photo = models.ImageField(
        verbose_name="фото",
        upload_to='photos',
        null=True,
        blank=True
    )