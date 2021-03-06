from django.shortcuts import render
from django.views.generic import ListView
from .models import Picture, Therapist, Therapy
from django.shortcuts import render,reverse , redirect
from .forms  import Contactform
from django.core.mail import EmailMessage


#Index
def index(request):
    index= Picture.objects.all()
    return render (request,'index.html',{'index' : index})

# Contact
def contacto(request):
    contact_form = Contactform()
    if request.method == "POST":  
        contact_form = Contactform(data=request.POST)
        if contact_form.is_valid(): 
            name= request.POST.get('name')
            email= request.POST.get('email')
            content= request.POST.get('content')
            mail = EmailMessage(
                "Prana Massage : Nuevo Mensaje de Contacto ",
                "De {} {}\n\nEscribio:\n\n {}".format(name ,email,content),
                "circuloin.com", ["ignaciovidondo@hotmail.com"],
                reply_to = [email]
                )
            try:
                mail.send() #Si esta todo ok redireccionar
                return redirect(reverse("automatic")+"?ok")
                 
                 
            
            except:
                return redirect(reverse("contacto")+"?fail")
            
    return render (request, 'contact.html', {'form':contact_form })

#Automatic message after contact us
def automatic(request):
    return render (request, 'automatic.html') 

#About-Us
def about(request):
    about= Picture.objects.all()
    return render (request,'about-us.html',{'about' : about})

#Therapies
def therapies(request):
    therapies= Therapy.objects.all()
    return render (request,'therapies.html',{'therapies' : therapies }) 

#Therapist
def therapist(request):
    therapist= Therapist.objects.all()
    return render (request,'therapist.html',{'therapist' : therapist }) 