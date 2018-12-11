from django.views.generic.base import View
from django.http import HttpResponse
from appdemo01.models import Cars
import json


class DemoView(View):
    def get(self, request):
        car_list = []
        cars = Cars.objects.all()
        for car in cars:
            car_dic = {}
            car_dic["name"] = car.car_name
            car_dic["type"] = car.car_type
            car_dic["color"] = car.car_color
            car_dic["count"] = car.car_count
            car_list.append(car_dic)
        return HttpResponse(json.dumps(car_list), content_type="application/json")
