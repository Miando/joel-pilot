import scrapy
from scrapy_djangoitem import DjangoItem

import os

from joelsite import settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'joelsite.settings'
import django
django.setup()

from craigs.models import CityOptions


class PersonItem(DjangoItem):
    # fields for this item are automatically created from the django model
    django_model = CityOptions


class MySpider(scrapy.Spider):
    name = "get_cities"
    start_urls = ['https://www.craigslist.org/about/sites']
    custom_settings = {
        'DOWNLOAD_DELAY': 1
    }
    unique = []

    def parse(self, response):
        for i, div in enumerate(response.xpath('//section/div[@class="colmask"][1]//li/a')):
            city = div.xpath('./text()').extract_first()
            city_for_frontend = div.xpath('./@href').extract_first()
            s = CityOptions(
                city=city,
                city_for_frontend=city_for_frontend,
               )
            s.save()
            print (i)

