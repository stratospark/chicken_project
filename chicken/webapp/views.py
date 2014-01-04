from django.db import Error
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader, RequestContext
from django.views.decorators.csrf import csrf_exempt
from webapp.models import SensorData


def index(request):
    context = RequestContext(request, {
        'latest_question_list': None,
        'chickens_put_away': not SensorData.objects.last().door_open
    })

    return render(request, 'webapp/index.html', context)

    # latest_sensor_reads = SensorData.objects.all()[:10]
    # output = ', '.join(["%s" % (s.timestamp) for s in latest_sensor_reads])
    # return HttpResponse(output)


@csrf_exempt
def add_data(request):
    data_string = request.body
    try:
        s = SensorData.create_from_string(data_string)
        s.save()
        return HttpResponse('OK')
    except Exception as e: # TODO: catch a more specific exception
        return HttpResponse(e, status=400)