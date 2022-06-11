from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from AppFamilia.models import parientesPorMadre, parientesPorPadre

def plantilla1(self):
    madre = parientesPorMadre.objects.all()
    padre = parientesPorPadre.objects.all()
    diccionario = {'madre': madre, "padre": padre}
    plantilla = loader.get_template('plantilla1.html')

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)
