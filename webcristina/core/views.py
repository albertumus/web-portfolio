from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import TemplateView
from django.urls import reverse
from .models import Personalizacion, Servicios
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.

def personalizacion(request):
    
    servicios = Servicios.objects.all()
    print(servicios)
    
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get("name", "")
            email = request.POST.get("email", "")
            comment = request.POST.get("comment", "")
            #Supones que todo ha ido bien, enviamos y redireccionamos
            email = EmailMessage(
                "Cristina Blanco Portfolio - Nuevo Mensaje de Contacto",
                "De {} <{}>\n\nEscribio:\n\n{}".format(name,email,comment),
                "cristina.blanco.portfolio@gmail.com",
                ["cristina.blanco.portfolio@gmail.com"],
                reply_to=[email]
            )

            try:
                #todo ha ido bien
                email.send()
                return redirect(reverse("home")+ "?ok")
            except:
                #algo no ha ido bien
                return redirect(reverse("home")+ "?fail")

    
    return render(request, "core/home.html", {"personalizacion": personalizacion,"form": contact_form, "servicios": servicios})



#def contact(request):
    #contact_form = ContactForm()
    #return render(request, "core/home.html", {"form":contact_form})
