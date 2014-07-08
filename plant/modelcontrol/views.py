# Create your views here.

from django.shortcuts import render, get_object_or_404
from django.views import generic

from modelcontrol.models import Servo


class IndexView(generic.ListView):
    template_name = 'modelcontrol/index.html'
    context_object_name = 'servo_list'

    def get_queryset(self):
        return Servo.objects.all()


def update(request, servo_id):
    p = get_object_or_404(Servo, pk=servo_id)
    try:
        p.position = request.POST['position']
        p.save()
    except (KeyError):
        # error page
        pass

    servo_list = Servo.objects.all()
    context = {'servo_list': servo_list}
    return render(request, 'modelcontrol/index.html', context)