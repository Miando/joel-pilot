import scrapy
from w3lib.html import remove_tags
from scrapy_djangoitem import DjangoItem
from scrapy.item import Field

import os
import sys

from joelsite import settings
#sys.path.append('/home/miando/upwork/joel/joelsite/joelsite')
os.environ['DJANGO_SETTINGS_MODULE'] = 'joelsite.settings'
import django
django.setup()

from craigs.models import PersonOptions


class PersonItem(DjangoItem):
    # fields for this item are automatically created from the django model
    django_model = PersonOptions

class MySpider(scrapy.Spider):
    name = "craigs1"
    allowed_domains = ["craigslist.org"]

    def __init__(self,  **kwargs):
        super(MySpider, self).__init__(self, **kwargs)
        self.category = kwargs.get('category', '')

    def start_requests(self):
        subcategory = self.subcategory
        if subcategory == "all":
            subcategory = self.category
        url = "https://{city}.craigslist.org/search/{subcategory}?query={keymord}".format(
            city=self.city,
            subcategory=subcategory,
            keymord=self.keyword
        )
        # url = "https://dallas.craigslist.org/search/jjj?query=food"
        yield scrapy.Request(
            url=url,
            callback=self.parse_item
        )


    def parse_item(self, response):
        i = PersonItem.django_model.objects.get(job_name="rent")
        print("================")
        item = {}
        i.city = "dallas"
        i.save()
        i = PersonItem.django_model.objects.get(job_name="rent")
        #p = PersonItem()
        #item["title"] = response.xpath('//*[@id="titletextonly"]/text()').extract_first()
        #try:
        #    item["text"] = remove_tags(response.xpath('//*[@id="postingbody"]').extract_first()).replace('QR Code Link to This Post','').strip()
        #except:
        #    pass
        item["link"] = i.city
        return item
