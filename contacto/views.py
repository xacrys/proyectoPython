from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.
def contacto(request):
    contacto_form = ContactForm()
    if request.method == "POST":
        contacto_form = ContactForm(data=request.POST)
        if contacto_form.is_valid():
            name = request.POST.get("name")
            email = request.POST.get("email")
            content = request.POST.get("content")
            emailToSend = EmailMessage(
                "ITQ: Asunto del Mensaje",
                "De {} <{}> \n\n\n Escribio: \n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["cristiantintinmedina@hotmail.com"],
                reply_to=[email],
            )
            try:
                emailToSend.send()
                return redirect(reverse("contacto") + "?emailSend")
            except:
                return redirect(reverse("contacto") + "?emailNotSend")
            # logica para enviar el correo
    # logica que guarda en el modelo
    return render(request, "contacto/contacto.html", {"formulario": contacto_form})

