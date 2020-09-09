import sys, socket

def start():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(("127.0.0.1", 47200))
    except socket.error:
        print ("!!!scheduler already started, DO NOTHING")
    else:
        from apscheduler.schedulers.background import BackgroundScheduler
        from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
        from .update_api import UpdateApi
        from datetime import datetime
        
        scheduler = BackgroundScheduler()
        scheduler.add_job(UpdateApi().end_today_game, 'interval', seconds=10)
        scheduler.add_job(UpdateApi().start_today_game, 'interval', seconds=10)
        scheduler.add_job(UpdateApi().alter_slip, 'interval', seconds=10)
        scheduler.add_job(UpdateApi().send_birthday_msg, 'interval', hours=24, start_date='2020-09-06 00:00:00')
        scheduler.add_job(UpdateApi().add_raffle_members, 'interval', seconds=10)
        scheduler.add_job(UpdateApi().end_raffle_draw, 'interval', seconds=10)
        scheduler.add_job(UpdateApi().init_game_setting, 'interval', hours=3)
        scheduler.add_job(UpdateApi().check_payments, 'interval', seconds=15)
        scheduler.add_job(UpdateApi().remove_limit, 'interval', hours=24, start_date='2020-07-15 00:00:00')
        scheduler.start()
# from apscheduler.schedulers.background import BackgroundScheduler
# from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
# from .update_api import UpdateApi
# from datetime import datetime


# def start():
#     scheduler = BackgroundScheduler()
#     scheduler.add_job(UpdateApi().end_today_game, 'interval', seconds=10)
#     scheduler.add_job(UpdateApi().start_today_game, 'interval', seconds=10)
#     scheduler.add_job(UpdateApi().alter_slip, 'interval', seconds=10)
#     scheduler.add_job(UpdateApi().add_raffle_members, 'interval', seconds=10)
#     scheduler.add_job(UpdateApi().send_birthday_msg, 'interval', seconds=30)
#     scheduler.add_job(UpdateApi().end_raffle_draw, 'interval', seconds=10)
#     scheduler.add_job(UpdateApi().init_game_setting, 'interval', hours=3)
#     scheduler.add_job(UpdateApi().check_payments, 'interval', seconds=15)
#     scheduler.add_job(UpdateApi().remove_limit, 'interval', hours=24, start_date='2020-07-15 00:00:00')
#     scheduler.start()

# # import logging

# # from apscheduler.schedulers.background import BackgroundScheduler
# # from apscheduler.executors.pool import ProcessPoolExecutor, ThreadPoolExecutor
# # #from django_apscheduler.jobstores import register_events, register_job
# # from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
# # from .update_api import UpdateApi

# # from django.conf import settings

# # #Create scheduler to run in a thread inside the application process
# # # scheduler = BackgroundScheduler(settings.SCHEDULER_CONFIG)

# # # def start():
# # #     if settings.DEBUG:
# # #       	# Hook into the apscheduler logger
# # #         logging.basicConfig()
# # #         logging.getLogger('apscheduler').setLevel(logging.DEBUG)

# # #     # Adding this job here instead of to crons.
# # #     # This will do the following:
# # #     # - Add a scheduled job to the job store on application initialization
# # #     # - The job will execute a model class method at midnight each day
# # #     # - replace_existing in combination with the unique ID prevents duplicate copies of the job
# # #     scheduler.add_job(UpdateApi().testing, "interval", id="my_class_method", seconds=10, replace_existing=True)
# # #     scheduler.add_job(UpdateApi().testingtwo, "interval", id="my_class_method2", seconds=10, replace_existing=True)

# # #     # Add the scheduled jobs to the Django admin interface
# # #     register_events(scheduler)

# # #     scheduler.start()
# # def start():
# #     try:
# #         scheduler = BackgroundScheduler()
# #         scheduler.add_jobstore(DjangoJobStore(), "default")

# #         @register_job(scheduler, 'interval', seconds=10)
# #         def newTest():
# #             print('this is the new one')
# #         register_events(scheduler)
# #         scheduler.start()
# #     except Exception as e:
# #         print(e)