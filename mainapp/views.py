from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Person,Telefon,Choroby,Uzaleznienia
import json

def index(request):
    if request.method == 'POST':
        return HttpResponse(request)
    else:
        return render(request, 'index.html')

def end(request):
    return render(request, 'end.html')

def vote(request):
    if request.method == 'POST':
        formData=request.POST.get("formData")
        jsonData=json.loads(formData)

        try:


            p=Person(kod_pocztowy=jsonData['kod'],wiek=jsonData['wiek'],plec=jsonData['plec'],student=jsonData['student'],odpornosc_stresowa=jsonData['stres'],rozproszenie=jsonData['rozpraszanie']
            ,wynik1=jsonData['tru_false1'],wynik2=jsonData['tru_false2'],wynikSAR=jsonData['odp_SAR'],wiedza_o_nomofobii=jsonData['odp_nomofobia'],podejrzenie_nomofobii=jsonData['odp_nomofobia2'])

        except():
            return HttpResponse(jsonData['choroby'])
        else:
            p.save()
        try:
            p.telefon_set.create(rodzaj=jsonData['telefon'],przywiazanie=jsonData['przywiazanie'],przekatna=jsonData['przekatna'],czas_dzienne=jsonData['czas'],najczesciej=jsonData['najczesciej'],czas_najczesciej=jsonData['najczesciej_czas'],
            cena=jsonData['cena'])
            for i in jsonData['choroby']:
                print(i)
                c=Choroby.objects.get(nazwa=i)

                p.choroby.add(c)
            for i in jsonData['uzaleznienia']:
                print(i)
                u=Uzaleznienia.objects.get(nazwa=i)
                p.uzaleznienia.add(u)
        except():
            return HttpResponse('Coś poszło nie tak... Zespół techików NA PEWNO pracuje JUŻ nad rozwiązaniem tego problemu')
        else:
            p.save()
    return HttpResponseRedirect(reverse('ankieta:end'))
