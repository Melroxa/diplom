from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.validators import FileExtensionValidator
from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(verbose_name='Название', max_length=100)
    slug = models.SlugField(verbose_name='URL', db_index=True, unique=True, null=True, blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория цен'
        verbose_name_plural = 'Категории цен'

    def __str__(self):
        return self.name


class Service(models.Model):
    category = models.ForeignKey(Category, related_name='prices',
                                 verbose_name='Категория',
                                 on_delete=models.CASCADE)
    title = models.CharField(max_length=200, db_index=True,
                             verbose_name='Название')
    description = models.TextField(blank=True, verbose_name="Описание")

    min_price = models.DecimalField(max_digits=10, decimal_places=2,
                                    verbose_name="Минимальная цена", null=True, blank=True)
    max_price = models.DecimalField(max_digits=10, decimal_places=2,
                                    verbose_name="Максимальная цена", null=True, blank=True)

    available = models.BooleanField(default=True,
                                    verbose_name="Действующая услуга")

    class Meta:
        ordering = ('title',)
        index_together = (('id',),)
        verbose_name = 'Цена на услугу'
        verbose_name_plural = 'Цены на услуги'

    def __str__(self):
        return self.title

@receiver(pre_save, sender=Category)
def set_category_slug(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)



class CategoryMaster(models.Model):
    name = models.CharField(verbose_name='Имя мастера', max_length=100)
    slug = models.SlugField(verbose_name='URL', db_index=True, null=True)
    image = models.ImageField(verbose_name="Фото мастера",
                              blank=True,
                              default='images/thumbnails/unnamed.jpg',
                              upload_to='images/cat_lookbook/%Y/%m/%d',
                              validators=[FileExtensionValidator(
                                  allowed_extensions=(
                                      'png', 'jpg', 'webp', 'jpeg', 'gif'))]
                              )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория мастера'
        verbose_name_plural = 'Категории мастеров'

    def __str__(self):
        return self.name



class Master(models.Model):
    category = models.ForeignKey(CategoryMaster, related_name='prices',
                                 verbose_name='Категория',
                                 on_delete=models.CASCADE)
    title = models.CharField(max_length=200, db_index=True,
                             verbose_name='ФИО')
    experience = models.CharField(verbose_name='Стаж рааботы', max_length=20)
    description = models.TextField(blank=True, verbose_name="Описание")

    # image = models.ImageField(verbose_name="Фото услуг",
    #                           blank=True,
    #                           default='images/thumbnails/unnamed.jpg',
    #                           upload_to='images/lookbook/%Y/%m/%d',
    #                           validators=[FileExtensionValidator(
    #                               allowed_extensions=(
    #                                   'png', 'jpg', 'webp', 'jpeg', 'gif'))]
    #                           )

    class Meta:
        ordering = ('title',)

        verbose_name = 'Мастер'
        verbose_name_plural = 'Мастера'

    def __str__(self):
        return self.title


class MasterImage(models.Model):
    master = models.ForeignKey(Master, related_name='images',
                               on_delete=models.CASCADE)
    image = models.ImageField(upload_to='master_images/%Y/%m/%d',
                              default='images/thumbnails/unnamed.jpg',
                              validators=[FileExtensionValidator(
                                  allowed_extensions=(
                                      'png', 'jpg', 'webp', 'jpeg', 'gif'))])

    class Meta:
        ordering = ('master',)

        verbose_name = 'Фотография работ мастера'
        verbose_name_plural = 'Фотографии работ мастера'

    def __str__(self):
        return str(self.master)
