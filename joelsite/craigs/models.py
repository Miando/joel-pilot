from django.db import models
from django.contrib.auth.models import Permission, User
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
    options = models.CharField(max_length=1000, blank=True)
    keyword = models.CharField(max_length=250, blank=True)
    stop_word = models.CharField(max_length=250, blank=True)
    time_update = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.job_name


class CityOptions(models.Model):
    city = models.CharField(max_length=250, unique=True)
    city_for_frontend = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.city_for_frontend


class Options(models.Model):
    category = models.CharField(max_length=250)
    front_category = models.CharField(max_length=250, blank=True)
    subcategory = models.CharField(max_length=250)
    front_subcategory = models.CharField(max_length=250, blank=True)
    option1 = models.CharField(max_length=250, blank=True)
    option2 = models.CharField(max_length=250, blank=True)
    option3 = models.CharField(max_length=250, blank=True)
    option4 = models.CharField(max_length=250, blank=True)
    option5 = models.CharField(max_length=250, blank=True)
    option6 = models.CharField(max_length=250, blank=True)
    option7 = models.CharField(max_length=250, blank=True)
    option8 = models.CharField(max_length=250, blank=True)
    option9 = models.CharField(max_length=250, blank=True)
    option10 = models.CharField(max_length=250, blank=True)
    option11 = models.CharField(max_length=250, blank=True)
    option12 = models.CharField(max_length=250, blank=True)
    option13 = models.CharField(max_length=250, blank=True)
    option14 = models.CharField(max_length=250, blank=True)
    option15 = models.CharField(max_length=250, blank=True)
    front_option1 = models.CharField(max_length=250, blank=True)
    front_option2 = models.CharField(max_length=250, blank=True)
    front_option3 = models.CharField(max_length=250, blank=True)
    front_option4 = models.CharField(max_length=250, blank=True)
    front_option5 = models.CharField(max_length=250, blank=True)
    front_option6 = models.CharField(max_length=250, blank=True)
    front_option7 = models.CharField(max_length=250, blank=True)
    front_option8 = models.CharField(max_length=250, blank=True)
    front_option9 = models.CharField(max_length=250, blank=True)
    front_option10 = models.CharField(max_length=250, blank=True)
    front_option11 = models.CharField(max_length=250, blank=True)
    front_option12 = models.CharField(max_length=250, blank=True)
    front_option13 = models.CharField(max_length=250, blank=True)
    front_option14 = models.CharField(max_length=250, blank=True)
    front_option15 = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.front_subcategory


class CategoryOptions(models.Model):
    category = models.CharField(max_length=250)
    category_for_frontend = models.CharField(max_length=250)

    def __str__(self):
        return self.category_for_frontend


class SubCategoryOptions(models.Model):
    category = models.CharField(default='', max_length=250)  #ForeignKey(CategoryOptions, on_delete=models.CASCADE)
    subcategory = models.CharField(default='', max_length=250)
    subcategory_for_frontend = models.CharField(max_length=250)

    def __str__(self):
        return self.subcategory_for_frontend


class AdditionalOptions(models.Model):
    subcategory = models.CharField(default='', max_length=250)#models.ForeignKey(SubCategoryOptions, on_delete=models.CASCADE)
    option = models.CharField(default='', max_length=250)
    option_for_frontend = models.CharField(default='all', max_length=250)

    def __str__(self):
        return self.option_for_frontend
