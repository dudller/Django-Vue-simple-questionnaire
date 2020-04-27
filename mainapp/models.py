from django.db import models

class Choroby(models.Model):
    nazwa=models.CharField(max_length=200)
    def __str__(self):
        return self.nazwa

class Uzaleznienia(models.Model):
    nazwa=models.CharField(max_length=200)
    def __str__(self):
        return self.nazwa

class Person(models.Model):
    kod_pocztowy=models.CharField(max_length=6)
    wiek=models.IntegerField(default=0)
    plec=models.CharField(max_length=20)
    student=models.CharField(max_length=4)
    choroby=models.ManyToManyField(Choroby)
    uzaleznienia=models.ManyToManyField(Uzaleznienia)
    odpornosc_stresowa=models.IntegerField(default=0)
    rozproszenie=models.IntegerField(default=0)
    wynik1=models.IntegerField(default=0)
    wynik2=models.IntegerField(default=0)
    wynikSAR=models.IntegerField(default=0)
    wiedza_o_nomofobii=models.CharField(max_length=20)
    podejrzenie_nomofobii=models.CharField(max_length=20)

class Telefon(models.Model):
    person=models.ForeignKey(Person, on_delete=models.CASCADE)
    rodzaj=models.CharField(max_length=20)
    przywiazanie=models.CharField(max_length=200)
    przekatna=models.FloatField(default=0)
    czas_dzienne=models.FloatField(default=0)
    najczesciej=models.CharField(max_length=200)
    czas_najczesciej=models.FloatField(default=0)
    cena=models.CharField(max_length=20)
