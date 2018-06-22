from django.shortcuts import render
from django.views.generic import View
from apps.goods import models
# Create your views here.
from apps.goods import models


class IndexView(View):

    def get(self,request,*args,**kwargs):
            condition = {}
            for k, v in kwargs.items():
                    temp = int(v)
                    kwargs[k] = temp
            print(kwargs)
            system_id = kwargs.get("system_id")
            country_id = kwargs.get("country_id")
            area_id = kwargs.get("area_id")
            house_id = kwargs.get("house_id")
            time_id = kwargs.get('time_id')
            system_list = models.System.objects.all()
            house_list = models.House.objects.all()
            time_list = models.Time.objects.all()
            if system_id == 0:
                    class_country_list = models.Country.objects.all()
                    if country_id == 0:
                            pass
                    else:
                            kwargs["country_id"] = 0
                            condition["country_id"] = country_id

            else:
                    system_obj = models.System.objects.filter(id=system_id).first()
                    class_country_list = system_obj.country.all()

                    vlist = system_obj.country.all().values_list('id')
                    if not vlist:
                            country_id_list = []
                    else:
                            country_id_list = list(zip(*vlist))[0]
                    if country_id == 0:
                            condition["country_id__in"] = country_id_list
                    else:
                            if country_id in class_country_list:
                                    condition["country_id"] = country_id
                            else:
                                    condition["country_id__in"] = country_id_list

            if country_id == 0:
                    class_area_list = models.Area.objects.all()
                    if area_id == 0:
                            pass
                    else:
                            kwargs['area_id'] = 0
                            condition["area_id"] = area_id
            else:
                    country_obj = models.Country.objects.filter(id=country_id).first()
                    class_area_list = models.Area.objects.filter(country__name=country_obj)
                    condition['area_id'] = class_area_list

            if house_id == 0:
                    pass
            else:
                    condition["house_id"] = house_id

            if time_id == 0:
                    pass
            else:
                    condition["time_id"] = time_id

            return render(request, 'index.html',
                          {
                                  "system_list": system_list,
                                  "class_country_list": class_country_list,
                                  "class_area_list": class_area_list,
                                  "house_list": house_list,
                                  "time_list": time_list,
                                  "kwargs": kwargs
                          }
                          )

