import scrapy
from scrapy_djangoitem import DjangoItem

import os

from joelsite import settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'joelsite.settings'
import django
django.setup()

from craigs.models import SubCategoryOptions


class PersonItem(DjangoItem):
    # fields for this item are automatically created from the django model
    django_model = SubCategoryOptions

class MySpider(scrapy.Spider):
    name = "subcategories"
    start_urls = ['https://dallas.craigslist.org/']
    custom_settings = {
        'DOWNLOAD_DELAY': 1
    }

    def parse(self, response):
        for div in response.xpath('//div[@id="center"]/div/div[not(contains(@id, "forums"))]'):
            category = div.xpath('./h4/a/span/text()').extract_first()
            if not category:
                category = div.xpath('./h4/text()').extract_first()
            subcat='all'
            try:
                link = div.xpath('./h4/a/@href').extract_first()
                s = SubCategoryOptions(
                            category=category,
                            subcategory=link,
                            subcategory_for_frontend=subcat
                        )
                s.save()
            except:
                pass
            for url in div.xpath('./div/ul/li/a'):
                link = url.xpath('./@href').extract_first()
                subcat = url.xpath('./span/text()').extract_first()\
                    .replace('  /  ', '-').replace(' / ', '-').replace('/', '-') \
                    .replace('[', '').replace(']', '')
                print(category, link, subcat)
                s = SubCategoryOptions(
                    category=category,
                    subcategory=link,
                    subcategory_for_frontend=subcat
                )
                s.save()
