from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class ScrapedInfo(models.Model):
    user = models.ForeignKey(User, default=1)
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class PersonOptions(models.Model):
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, default=1)
    job_name = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    category = models.CharField(max_length=250)
    subcategory = models.CharField(max_length=250)
    options = models.CharField(max_length=1000)
    keyword = models.CharField(max_length=250)
    stop_word = models.CharField(max_length=250, blank=True)
    time_update = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.job_name


class CityOptions(models.Model):
    city = models.CharField(max_length=250)
    city_for_frontend = models.CharField(max_length=250)

    def __str__(self):
        return self.city_for_frontend


class CategoryOptions(models.Model):
    category = models.CharField(max_length=250)
    category_for_frontend = models.CharField(max_length=250)

    def __str__(self):
        return self.category_for_frontend


class SubCategoryOptions(models.Model):
    category = models.ForeignKey(CategoryOptions, on_delete=models.CASCADE)
    subcategory = models.CharField(default='', max_length=250)
    subcategory_for_frontend = models.CharField(default='all', max_length=250)

    def __str__(self):
        return self.subcategory_for_frontend


class AdditionalOptions(models.Model):
    subcategory = models.ForeignKey(SubCategoryOptions, on_delete=models.CASCADE)
    option = models.CharField(default='', max_length=250)
    option_for_frontend = models.CharField(default='all', max_length=250)

    def __str__(self):
        return self.option_for_frontend
