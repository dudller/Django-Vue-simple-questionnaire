from django.contrib import admin

from .models import Person,Telefon,Choroby,Uzaleznienia

class PersonAdmin(admin.ModelAdmin):
    fieldsets = [
        ('kod_pocztowy',               {'fields': ['kod_pocztowy']}),
        ('wiek', {'fields': ['wiek']}),
        ('plec', {'fields': ['plec']}),
        ('student', {'fields': ['student']}),
        ('choroby', {'fields': ['choroby']}),
        ('uzaleznienia', {'fields': ['uzaleznienia']}),
        ('odpornosc_stresowa', {'fields': ['odpornosc_stresowa']}),
        ('rozproszenie', {'fields': ['rozproszenie']}),
        ('wynik1', {'fields': ['wynik1']}),
        ('wynik2', {'fields': ['wynik2']}),
        ('wynikSAR', {'fields': ['wynikSAR']}),
        ('wiedza_o_nomofobii', {'fields': ['wiedza_o_nomofobii']}),
        ('podejrzenie_nomofobii', {'fields': ['podejrzenie_nomofobii']})
    ]
    list_display = ('student', 'kod_pocztowy')
    list_filter = ['student']
    search_fields = ['kod_pocztowy']

admin.site.register(Person, PersonAdmin)
