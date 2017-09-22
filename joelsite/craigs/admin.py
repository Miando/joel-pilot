from django.contrib import admin
from .models import Options, CityOptions, ScrapedInfo, CategoryOptions, SubCategoryOptions, AdditionalOptions, PersonOptions
# Register your models here.


admin.site.register(CityOptions)
admin.site.register(ScrapedInfo)
admin.site.register(Options)
admin.site.register(CategoryOptions)
admin.site.register(SubCategoryOptions)
admin.site.register(AdditionalOptions)
admin.site.register(PersonOptions)