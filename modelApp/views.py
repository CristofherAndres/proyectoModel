from django.shortcuts import render
from modelApp.models import Persona
from modelApp.forms import PersonaRegistrationForm

# Create your views here.

def listarPersonas(request):
    #ORM solicitar todos los datos
    # SQL <- Select * from personas
    personas = Persona.objects.all()
    data = {
        'personas' : personas
    }
    return render(request, 'modelApp/personas.html',data)

def registrarPersonas(request):
    form = PersonaRegistrationForm()

    if request.method == 'POST':
        form = PersonaRegistrationForm(request.POST)
        if form.is_valid():
            print("El form es valido")
            print("Nombre: ", form.cleaned_data['nombre'])
            print("Correo: ", form.cleaned_data['email'])
            print("Telefono: ", form.cleaned_data['telefono'])
            form.save()
            return listarPersonas(request)

    data = {'form' : form}
    return render(request, 'modelApp/formPersona.html',data)