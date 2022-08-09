from django.http import HttpResponse

from AppCoder.models import Curso

def curso(self):
      curso = Curso(nombre = "Desarrollo web", camada = "19881")
      curso.save()
      documentoDeText = f"--->Curso:{curso.nombre}, Camada:{curso.camada}"
      return HttpResponse(documentoDeText)
