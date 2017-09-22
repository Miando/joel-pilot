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
from craigs.models import ScrapedInfo
from django.core.mail import send_mail
from datetime import datetime


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
        self.pk = kwargs.get('pk', '')
        self.job_name = kwargs.get('job_name', '')

    def parse(self, response):
        print(self.start_urls)
        p = PersonOptions.objects.get(pk=self.pk)#PersonItem.django_model.objects.get(pk=self.pk)
        ul = response.xpath('//li[@class="result-row"]')
        # pp = PersonOptions.objects.get(pk=self.pk)
        new = []
        new_time = []
        for li in ul:
            time = li.xpath('.//@datetime').extract_first()
            time = time + ':00'
            time_obj = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')
            if p.time_update.replace(tzinfo=None) < time_obj:
                url = li.xpath('.//a[@class="result-title hdrlnk"]/@href').extract_first()
                title = li.xpath('.//a[@class="result-title hdrlnk"]/text()').extract_first()
                new.append([url, title])
                new_time.append(time_obj)
                p.scrapedinfo_set.create(
                    title=title,
                    url=url
                )
        message = ''
        if new:
            for m in new:
                message = message + '<br>' + '<a href="{}">{}</a>'.format(m[0], m[1]) + '<br>'


                p.time_update = max(new_time)
                p.save()
            send_mail(
                'New items for: {}'.format(self.job_name),
                '',
                'mykhailo.kuznietsov@gmail.com',
                [p.user.email],
                fail_silently=False,
                html_message=message
            )
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
