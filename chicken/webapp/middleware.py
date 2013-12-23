import pytz

from django.utils import timezone

class TimezoneMiddleware(object):
    timezone.activate('US/Pacific')
    # def process_request(self, request):
    #     tzname = request.session.get('django_timezone')
    #     if tzname:
    #         timezone.activate(pytz.timezone(tzname))
    #     else:
    #         timezone.deactivate()