import os

from joelsite import settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'joelsite.settings'
import django
django.setup()

from craigs.models import AdditionalOptions


with open("options2.csv", "r") as file:
    for line in file.readlines():
        a = (line.split(","))
        print (a)
        s = AdditionalOptions(
            subcategory=a[1],
            option=a[0].strip(),
            option_for_frontend=a[2].replace('  /  ', '-').replace(' / ', '-').replace('/', '-') \
                .replace('[', '').replace(']', '').replace("'", '').strip()
        )
        s.save()
