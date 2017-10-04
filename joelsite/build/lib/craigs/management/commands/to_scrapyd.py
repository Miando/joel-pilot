from django.core.management.base import BaseCommand, CommandError
from craigs.models import PersonOptions
from django.contrib.auth.models import User
import requests


class Command(BaseCommand):

    def handle(self, *args, **options):
        tasks = PersonOptions.objects.all()
        url = 'http://localhost:6800/schedule.json'
        for task in tasks:
            if task.is_active:
                user_email = task.user.email
                params = {'project':'craiglist','spider':'craigs1'}
                params['city'] = task.city
                params['pk'] = task.pk
                params['user_email'] = user_email
                params['category'] = task.category
                params['subcategory'] = task.subcategory
                params['options'] = task.options
                params['job_name'] = task.job_name
                options = task.options
                # params['time_update'] = task.time_update
                keyword = task.keyword
                if keyword != '':
                    keyword = '?query=' + keyword
                else:
                    options = "?" + options[1:]
                params['keyword'] = keyword
                params['url_task1'] = task.city[:-1] + task.subcategory + keyword + options
                if task.url:
                    params['url_task1'] = task.url
                try:
                    params['stop_word'] = task.stop_word
                except:
                    pass
                print(params)
                response = requests.post(url, data=params)
                print(response.status_code)
