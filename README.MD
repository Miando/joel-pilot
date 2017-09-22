pip install -r requirements.txt
nohup scrapyd >/dev/null 2>&1 &
pip install django whitenoise
python manage.py collectstatic
python manage.py migrate
scrapy crawl get_cities
scrapy crawl subcategories