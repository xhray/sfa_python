import os
import sys

os.chdir(sys.path[0])
sys.path.append('..')

from apscheduler.scheduler import Scheduler
from admin.iislogs import *

#sched = Scheduler(daemonic=False)
#
#@sched.cron_schedule(day_of_week='mon-fri', hour='*', minute='0-59', second='*/2', args=['hello world, xxx'])
# def job_function(a):
#    print '%s %s'% (datetime.datetime.now(), a)
#
# sched.start()

if __name__ == '__main__':
    sched = Scheduler(daemonic=False)

    # import daily iis logs
    sched.add_cron_job(import_logs, day_of_week='mon-sun', hour='14',
                       minute='58',
                       args=['C:\Users\Administrator\Desktop\W3SVC1\u_ex140508.log'])

    # daily iis logs analysis
    sched.add_cron_job(analysis, day_of_week='0-6',
                       hour='22', minute='07', args=[datetime.now()])

    sched.start()


#   def add_cron_job(self, func, year=None, month=None, day=None, week=None,
#                    day_of_week=None, hour=None, minute=None, second=None,
#                    start_date=None, args=None, kwargs=None, **options):
#       """
#       Schedules a job to be completed on times that match the given
#       expressions.
#
#       :param func: callable to run
#       :param year: year to run on
#       :param month: month to run on
#       :param day: day of month to run on
#       :param week: week of the year to run on
#       :param day_of_week: weekday to run on (0 = Monday)
#       :param hour: hour to run on
#       :param second: second to run on
#       :param args: list of positional arguments to call func with
#       :param kwargs: dict of keyword arguments to call func with
#       :param name: name of the job
#       :param jobstore: alias of the job store to add the job to
#       :param misfire_grace_time: seconds after the designated run time that
#           the job is still allowed to be run
#       :return: the scheduled job
#       :rtype: :class:`~apscheduler.job.Job`
