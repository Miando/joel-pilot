import scrapy
from scrapy_djangoitem import DjangoItem

import os

from joelsite import settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'joelsite.settings'
import django
django.setup()

from craigs.models import AdditionalOptions


class PersonItem(DjangoItem):
    # fields for this item are automatically created from the django model
    django_model = AdditionalOptions


class MySpider(scrapy.Spider):
    name = "options"
    start_urls = ['https://dallas.craigslist.org/']
    custom_settings = {
        'DOWNLOAD_DELAY': 1
    }
    unique = []

    def parse(self, response):
        for div in response.xpath('//div[@id="center"]/div/div[not(contains(@id, "forums"))]'):
            category = div.xpath('./h4/a/span/text()').extract_first()
            if not category:
                category = div.xpath('./h4/text()').extract_first()
            subcat='all'
            try:
                link = div.xpath('./h4/a/@href').extract_first()
                yield scrapy.Request(
                    url='https://dallas.craigslist.org' + link,
                    meta={
                        'subcat': subcat

                    },
                    callback=self.parse_item
                )
            except:
                pass
            for url in div.xpath('./div/ul/li/a'):
                link = url.xpath('./@href').extract_first()
                subcat = url.xpath('./span/text()').extract_first()\
                    .replace('  /  ', '-').replace(' / ', '-').replace('/', '-') \
                    .replace('[', '').replace(']', '')
                yield scrapy.Request(
                    url='https://dallas.craigslist.org' + link,
                    meta={
                        'subcat': subcat

                    },
                    callback=self.parse_item
                )

    def parse_item(self, response):
        items = {}
        options = response.xpath('//div[@class="search-options"]//label/input[@type="checkbox" and not(contains(@class, "use-id nearbyArea"))]')
        for option in options:
            try:
                name = option.xpath('./@name').extract_first()
                value = option.xpath('./@value').extract_first()
                subcategory = response.meta['subcat'].strip()
                o=name + '=' + value
                option_for_frontend = option.xpath('./../text()').extract_first().strip()
                if option_for_frontend == '':
                    option_for_frontend = "".join(x.strip() for x in option.xpath('./../text()').extract())
                print (subcategory, o, option_for_frontend)

                if [subcategory, o, option_for_frontend] not in self.unique:
                    # s = AdditionalOptions(
                    #     subcategory=subcategory,
                    #     option=o,
                    #     option_for_frontend=option_for_frontend.replace('  /  ', '-').replace(' / ', '-').replace('/', '-') \
                    #     .replace('[', '').replace(']', '').replace("'", '').strip()
                    # )
                    # s.save()
                    items["subcategory"] = subcategory
                    items["option"] = o
                    items["option_for_frontend"] = option_for_frontend.replace('  /  ', '-').replace(' / ', '-').replace('/', '-') \
                        .replace('[', '').replace(']', '').replace("'", '').strip()

                    self.unique.append([subcategory, o, option_for_frontend])
                    yield items
            except:
                print ('========================')
                print (name, value)