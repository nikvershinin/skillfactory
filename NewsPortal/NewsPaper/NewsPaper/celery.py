import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsPaper.settings')

app = Celery('NewsPaper')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

# app.conf.beat_schedule = {
#     'when_creating_post': {
#         'task': 'news.tasks.notify_about_new_post',
#         'schedule': 30,
#         'args': ("some_arg"),
#     },
# }
#  каждый понедельник в 8
# app.conf.beat_schedule = {
#     'when_week': {
#         'task': 'news.tasks.notify_weekly',
#         'schedule': crontab(hour=8, minute=0, day_of_week='monday'),
#         # 'args': (agrs),
#     },
# }
# app.conf.beat_schedule = {
#     'when_week': {
#         'task': 'news.tasks.notify_weekly',
#         'schedule': 30,
#         'args': ("some_arg"),
#     },
# }