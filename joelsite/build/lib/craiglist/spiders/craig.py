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
        # self.category = kwargs.get('category', '')
        self.start_urls.append(kwargs.get('url_task1', ''))

    def gstart_requests(self):
        print (self.url_task1)

        url = self.url_task1
        # url = "https://dallas.craigslist.org/search/jjj?query=food"
        yield scrapy.Request(
            url=url,
            dont_filter=False,
            callback=self.parse_item
        )


    def parse(self, response):
        print (response.url)
        # i = PersonItem.django_model.objects.get(job_name="rent")
        # print("================")
        item = {}
        # i.city = "dallas"
        # i.save()
        # i = PersonItem.django_model.objects.get(job_name="rent")
        # #p = PersonItem()
        # #item["title"] = response.xpath('//*[@id="titletextonly"]/text()').extract_first()
        # #try:
        # #    item["text"] = remove_tags(response.xpath('//*[@id="postingbody"]').extract_first()).replace('QR Code Link to This Post','').strip()
        # #except:
        # #    pass
        item["link"] = response.xpath('//a[@class="result-title hdrlnk"]/text()').extract_first()
        yield item
