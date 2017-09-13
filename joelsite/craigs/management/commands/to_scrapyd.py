from django.core.management.base import BaseCommand, CommandError
from craigs.models import PersonOptions
from django.contrib.auth.models import User
import requests


class Command(BaseCommand):

    def handle(self, *args, **options):
        users = User.objects.all()
        url = 'http://localhost:6800/schedule.json'
        for user in users:
            user_email = user.email
            objs = PersonOptions.objects.filter(user=user)
            for obj in objs:
                params = {'project':'craiglist','spider':'craigs1'}
                params['city'] = obj.city
                params['category'] = obj.category
                params['subcategory'] = obj.subcategory
                params['options'] = obj.subcategory
                params['keyword'] = obj.keyword
                try:
                    params['stop_word'] = obj.stop_word
                except:
                    pass
                print (params)
                response = requests.post(url, data=params)
