from django.shortcuts import render
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
import smtplib
from django.conf import settings


from .models import Images,Compititiveprice,FreshAndOrganicBeans,Specialoffer,Bookyourtable,Ourclientssay,Contact


# Create your views here.
@csrf_exempt
def loadindex(request):
    if request.POST:
        name = request.POST["uname"]
        email = request.POST["uemail"]
        date = request.POST["udate"]
        time = request.POST["utime"]
        amount = request.POST["uamount"]
        client = razorpay.Client(auth=("rzp_test_BIek49HafHJd1R", "hh2GlOWUCVAnj5n3CqmFmU1U"))
        payment = client.order.create({'amount': amount, 'currency': 'INR','payment_capture': '1'})


    data = Images.objects.all
    data1 = Compititiveprice.objects.all
    data2 = FreshAndOrganicBeans.objects.all
    data3 = Specialoffer.objects.all
    data4 = Bookyourtable.objects.all
    data5 = Ourclientssay.objects.all
    return render(request, "index.html", {"data": data, "data1": data1, "data2": data2,  "data3": data3, "data4": data4, "data5": data5})


def about(request):
    return render(request, "about.html")


def service(request):
    data = FreshAndOrganicBeans.objects.all
    return render(request, "service.html",{"data": data})


def menu(request):
    data = Compititiveprice.objects.all
    return render(request, "menu.html",{"data": data})


def contact(request):
    if request.POST:
        name = request.POST["uname"]
        email1 = request.POST["uemail"]
        subject = request.POST["usubject"]
        message1= request.POST["umessage"]

        subject = 'Confirmation Email'
        message = 'Welcome to koppee website'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ["unnatipanchal1141@gmail.com","hemishreepethani@gmail.com"]
        send_mail(subject, message, email_from, recipient_list)


    return render(request, "contact.html")


def reservation(request):
    data = Bookyourtable.objects.all
    return render(request, "reservation.html",{"data": data})


def testimonial(request):
    data = Ourclientssay.objects.all
    return render(request, "testimonial.html",{"data": data})

def success(request):
    return render(request,"success.html")