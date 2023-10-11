from django.shortcuts import render
from modelApp.models import Persona

# Create your views here.

def listarPersonas(request):
    #ORM solicitar todos los datos
    # SQL <- Select * from personas
    personas = Persona.objects.all()
    data = {
        'personas' : personas
    }

    return render(request, 'modelApp/personas.html',data)