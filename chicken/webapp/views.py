from django.shortcuts import render

# Create your views here.
from django.template import loader, RequestContext
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