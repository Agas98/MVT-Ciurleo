from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context, loader

def plantilla1(self):
    nom = "Augusto"
    ape = "Ciurleo"
    diccionario = {'nombre': nom, "apellido": ape}
    plantilla = loader.get_template('plantilla1.html')

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)