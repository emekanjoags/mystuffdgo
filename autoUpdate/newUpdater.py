import logging

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ProcessPoolExecutor, ThreadPoolExecutor
#from django_apscheduler.jobstores import register_events, register_job
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
from .update_api import UpdateApi

from django.conf import settings

# Create scheduler to run in a thread inside the application process
scheduler = BackgroundScheduler(settings.SCHEDULER_CONFIG)

# def start():
#     if settings.DEBUG:
#       	# Hook into the apscheduler logger
#         logging.basicConfig()
#         logging.getLogger('apscheduler').setLevel(logging.DEBUG)

#     # Adding this job here instead of to crons.
#     # This will do the following:
#     # - Add a scheduled job to the job store on application initialization
#     # - The job will execute a model class method at midnight each day
#     # - replace_existing in combination with the unique ID prevents duplicate copies of the job
#     scheduler.add_job(UpdateApi().testing, "interval", id="my_class_method", seconds=10, replace_existing=True)

#     # Add the scheduled jobs to the Django admin interface
#     register_events(scheduler)

#     scheduler.start()
try:
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")

    @register_job(scheduler, 'interval', seconds=10)
    def newTest():
        print('this is the new one')
    register_events(scheduler)
    scheduler.start()
except Exception as e:
    print(e)