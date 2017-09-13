from django.contrib import admin
from .models import CityOptions, CategoryOptions, SubCategoryOptions, AdditionalOptions, PersonOptions
# Register your models here.


admin.site.register(CityOptions)
admin.site.register(CategoryOptions)
admin.site.register(SubCategoryOptions)
admin.site.register(AdditionalOptions)
admin.site.register(PersonOptions)