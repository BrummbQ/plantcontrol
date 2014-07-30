# Create your views here.

from django.shortcuts import render, get_object_or_404
from django.views import generic

from modelcontrol.models import Plant

from xmlrpclib import ServerProxy, Error


class IndexView(generic.ListView):
    template_name = 'modelcontrol/index.html'
    context_object_name = 'plant_list'

    def get_queryset(self):
        return Plant.objects.all()


def update(request, plant_id):
    p = get_object_or_404(Plant, pk=plant_id)
    try:
        motor = ServerProxy('http://127.0.0.1:1337', allow_none=True)
        if 'position' in request.POST:
            p.servo.position = request.POST['position']
            p.servo.save()
        if 'speed' in request.POST:
            p.motor.speed = request.POST['speed']
            p.motor.save()
            motor.set_rate(0, 7)
            motor.set_rate(int(p.motor.speed), 25)
        # set device

    except (KeyError):
        # error page
        pass

    plant_list = Plant.objects.all()
    context = {'plant_list': plant_list}
    return render(request, 'modelcontrol/index.html', context)