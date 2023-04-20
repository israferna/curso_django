from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
import datetime

class Persona(object):
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido

def saludo(request): # primera vista

    nombre="Juan"
    apellido="Perez"
    p1=Persona(nombre,apellido)
    fecha_actual=datetime.datetime.now()

    #doc_externo=open("/home/israferna/Documents/VisualStudio/ProyectosDjango/Proyecto1/Proyecto1/plantillas/miplantilla.html")
    #plt=Template(doc_externo.read())
    #doc_externo.close()
    #doc_externo=get_template('miplantilla.html')


    temario=["Modelos","Plantillas","Formularios","Vistas"]

    diccionario={"nombre_persona":p1.nombre,
        "apellido_persona":p1.apellido, 
        "fecha":fecha_actual,
        "temas":temario}

    #documento=doc_externo.render(ctx)

    #return HttpResponse(documento)
    return render(request,"miplantilla.html",diccionario)


def despedida(request):

    return HttpResponse("Nos vemos pronto")


def dameFecha(request):
    fecha_actual=datetime.datetime.now()
    documento="""
    <html>
        <body>
        <h2>
            Fecha y hora actuales %s
        </h2>
        </body>
    </html>
    """ % fecha_actual

    return HttpResponse(documento)