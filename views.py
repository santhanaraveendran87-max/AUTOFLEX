from django.shortcuts import get_object_or_404,render,redirect,HttpResponse
from .import models
from .models import user,work,show,feedback,spare,carsell,bikesell,carrent,BookingCarsell,BookingCarRent,BookingBikesell,BookingBikeRent,bikerent,Bookingworkshop,S_services,Bookingshowroom,Approvedworkshops,showpost,sparepost,Bookingtestdrive,Approvedtestdrive


def register(request):
    if request.method=="POST":
        Username=request.POST.get("username")
        Email=request.POST.get("email")
        Phonenumber=request.POST.get("phonenumber")
        Password=request.POST.get("password")
        Place=request.POST.get("place")
        Pincode=request.POST.get("pincode")
        Image=request.FILES.get("image")
        if user.objects.filter(email=Email).exists():
            return HttpResponse("<script>alert('This email already exists'); window.location.href='/register';</script>")
        class1=models.user(username=Username,email=Email,phonenumber=Phonenumber,password=Password,place=Place,pincode=Pincode,image=Image,status='applied').save()
        return redirect('login')
    return render(request,'userregistration.html')
def index(request):
    return render(request,'index.html')


from django.core.exceptions import ObjectDoesNotExist

def login(request):
    if request.method == "POST":
        Email = request.POST.get("email")
        Password = request.POST.get("password")
        
        try:
            us = models.user.objects.get(email=Email, password=Password)
            if us:
                request.session['email'] = us.email
                if us.status == 'approved':
                    return redirect('home')
                else:
                    return HttpResponse("<script>alert('Your account is not yet approved. Please wait until the admin approves your registration.'); window.location.href='/login/';</script>")
        except ObjectDoesNotExist:
            return HttpResponse("<script>alert('Invalid email or password'); window.location.href='/login';</script>")
    
    return render(request, 'login.html')

def home(request):
    return render(request,'home.html')

def userlist(request):
    u=user.objects.all()
    return render(request,'userlist.html',{'user':u})
    # Create your views here.
def deluser(request,id):
    d=user.objects.get(id=id)
    d.delete()
    return redirect('userlist')

def userprofile(request):
    email=request.session['email']
    cr=user.objects.get(email=email)
    username=cr.username
    email=cr.email
    image=cr.image
    bio=cr.bio
    phonenumber=cr.phonenumber
    place=cr.place
    pincode=cr.pincode

           
    return render(request,'userprofile.html',{'username':username,'email':email,'image':image,'bio':bio,'phonenumber':phonenumber,'place':place,'pincode':pincode})


from django.contrib.auth import logout

def ulogout(request):
    logout(request)  # This logs the user out
    return redirect('index')  # Redirect to login page or homepage


def workreg(request):
    if request.method=="POST":
        Workshopname=request.POST.get("workname")
        Email=request.POST.get("email")
        Password=request.POST.get("password")
        Phonenumber=request.POST.get("phonenumber")
        Address=request.POST.get("workaddress")
        Registration=request.POST.get("workregno")
        Image=request.FILES.get("image")
        if work.objects.filter(email=Email).exists():
            return HttpResponse("<script>alert('This email already exists'); window.location.href='/workreg';</script>")
        class2=models.work(workname=Workshopname,email=Email,password=Password,phonenumber=Phonenumber,workaddress=Address,workregno=Registration,image=Image,status='applied').save()
        return redirect('worklogin')
    return render(request,'workreg.html')


def worklogin(request):
    if request.method == "POST":
        Email = request.POST.get("email")
        Password = request.POST.get("password")

        try:
            us = models.work.objects.get(email=Email)
            if us.password == Password:  # Insecure; use Django authentication
                if us.status == 'approved':
                    request.session['email'] = us.email
                    return redirect('workhome')
                else:
                    return HttpResponse("<script>alert('Your account is not yet approved. Please wait until the admin approves your registration.'); window.location.href='/worklogin';</script>")
            else:
                return HttpResponse("<script>alert('Invalid email or password'); window.location.href='/worklogin';</script>")
        
        except ObjectDoesNotExist:
            return HttpResponse("<script>alert('Invalid email or password'); window.location.href='/worklogin';</script>")

    return render(request, 'worklogin.html')


def worklist(request):
    u=work.objects.all()
    return render(request,'worklist.html',{'work':u})
    # Create your views here.
def delwork(request,id):
    d=work.objects.get(id=id)
    d.delete()
    return redirect('worklist')

def workprofile(request):
    email=request.session['email']
    cr=work.objects.get(email=email)
    workname=cr.workname
    email=cr.email
    image=cr.image
    phonenumber=cr.phonenumber
    workaddress=cr.workaddress
    workregno=cr.workregno
           
    return render(request,'workprofile.html',{'workname':workname,'email':email,'image':image,'phonenumber':phonenumber,'workaddress':workaddress,'workregno':workregno})


def workhome(request):
    return render(request,'workhome.html')

def wlogout(request):
    logout(request)  
    return redirect('index') 

def w_updateprou(request):
    email=request.session['email']
    cr=work.objects.get(email=email)
    if cr:
        user_info={'workname':cr.workname,'email':cr.email,'phonenumber':cr.phonenumber,'password':cr.password,'workaddress':cr.workaddress,'workregno':cr.workregno,'image':cr.image}
        return render(request,'w_updateprou.html',user_info)
    else:
        return render(request,'w_updateprou.html')
    
def w_proupdateu(request):
    email=request.session['email']
    if request.method=='POST':
        workname=request.POST.get('workname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        phonenumber=request.POST.get('phonenumber')
        workaddress=request.POST.get('workaddress')
        workregno=request.POST.get('workregno')
        image=request.POST.get('image')
        data=work.objects.get(email=email)
        data.workname=workname
        data.email=email
        data.phonenumber=phonenumber
        data.password=password
        data.workaddress=workaddress
        data.workregno=workregno
        if image:
            data.image=image
        data.save()
        cr=work.objects.get(email=email)
        if cr:
                user_info={'workname':cr.workname,'email':cr.email,'phonenumber':cr.phonenumber,'password':cr.password,'workaddress':cr.workaddress,'workregno':cr.workregno,'image':cr.image}
                return render(request,'workprofile.html',user_info)
        else:
                return render(request,'w_updateprou.html')
    return render(request,'w_updateprou.html')

    
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db import models

def addservices(request):
    semail = request.session.get('email')
    workshop = models.work.objects.get(email=semail)
    
    if request.method == "POST":
        service = request.POST.get('service')
        price_range = request.POST.get('price_range') 
        workername = request.POST.get('workername')
        phoneno=request.POST.get('phoneno')
        
        # Generate unique service_id
        # Get the highest current service_id and increment it by 1
        last_service = models.Services.objects.all().order_by('service_id').last()
        if last_service:
            service_id = last_service.service_id + 1
        else:
            service_id = 1  # If no services exist, start with service_id 1
        
        # Check if the service already exists by service_id
        if models.Services.objects.filter(service_id=service_id).exists():
            alert_message = "<script>alert('This service already added.'); window.location.href='/addservices';</script>"
            return HttpResponse(alert_message)
        
        # Create and save the new service
        models.Services(workshop=workshop, service_id=service_id, services=service, price_range=price_range,workername=workername,phoneno=phoneno).save()
        return redirect('services_list')
    
    else:
        return render(request, 'add_services.html')


def services_list(request):
    semail=request.session.get('email')
    workshop=models.work.objects.get(email=semail)
    services=models.Services.objects.filter(workshop=workshop)
    return render(request,'service_list.html',{'services':services})

def delete_service(request,service_id):
    services=models.Services.objects.get(service_id=service_id)
    services.delete()
    return redirect('services_list')

def edit_service(request, service_id):
    semail = request.session.get('email')
    workshop = models.work.objects.get(email=semail)
    
    try:
        service = models.Services.objects.get(service_id=service_id, workshop=workshop)
    except models.Services.DoesNotExist:
        return HttpResponse("<script>alert('Service not found.'); window.location.href='/services_list';</script>")
    
    if request.method == "POST":
        # Get the updated values from the form
        service.services = request.POST.get('service')
        service.price_range = request.POST.get('price_range')
        service.workername = request.POST.get('workername')
        service.phoneno = request.POST.get('phoneno')

        # Save the updated service
        service.save()

        # Redirect to the service list page after updating
        return redirect('services_list')
    
    # For GET request, populate the form with the current service details
    return render(request, 'edit_service.html', {'service': service})
    
def book_services(request,id):
    semail=request.session.get('email')
    user=models.user.objects.get(email=semail)
    workshop=models.work.objects.get(id=id)
    services=models.Services.objects.filter(workshop=workshop)
    return render(request,'book_services.html',{'services':services,'user':user})

def booknow_services(request,service_id):
    semail = request.session.get('email')
    user=models.user.objects.get(email=semail)
    services=models.Services.objects.get(id=service_id)
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        date = request.POST.get('date')

       
        booking,created = Bookingworkshop.objects.get_or_create(
            user=user,
            services=services,
            date=date
        )
        if created:
            return redirect('mybookingworkshop')  
        else:
            alert="<script>alert('already booked'); window.location.href='/book_services/';</script>"
            return HttpResponse(alert)
    return render(request, 'booknow_services.html', {'services': services,'user':user})

def mybookingworkshop(request):
    email=request.session.get('email')
    user=models.user.objects.get(email=email)
    bookings=models.Bookingworkshop.objects.filter(user=user)
    return render(request, 'mybookingworkshop.html',{'bookings':bookings})

def listworkbookings(request,wid):
    services=models.Services.objects.get(id=wid)
    bookings=models.Bookingworkshop.objects.filter(services=services)
    return render(request,'listworkbookings.html',{'bookings':bookings})

def approveinsterestedworkshops(request,bid):
    booking=models.Bookingworkshop.objects.get(id=bid)
    user=booking.user
    services=booking.services
    status='approved'
    booking.approval_status='approved'
    booking.save()
    models.Approvedworkshops(user=user,services=services,status=status).save()
    # alert="<script>alert('The buyer is approved')window.location.href='/listcarbuyers/'</script>"
    return redirect('listworkbookings',wid=services.id)

def listworkbookings(request, wid):
    services = models.Services.objects.get(id=wid)
    bookings = models.Bookingworkshop.objects.filter(services=services)
    
    for booking in bookings:
        # Assuming booking.date is a datetime.date object, convert it to datetime if necessary
        booking_date = booking.date

        # Convert the booking's date to datetime (set the time to midnight)
        booking_datetime = datetime.combine(booking_date, datetime.min.time())
        
        # Get the current datetime
        current_datetime = datetime.now()

        # Compare the datetime objects
        if booking_datetime < current_datetime:
            # Handle your logic here (e.g., automatically reject after 2 minutes)
            pass

    return render(request, 'listworkbookings.html', {'bookings': bookings})

def approveinsterestedworkshops(request,bid):
    booking=models.Bookingworkshop.objects.get(id=bid)
    user=booking.user
    services=booking.services
    status='approved'
    booking.approval_status='approved'
    booking.save()
    models.Approvedworkshops(user=user,services=services,status=status).save()
    alert_message = f"""
    <script>
        alert('The Person is approved');
        window.location.href='/listworkbookings/{services.id}/';  // Redirect after alert
    </script>
    """
    return HttpResponse(alert_message)

def rejectinsterestedworkshops(request,bid):
    booking=models.Bookingworkshop.objects.get(id=bid)
    user=booking.user
    services=booking.services
    status='reject'
    booking.approval_status='reject'
    booking.save()
    models.Approvedworkshops(user=user,services=services,status=status).save()
    alert_message = f"""
    <script>
        alert('The Person is rejected');
        window.location.href='/listworkbookings/{services.id}/';  // Redirect after alert
    </script>
    """
    
    return HttpResponse(alert_message)

def showreg(request):
    if request.method=="POST":
        Showroomname=request.POST.get("showname")
        Email=request.POST.get("email")
        Password=request.POST.get("password")
        Phonenumber=request.POST.get("phonenumber")
        Address=request.POST.get("showaddress")
        Registration=request.POST.get("showregno")
        Image=request.FILES.get("image")
        if show.objects.filter(email=Email).exists():
            return HttpResponse("<script>alert('This email already exists'); window.location.href='/showreg';</script>")    
        class3=models.show(showname=Showroomname,email=Email,password=Password,phonenumber=Phonenumber,showaddress=Address, showregno=Registration,image=Image,status='applied').save()
        return redirect('showlogin')
    return render(request,'showreg.html')
 
def showlogin(request):
    if request.method == "POST":
        Email = request.POST.get("email")
        Password = request.POST.get("password")

        try:
            us = models.show.objects.get(email=Email, password=Password)
            if us.status == 'approved':
                request.session['email'] = us.email
                return redirect('showhome')
            else:
                return HttpResponse("<script>alert('Your account is not yet approved. Please wait until the admin approves your registration.'); window.location.href='/showlogin';</script>")
        except models.show.DoesNotExist:
            return HttpResponse("<script>alert('Invalid email or password'); window.location.href='/showlogin';</script>")

    return render(request, 'showlogin.html')

def showlist(request):
    u=show.objects.all()
    return render(request,'showlist.html',{'show':u})
    # Create your views here.
def delshow(request,id):
    d=show.objects.get(id=id)
    d.delete()
    return redirect('showlist')

def showprofile(request):
    email=request.session['email']
    cr=show.objects.get(email=email)
    showname=cr.showname
    email=cr.email
    image=cr.image
    phonenumber=cr.phonenumber
    showaddress=cr.showaddress
    showregno=cr.showregno
           
    return render(request,'showprofile.html',{'showname':showname,'email':email,'image':image,'phonenumber':phonenumber,'showaddress':showaddress,'showregno':showregno})

def s_updateprou(request):
    email=request.session['email']
    cr=show.objects.get(email=email)
    if cr:
        user_info={'showname':cr.showname,'email':cr.email,'phonenumber':cr.phonenumber,'password':cr.password,'showaddress':cr.showaddress,'showregno':cr.showregno,'image':cr.image}
        return render(request,'s_updateprou.html',user_info)
    else:
        return render(request,'s_updateprou.html')
    
def s_proupdateu(request):
    email=request.session['email']
    if request.method=='POST':
        showname=request.POST.get('showname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        phonenumber=request.POST.get('phonenumber')
        showaddress=request.POST.get('showaddress')
        showregno=request.POST.get('showregno')
        image=request.POST.get('image')
        data=show.objects.get(email=email)
        data.showname=showname
        data.email=email
        data.phonenumber=phonenumber
        data.password=password
        data.showaddress=showaddress
        data.showregno=showregno
        if image:
            data.image=image
        data.save()
        cr=show.objects.get(email=email)
        if cr:
                user_info={'showname':cr.showname,'email':cr.email,'phonenumber':cr.phonenumber,'password':cr.password,'showaddress':cr.showaddress,'showregno':cr.showregno,'image':cr.image}
                return render(request,'showprofile.html',user_info)
        else:
                return render(request,'s_updateprou.html')
    return render(request,'s_updateprou.html')



def showhome(request):
    return render(request,'showhome.html')

def shlogout(request):
    logout(request)  
    return redirect('index') 

def s_add_services(request):
    semail = request.session.get('email')
    showroom = models.show.objects.get(email=semail)
    
    if request.method == "POST":
        service = request.POST.get('service')
        price_range = request.POST.get('price_range') 
        
        # Generate unique service_id
        # Get the highest current service_id and increment it by 1
        last_service = models.S_services.objects.all().order_by('service_id').last()
        if last_service:
            service_id = last_service.service_id + 1
        else:
            service_id = 1  # If no services exist, start with service_id 1
        
        # Check if the service already exists by service_id
        if models.S_services.objects.filter(service_id=service_id).exists():
            alert_message = "<script>alert('This service already added.'); window.location.href='/s_add_services';</script>"
            return HttpResponse(alert_message)
        
        # Create and save the new service
        models.S_services(showroom=showroom, service_id=service_id, services=service, price_range=price_range).save()
        return redirect('s_services_list')
    
    else:
        return render(request, 's_add_services.html')


def s_services_list(request):
    semail=request.session.get('email')
    showroom=models.show.objects.get(email=semail)
    services=models.S_services.objects.filter(showroom=showroom)
    return render(request,'s_services_list.html',{'services':services})


def delete_service1(request,service_id):
    services=models.S_services.objects.get(service_id=service_id)
    services.delete()
    return redirect('s_services_list')

def edit_service1(request, service_id):
    semail = request.session.get('email')
    showroom = models.show.objects.get(email=semail)
    
    try:
        service = models.S_services.objects.get(service_id=service_id, showroom=showroom)
    except models.S_services.DoesNotExist:
        return HttpResponse("<script>alert('Service not found.'); window.location.href='/s_services_list';</script>")
    
    if request.method == "POST":
        # Get the updated values from the form
        service.services = request.POST.get('service')
        service.price_range = request.POST.get('price_range')

        # Save the updated service
        service.save()

        # Redirect to the service list page after updating
        return redirect('services_list')
    
    # For GET request, populate the form with the current service details
    return render(request, 'edit_service1.html', {'service': service})

def s_book_services(request,id):
    semail=request.session.get('email')
    user=models.user.objects.get(email=semail)
    showroom=models.show.objects.get(id=id)
    services=models.S_services.objects.filter(showroom=showroom)
    return render(request,'s_book_services.html',{'services':services,'user':user})

def s_booknow_services(request,service_id):
    semail = request.session.get('email')
    user=models.user.objects.get(email=semail)
    services=models.S_services.objects.get(id=service_id)
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        date = request.POST.get('date')

       
        booking,created = Bookingshowroom.objects.get_or_create(
            user=user,
            services=services,
            date=date
        )
        if created:
            return redirect('mybookingshowroom')  
        else:
            alert="<script>alert('already booked'); window.location.href='/s_book_services/';</script>"
            return HttpResponse(alert)
    return render(request, 's_booknow_services.html', {'services': services,'user':user})

def mybookingshowroom(request):
    email=request.session.get('email')
    user=models.user.objects.get(email=email)
    bookings=models.Bookingshowroom.objects.filter(user=user)
    return render(request, 'mybookingshowroom.html',{'bookings':bookings})


def listshowbookings(request, wid):
    services = models.S_services.objects.get(id=wid)
    bookings = models.Bookingshowroom.objects.filter(services=services)
    
    for booking in bookings:
        # Assuming booking.date is a datetime.date object, convert it to datetime if necessary
        booking_date = booking.date

        # Convert the booking's date to datetime (set the time to midnight)
        booking_datetime = datetime.combine(booking_date, datetime.min.time())
        
        # Get the current datetime
        current_datetime = datetime.now()

        # Compare the datetime objects
        if booking_datetime < current_datetime:
            # Handle your logic here (e.g., automatically reject after 2 minutes)
            pass

    return render(request, 'listshowbookings.html', {'bookings': bookings})

def approveinsterestedshowrooms(request,bid):
    booking=models.Bookingshowroom.objects.get(id=bid)
    user=booking.user
    services=booking.services
    status='approved'
    booking.approval_status='approved'
    booking.save()
    models.Approvedshowroomss(user=user,services=services,status=status).save()
    alert_message = f"""
    <script>
        alert('The Person is approved');
        window.location.href='/listshowbookings/{services.id}/';  // Redirect after alert
    </script>
    """
    return HttpResponse(alert_message)

def rejectinsterestedshowrooms(request,bid):
    booking=models.Bookingshowroom.objects.get(id=bid)
    user=booking.user
    services=booking.services
    status='reject'
    booking.approval_status='reject'
    booking.save()
    models.Approvedshowroomss(user=user,services=services,status=status).save()
    alert_message = f"""
    <script>
        alert('The Person is rejected');
        window.location.href='/listshowbookings/{services.id}/';  // Redirect after alert
    </script>
    """
    
    return HttpResponse(alert_message)

#TEST DRIVE 

def booknow_testdrive(request,test_id):
    semail = request.session.get('email')
    user=models.user.objects.get(email=semail)
    testdrive=models.showpost.objects.get(id=test_id)
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        date = request.POST.get('date')

       
        booking,created = Bookingtestdrive.objects.get_or_create(
            user=user,
            testdrive=testdrive,
            date=date
        )
        if created:
            return redirect('mybookingtestdrive')  
        else:
            alert="<script>alert('already booked'); window.location.href='/s_book_services/';</script>"
            return HttpResponse(alert)
    return render(request, 'booknow_testdrive.html', {'testdrive': testdrive,'user':user})

def mybookingtestdrive(request):
    email=request.session.get('email')
    user=models.user.objects.get(email=email)
    bookings=models.Bookingtestdrive.objects.filter(user=user)
    return render(request, 'mybookingtestdrive.html',{'bookings':bookings})


def listtestdrive(request, tid):
    testdrive = models.showpost.objects.get(id=tid)
    bookings = models.Bookingtestdrive.objects.filter(testdrive=testdrive)
    
    for booking in bookings:
        # Assuming booking.date is a datetime.date object, convert it to datetime if necessary
        booking_date = booking.date

        # Convert the booking's date to datetime (set the time to midnight)
        booking_datetime = datetime.combine(booking_date, datetime.min.time())
        
        # Get the current datetime
        current_datetime = datetime.now()

        # Compare the datetime objects
        if booking_datetime < current_datetime:
            # Handle your logic here (e.g., automatically reject after 2 minutes)
            pass

    return render(request, 'listtestdrive.html', {'bookings': bookings})

def approveinsterestedtestdrivers(request,bid):
    booking=models.Bookingtestdrive.objects.get(id=bid)
    user=booking.user
    testdrive=booking.testdrive
    status='approved'
    booking.approval_status='approved'
    booking.save()
    models.Approvedtestdrive(user=user,testdrive=testdrive,status=status).save()
    alert_message = f"""
    <script>
        alert('The Person is approved');
        window.location.href='/listtestdrive/{testdrive.id}/';  // Redirect after alert
    </script>
    """
    return HttpResponse(alert_message)

def rejectinsterestedtestdrivers(request,bid):
    booking=models.Bookingtestdrive.objects.get(id=bid)
    user=booking.user
    testdrive=booking.testdrive
    status='reject'
    booking.approval_status='reject'
    booking.save()
    models.Approvedtestdrive(user=user,testdrive=testdrive,status=status).save()
    alert_message = f"""
    <script>
        alert('The Person is rejected');
        window.location.href='/listtestdrive/{testdrive.id}/';  // Redirect after alert
    </script>
    """
    
    return HttpResponse(alert_message)

#Show Posts
def showposts(request):
    semail=request.session.get('email')
    show=models.show.objects.get(email=semail)
    if request.method=="POST":
        brand=request.POST.get('brand')
        model=request.POST.get('model')
        price = request.POST.get('price')  
        location = request.POST.get('location')
        description=request.POST.get('description')
        image = request.FILES.get('image')   
        showposts = models.showpost(show=show,brand=brand,model=model,price=price,location=location,description=description,image=image)
        showposts.save()
        return redirect('showpostslist')
    return render(request,'showposts.html')
    
def showpostslist(request):
    semail=request.session.get('email')
    show=models.show.objects.get(email=semail)
    u=showpost.objects.filter(show=show)
    return render(request,'showpostslist.html',{'show':u})
 
    
def delshowposts(request,id):
    d=showpost.objects.get(id=id)
    d.delete()
    return redirect('showpostslist') 

def edit_showposts(request, id):
    showposts = showpost.objects.get(id=id)

    if request.method == 'POST':
        showposts.brand = request.POST.get('brand')
        showposts.model = request.POST.get('model')
        showposts.price = request.POST.get('price')
        showposts.location = request.POST.get('location')
        showposts.description = request.POST.get('description')

        if 'image' in request.FILES:
            showposts.image = request.FILES['image']
        
        showposts.save()  
        return redirect('showpostslist')  

    return render(request, 'edit_showposts.html', {'showposts': showposts})

def showpostsview(request):
    semail=request.session.get('email')
    show=models.show.objects.get(email=semail)
    showposts=showpost.objects.exclude(show=show)
    return render(request,'showpostsview.html',{'showposts':showposts})

def showpostslistu(request,id):
    show=models.show.objects.get(id=id)
    showpost=models.showpost.objects.filter(show=show)
    return render(request,'showpostslistu.html',{'showposts':showpost})




def sparereg(request):
    if request.method=="POST":
        Sparepartsname=request.POST.get("sparename")
        Email=request.POST.get("email")
        Password=request.POST.get("password")
        Phonenumber=request.POST.get("phonenumber")
        Address=request.POST.get("spareaddress")
        Registration=request.POST.get("spareregno")
        Image=request.FILES.get("image")
        if user.objects.filter(email=Email).exists():
            return HttpResponse("<script>alert('This email already exists'); window.location.href='/sparereg';</script>")
        class2=models.spare(sparename=Sparepartsname,email=Email,password=Password,phonenumber=Phonenumber,spareaddress=Address,spareregno=Registration,image=Image,status='applied').save()
        return redirect('sparelogin')
    return render(request,'sparereg.html')

def sparelogin(request):
    if request.method == "POST":
        Email = request.POST.get("email")
        Password = request.POST.get("password")

        try:
            us = models.spare.objects.get(email=Email, password=Password)
            if us.status == 'approved':
                request.session['email'] = us.email
                return redirect('sparehome')
            else:
                return HttpResponse("<script>alert('Your account is not yet approved. Please wait until the admin approves your registration.'); window.location.href='/sparelogin';</script>")
        except models.spare.DoesNotExist:
            return HttpResponse("<script>alert('Invalid email or password'); window.location.href='/sparelogin';</script>")

    return render(request, 'sparelogin.html')

def sparelist(request):
    u=spare.objects.all()
    return render(request,'sparelist.html',{'spare':u})
    # Create your views here.
def delspare(request,id):
    d=spare.objects.get(id=id)
    d.delete()
    return redirect('sparelist')


def spareprofile(request):
    email=request.session['email']
    cr=spare.objects.get(email=email)
    sparename=cr.sparename
    email=cr.email
    image=cr.image
    phonenumber=cr.phonenumber
    spareaddress=cr.spareaddress
    spareregno=cr.spareregno
           
    return render(request,'spareprofile.html',{'sparename':sparename,'email':email,'image':image,'phonenumber':phonenumber,'spareaddress':spareaddress,'spareregno':spareregno})

def sp_updateprou(request):
    email=request.session['email']
    cr=spare.objects.get(email=email)
    if cr:
        user_info={'sparename':cr.sparename,'email':cr.email,'phonenumber':cr.phonenumber,'password':cr.password,'spareaddress':cr.spareaddress,'spareregno':cr.spareregno,'image':cr.image}
        return render(request,'sp_updateprou.html',user_info)
    else:
        return render(request,'sp_updateprou.html')
    
def sp_proupdateu(request):
    email=request.session['email']
    if request.method=='POST':
        sparename=request.POST.get('sparename')
        email=request.POST.get('email')
        password=request.POST.get('password')
        phonenumber=request.POST.get('phonenumber')
        spareaddress=request.POST.get('spareaddress')
        spareregno=request.POST.get('spareregno')
        image=request.POST.get('image')
        data=spare.objects.get(email=email)
        data.sparename=sparename
        data.email=email
        data.phonenumber=phonenumber
        data.password=password
        data.spareaddress=spareaddress
        data.spareregno=spareregno
        if image:
            data.image=image
        data.save()
        cr=spare.objects.get(email=email)
        if cr:
                user_info={'sparename':cr.sparename,'email':cr.email,'phonenumber':cr.phonenumber,'password':cr.password,'spareaddress':cr.spareaddress,'spareregno':cr.spareregno,'image':cr.image}
                return render(request,'spareprofile.html',user_info)
        else:
                return render(request,'sp_updateprou.html')
    return render(request,'sp_updateprou.html')

def sparehome(request):
    return render(request,'sparehome.html')

def splogout(request):
    logout(request)  
    return redirect('index') 

def alogout(request):
    logout(request)  # This logs the admin out
    return redirect('index') 

def spareposts(request):
    semail=request.session.get('email')
    spare=models.spare.objects.get(email=semail)
    if request.method=="POST":
        productname=request.POST.get('productname')
        price = request.POST.get('price')  
        location = request.POST.get('location')
        description=request.POST.get('description')
        image = request.FILES.get('image')   
        spareposts = models.sparepost(spare=spare,productname=productname,price=price,location=location,description=description,image=image)
        spareposts.save()
        return redirect('sparepostslist')
    return render(request,'spareposts.html')
    
def sparepostslist(request):
    semail=request.session.get('email')
    spare=models.spare.objects.get(email=semail)
    u=sparepost.objects.filter(spare=spare)
    return render(request,'sparepostslist.html',{'spare':u})
    # Create your views here.
    
def delspareposts(request,id):
    d=sparepost.objects.get(id=id)
    d.delete()
    return redirect('sparepostslist') 

def edit_spareposts(request, id):
    spareposts = sparepost.objects.get(id=id)

    if request.method == 'POST':
        spareposts.productname = request.POST.get('productname')
        spareposts.price = request.POST.get('price')
        spareposts.location = request.POST.get('location')
        spareposts.description = request.POST.get('description')

        if 'image' in request.FILES:
            spareposts.image = request.FILES['image']
        
        spareposts.save()  
        return redirect('sparepostslist')  

    return render(request, 'edit_spareposts.html', {'spareposts': spareposts})

def sparepostsview(request):
    semail=request.session.get('email')
    spare=models.spare.objects.get(email=semail)
    spareposts=sparepost.objects.exclude(spare=spare)
    return render(request,'sparepostsview.html',{'spareposts':spareposts})

def sparepostslistu(request,id):
    spare=models.spare.objects.get(id=id)
    sparepost=models.sparepost.objects.filter(spare=spare)
    return render(request,'sparepostslistu.html',{'spareposts':sparepost})

def sparepostslistw(request,id):
    spare=models.spare.objects.get(id=id)
    sparepost=models.sparepost.objects.filter(spare=spare)
    return render(request,'sparepostslistw.html',{'spareposts':sparepost})


def updateprou(request):
    email=request.session['email']
    cr=user.objects.get(email=email)
    if request.method=="POST":
        bio=request.POST.get("bio")
        class1=models.user(bio=bio).save() 
    if cr:
        user_info={'username':cr.username,'email':cr.email,'phonenumber':cr.phonenumber,'password':cr.password,'place':cr.place,'pincode':cr.pincode,'image':cr.image,'bio':cr.bio}
        return render(request,'updateprou.html',user_info)
    else:
        return render(request,'updateprou.html')
    
def proupdateu(request):
    email=request.session['email']
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        bio=request.POST.get('bio')
        phonenumber=request.POST.get('phonenumber')
        password=request.POST.get('password')
        place=request.POST.get('place')
        pincode=request.POST.get('pincode')
        image=request.POST.get('image')
        data=user.objects.get(email=email)
        data.username=username
        data.email=email
        data.phonenumber=phonenumber
        data.password=password
        data.place=place
        data.pincode=pincode
        if image:
            data.image=image
        data.save()
        cr=user.objects.get(email=email)
        if cr:
                user_info={'username':cr.username,'email':cr.email,'bio':cr.bio,'phonenumber':cr.phonenumber,'password':cr.password,'place':cr.place,'pincode':cr.pincode,'image':cr.image}
                return render(request,'updateprou.html',user_info)
        else:
                return render(request,'updateprou.html')
    return render(request,'updateprou.html')

def adminlogin(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password') 
        u='admin@gmail.com'
        p='admin'
        if email==u:
            if password==p:
                return redirect('adminindex')
        
    return render(request,'adminlogin.html')

# def adminhome(request):
#     return render(request,'adminhome.html')    

def userfeedback_rate(request):
    if request.method == "POST":
        feedback_text = request.POST.get('feedback_text')
        rating = request.POST.get('rating')
        if not feedback_text or not rating:
            # Handle missing fields
            alert_message = "<script>alert('Please fill in all required fields.'); window.location.href='/userfeedback_rate';</script>"
            return HttpResponse(alert_message)
        try:
            rating = int(rating)
            if rating not in [1, 2, 3, 4, 5]:
                raise ValueError("Invalid rating value")
        except (ValueError, TypeError):
            # Handle invalid rating
            alert_message = "<script>alert('Invalid rating value. Please select a valid rating.'); window.location.href='/userfeedback_rate';</script>"
            return HttpResponse(alert_message)
        # Create and save the Feedback instance
        feedbacks = feedback(
            feedback_text=feedback_text,
            rating=rating
        )
        feedbacks.save()
        # Redirect to a success page
        return redirect('userfeedback_success')
    else:
        # Render the feedback form
        return render(request, 'userfeedback_rate.html')

def userfeedback_success(request):
    return render(request, 'userfeedback_success.html')

def workfeedback_rate(request):
    if request.method == "POST":
        feedback_text = request.POST.get('feedback_text')
        rating = request.POST.get('rating')
        if not feedback_text or not rating:
            # Handle missing fields
            alert_message = "<script>alert('Please fill in all required fields.'); window.location.href='/workfeedback_rate';</script>"
            return HttpResponse(alert_message)
        try:
            rating = int(rating)
            if rating not in [1, 2, 3, 4, 5]:
                raise ValueError("Invalid rating value")
        except (ValueError, TypeError):
            # Handle invalid rating
            alert_message = "<script>alert('Invalid rating value. Please select a valid rating.'); window.location.href='/workfeedback_rate';</script>"
            return HttpResponse(alert_message)
        # Create and save the Feedback instance
        feedbacks = feedback(
            feedback_text=feedback_text,
            rating=rating
        )
        feedbacks.save()
        # Redirect to a success page
        return redirect('workfeedback_success')
    else:
        # Render the feedback form
        return render(request, 'workfeedback_rate.html')

def workfeedback_success(request):
    return render(request, 'workfeedback_success.html')

def showfeedback_rate(request):
    if request.method == "POST":
        feedback_text = request.POST.get('feedback_text')
        rating = request.POST.get('rating')
        if not feedback_text or not rating:
            # Handle missing fields
            alert_message = "<script>alert('Please fill in all required fields.'); window.location.href='/showfeedback_rate';</script>"
            return HttpResponse(alert_message)
        try:
            rating = int(rating)
            if rating not in [1, 2, 3, 4, 5]:
                raise ValueError("Invalid rating value")
        except (ValueError, TypeError):
            # Handle invalid rating
            alert_message = "<script>alert('Invalid rating value. Please select a valid rating.'); window.location.href='/showfeedback_rate';</script>"
            return HttpResponse(alert_message)
        # Create and save the Feedback instance
        feedbacks = feedback(
            feedback_text=feedback_text,
            rating=rating
        )
        feedbacks.save()
        # Redirect to a success page
        return redirect('showfeedback_success')
    else:
        # Render the feedback form
        return render(request, 'showfeedback_rate.html')

def showfeedback_success(request):
    return render(request, 'showfeedback_success.html')

def sparefeedback_rate(request):
    if request.method == "POST":
        feedback_text = request.POST.get('feedback_text')
        rating = request.POST.get('rating')
        if not feedback_text or not rating:
            # Handle missing fields
            alert_message = "<script>alert('Please fill in all required fields.'); window.location.href='/sparefeedback_rate';</script>"
            return HttpResponse(alert_message)
        try:
            rating = int(rating)
            if rating not in [1, 2, 3, 4, 5]:
                raise ValueError("Invalid rating value")
        except (ValueError, TypeError):
            # Handle invalid rating
            alert_message = "<script>alert('Invalid rating value. Please select a valid rating.'); window.location.href='/sparefeedback_rate';</script>"
            return HttpResponse(alert_message)
        # Create and save the Feedback instance
        feedbacks = feedback(
            feedback_text=feedback_text,
            rating=rating
        )
        feedbacks.save()
        # Redirect to a success page
        return redirect('sparefeedback_success')
    else:
        # Render the feedback form
        return render(request, 'sparefeedback_rate.html')

def sparefeedback_success(request):
    return render(request, 'sparefeedback_success.html')

def feedbacklist(request):
    u=feedback.objects.all()
    return render(request,'feedbacklist.html',{'feedback':u})

def delfeedback(request,id):
    d=feedback.objects.get(id=id)
    d.delete()
    return redirect('feedbacklist')

def adminindex(request):
    return render(request,'adminindex.html')

def user_showlist(request):
    showrooms = show.objects.all()
    return render(request, 'user_showlist.html', {'showrooms': showrooms})

def user_worklist(request):
    workshop = work.objects.all()
    return render(request, 'user_worklist.html', {'workshop': workshop})

def user_sparelist(request):
    spareparts = spare.objects.all()
    return render(request, 'user_sparelist.html', {'spareparts': spareparts})

def work_sparelist(request):
    spareparts = spare.objects.all()
    return render(request, 'work_sparelist.html', {'spareparts': spareparts})


from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.conf import settings

def send_status_email(email, status):
    """Send an email notification based on the status update."""
    subject = "Application Status Update"
    
    if status == "approved":
        message = f"Dear User,\n\nYour account has been approved. You can now log in.\n\nRegards,\nTeam"
    elif status == "rejected":
        message = f"Dear User,\n\nWe regret to inform you that your application has been rejected.\n\nRegards,\nTeam"
    else:
        message = f"Dear User,\n\nYour application status has been updated to {status}.\n\nRegards,\nTeam"
    
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, ['carsbikes098@gmail.com'])

def update_status(request):
    if request.method == "POST":
        email = request.POST.get('email')
        status = request.POST.get('status')
        if not email or not status:
            return redirect('userlist')
        if status not in ['applied', 'approved', 'rejected']:
            return redirect('userlist')
        
        user_obj = get_object_or_404(user, email=email)
        user_obj.status = status
        user_obj.save()

        send_status_email(email, status)  # Send email notification
        return redirect('userlist')

def update_status2(request):
    if request.method == "POST":
        email = request.POST.get('email')
        status = request.POST.get('status')
        if not email or not status:
            return redirect('sparelist')
        if status not in ['applied', 'approved', 'rejected']:
            return redirect('sparelist')
        
        spare_obj = get_object_or_404(spare, email=email)
        spare_obj.status = status
        spare_obj.save()

        send_status_email(email, status)  # Send email notification
        return redirect('sparelist')

def update_status3(request):
    if request.method == "POST":
        email = request.POST.get('email')
        status = request.POST.get('status')
        if not email or not status:
            return redirect('worklist')
        if status not in ['applied', 'approved', 'rejected']:
            return redirect('worklist')
        
        work_obj = get_object_or_404(work, email=email)
        work_obj.status = status
        work_obj.save()

        send_status_email(email, status)  # Send email notification
        return redirect('worklist')

def update_status4(request):
    if request.method == "POST":
        email = request.POST.get('email')
        status = request.POST.get('status')
        if not email or not status:
            return redirect('showlist')
        if status not in ['applied', 'approved', 'rejected']:
            return redirect('showlist')
        
        show_obj = get_object_or_404(show, email=email)
        show_obj.status = status
        show_obj.save()

        send_status_email(email, status)  # Send email notification
        return redirect('showlist')

def carsell1(request):
    semail=request.session.get('email')
    user=models.user.objects.get(email=semail)
    if request.method=="POST":
        brand=request.POST.get('brand')
        model=request.POST.get('model')
        price = request.POST.get('price')  
        location = request.POST.get('location')
        varient=request.POST.get('variant')
        year=request.POST.get('year')
        fuel=request.POST.get('fuel')
        transmission=request.POST.get('transmission')
        km=request.POST.get('km')
        owner=request.POST.get('owner')
        discription=request.POST.get('description')
        image = request.FILES.get('image')   
        car = models.carsell(usr=user,brand=brand,model=model,price=price,location=location,variant=varient,year=year,fuel=fuel,transmission=transmission,km=km,owners=owner,description=discription,image=image)
        car.save()
        return redirect('carselllist')
    return render(request,'carsell.html')
    
def carselllist(request):
    semail=request.session.get('email')
    user=models.user.objects.get(email=semail)
    u=carsell.objects.filter(usr=user)
    return render(request,'carselllist.html',{'user':u})
    # Create your views here.
    
def deluser1(request,id):
    d=carsell.objects.get(id=id)
    d.delete()
    return redirect('carselllist') 


def edit_car(request, id):
    car = carsell.objects.get(id=id)

    if request.method == 'POST':
        car.brand = request.POST.get('brand')
        car.model = request.POST.get('model')
        car.price = request.POST.get('price')
        car.location = request.POST.get('location')
        car.variant = request.POST.get('variant')
        car.year = request.POST.get('year')
        car.fuel = request.POST.get('fuel')
        car.transmission = request.POST.get('transmission')
        car.km = request.POST.get('km')
        car.owners = request.POST.get('owners')
        car.description = request.POST.get('description')

        if 'image' in request.FILES:
            car.image = request.FILES['image']
        
        car.save()  
        return redirect('carselllist')  

    return render(request, 'carselllist_edit.html', {'car': car})

def bookcarsell(request):
    semail=request.session.get('email')
    user=models.user.objects.get(email=semail)
    car=carsell.objects.exclude(usr=user)
    return render(request,'bookcarsell.html',{'car':car})

def booknowcarsell(request, id):
    semail = request.session.get('email')
    user=models.user.objects.get(email=semail)
    car = carsell.objects.get(id=id)
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        date = request.POST.get('date')

       
        booking,created = BookingCarsell.objects.get_or_create(
            user=user,
            car=car,
            date=date
        )
        if created:
            return redirect('mybookingcar_S')  
        else:
            alert="<script>alert('already booked'); window.location.href='/bookcarsell/';</script>"
            return HttpResponse(alert)
    return render(request, 'booknowcarsell.html', {'car': car,'user':user})

def mybookingcar_S(request):
    email=request.session.get('email')
    user=models.user.objects.get(email=email)
    bookings=models.BookingCarsell.objects.filter(user=user)
    return render(request, 'mybookingcar_S.html',{'bookings':bookings,'RAZOR_KEY_ID': settings.RAZOR_KEY_ID})

from datetime import datetime

def listcarbuyers(request, cid):
    car = models.carsell.objects.get(id=cid)
    bookings = models.BookingCarsell.objects.filter(car=car)
    
    for booking in bookings:
        # Assuming booking.date is a datetime.date object, convert it to datetime if necessary
        booking_date = booking.date

        # Convert the booking's date to datetime (set the time to midnight)
        booking_datetime = datetime.combine(booking_date, datetime.min.time())
        
        # Get the current datetime
        current_datetime = datetime.now()

        # Compare the datetime objects
        if booking_datetime < current_datetime:
            # Handle your logic here (e.g., automatically reject after 2 minutes)
            pass

    return render(request, 'listcarbuyers.html', {'bookings': bookings})


def approveinsterestedbuyers(request,bid):
    booking=models.BookingCarsell.objects.get(id=bid)
    buyer=booking.user
    car=booking.car
    status='approved'
    booking.approval_status='approved'
    booking.save()
    models.Approvedcarbuyers(buyer=buyer,car=car,status=status).save()
    alert_message = f"""
    <script>
        alert('The buyer is approved');
        window.location.href='/listcarbuyers/{car.id}/';  // Redirect after alert
    </script>
    """
    
    return HttpResponse(alert_message)

def rejectinsterestedbuyers(request,bid):
    booking=models.BookingCarsell.objects.get(id=bid)
    buyer=booking.user
    car=booking.car
    status='reject'
    booking.approval_status='reject'
    booking.save()
    models.Approvedcarbuyers(buyer=buyer,car=car,status=status).save()
    alert_message = f"""
    <script>
        alert('The buyer is rejected');
        window.location.href='/listcarbuyers/{car.id}/';  // Redirect after alert
    </script>
    """
    
    return HttpResponse(alert_message)

    

def bikesell1(request):
    semail=request.session.get('email')
    user=models.user.objects.get(email=semail)
    if request.method=="POST":
        brand=request.POST.get('brand')
        model=request.POST.get('model')
        price=request.POST.get('price')
        location=request.POST.get('location')
        year=request.POST.get('year')
        fuel=request.POST.get('fuel')
        km=request.POST.get('km')
        owners=request.POST.get('owners')
        description=request.POST.get('description')
        image=request.FILES.get('image')    
        bike=models.bikesell(usr=user,brand=brand,model=model,price=price,location=location,year=year,fuel=fuel,km=km,owners=owners,description=description,image=image)
        bike.save()
        return redirect('bikeselllist')
    return render(request,'bikesell.html')

def bikeselllist(request):
    semail=request.session.get('email')
    user=models.user.objects.get(email=semail)
    u=bikesell.objects.filter(usr=user)
    return render(request,'bikeselllist.html',{'user':u})
    # Create your views here.
    
def deluser2(request,id):
    d=bikesell.objects.get(id=id)
    d.delete()
    return redirect('bikeselllist')
    
def edit_bike(request, id):
    bike = bikesell.objects.get(id=id)

    if request.method == 'POST':
        bike.brand = request.POST.get('brand')
        bike.model = request.POST.get('model')
        bike.price = request.POST.get('price')
        bike.location = request.POST.get('location')
        bike.year = request.POST.get('year')
        bike.fuel = request.POST.get('fuel')
        bike.km = request.POST.get('km')
        bike.owners = request.POST.get('owners')
        bike.description = request.POST.get('description')

        if 'image' in request.FILES:
            bike.image = request.FILES['image']
        
        bike.save()  
        return redirect('bikeselllist')  

    return render(request, 'bikeselllist_edit.html', {'bike': bike})

def bookbikesell(request):
    semail=request.session.get('email')
    user=models.user.objects.get(email=semail)
    bike=bikesell.objects.exclude(usr=user)
    return render(request,'bookbikesell.html',{'bike':bike})

def booknowbikesell(request, id):
    semail = request.session.get('email')
    user=models.user.objects.get(email=semail)
    bike = bikesell.objects.get(id=id)
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        date = request.POST.get('date')

       
        booking,created = BookingBikesell.objects.get_or_create(
            user=user,
            bike=bike,
            date=date
        )
        if created:
            return redirect('mybookingbike_S')  
        else:
            alert="<script>alert('already booked'); window.location.href='/bookbikesell/';</script>"
            return HttpResponse(alert)
    return render(request, 'booknowbikesell.html', {'bike': bike,'user':user})

def mybookingbike_S(request):
    email=request.session.get('email')
    user=models.user.objects.get(email=email)
    bookings=models.BookingBikesell.objects.filter(user=user)
    return render(request, 'mybookingbike_S.html',{'bookings':bookings,'RAZOR_KEY_ID': settings.RAZOR_KEY_ID})

def listbikebuyers(request, bike_id):
    bike = models.bikesell.objects.get(id=bike_id)
    bookings = models.BookingBikesell.objects.filter(bike=bike)
    
    for booking in bookings:
        # Assuming booking.date is a datetime.date object, convert it to datetime if necessary
        booking_date = booking.date

        # Convert the booking's date to datetime (set the time to midnight)
        booking_datetime = datetime.combine(booking_date, datetime.min.time())
        
        # Get the current datetime
        current_datetime = datetime.now()

        # Compare the datetime objects
        if booking_datetime < current_datetime:
            # Handle your logic here (e.g., automatically reject after 2 minutes)
            pass

    return render(request, 'listbikebuyers.html', {'bookings': bookings})

def approveinsterestedbikebuyers(request,bid):
    booking=models.BookingBikesell.objects.get(id=bid)
    buyer=booking.user
    bike=booking.bike
    status='approved'
    booking.approval_status='approved'
    booking.save()
    models.Approvedbikebuyers(buyer=buyer,bike=bike,status=status).save()
    alert_message = f"""
    <script>
        alert('The buyer is approved');
        window.location.href='/listbikebuyers/{bike.id}/';  // Redirect after alert
    </script>
    """
    return HttpResponse(alert_message)

def rejectinsterestedbikebuyers(request,bid):
    booking=models.BookingBikesell.objects.get(id=bid)
    buyer=booking.user
    bike=booking.bike
    status='reject'
    booking.approval_status='reject'
    booking.save()
    models.Approvedcarbuyers(buyer=buyer,bike=bike,status=status).save()
    alert_message = f"""
    <script>
        alert('The buyer is rejected');
        window.location.href='/listbikebuyers/{bike.id}/';  // Redirect after alert
    </script>
    """
    
    return HttpResponse(alert_message)

def carrent1(request):
    semail=request.session.get('email')
    user=models.user.objects.get(email=semail)
    if request.method=="POST":
        brand=request.POST.get('brand')
        model=request.POST.get('model')
        year=request.POST.get('year')
        fuel=request.POST.get('fuel')
        km=request.POST.get('km')
        owner=request.POST.get('owner')
        rentamount=request.POST.get('rentamount')
        description=request.POST.get('description')
        image=request.FILES.get('image')    
        car=models.carrent(usr=user,brand=brand,model=model,year=year,fuel=fuel,km=km,owner=owner,rentamount=rentamount,description=description,image=image).save()
        return redirect('carrentlist')
    return render(request,'carrent.html')

def carrentlist(request):
    email=request.session.get('email')
    user=models.user.objects.get(email=email)
    u=carrent.objects.filter(usr=user)
    return render(request,'carrentlist.html',{'user':u})
   

def deluser3(request,id):
    d=carrent.objects.get(id=id)
    d.delete()
    return redirect('carrentlist')    

def edit_car1(request, id):
    car = carrent.objects.get(id=id)

    if request.method == 'POST':
        car.brand = request.POST.get('brand')
        car.model = request.POST.get('model')
        car.year = request.POST.get('year')
        car.fuel = request.POST.get('fuel')
        car.km = request.POST.get('km')
        car.owner = request.POST.get('owner')
        car.rentamount=request.POST.get('rentamount')
        car.description = request.POST.get('description')
        if 'image' in request.FILES:
            car.image = request.FILES['image']
        
        car.save()  
        return redirect('carrentlist')  

    return render(request, 'carrentlist_edit.html', {'car': car})

def bookcarrent(request):
    semail=request.session.get('email')
    user=models.user.objects.get(email=semail)
    car=carrent.objects.exclude(usr=user)
    return render(request,'bookcarrent.html',{'car':car})

def listcarrenters(request, car_id):
    car = models.carrent.objects.get(id=car_id)
    bookings = models.BookingCarRent.objects.filter(car=car)
    
    for booking in bookings:
        # Assuming booking.date is a datetime.date object, convert it to datetime if necessary
        booking_startdate = booking.startdate

        # Convert the booking's date to datetime (set the time to midnight)
        booking_datetime = datetime.combine(booking_startdate, datetime.min.time())
        
        # Get the current datetime
        current_datetime = datetime.now()

        # Compare the datetime objects
        if booking_datetime < current_datetime:
            # Handle your logic here (e.g., automatically reject after 2 minutes)
            pass

    return render(request, 'listcarrenters.html', {'bookings': bookings})

def approveinsterestedrenters(request,bid):
    booking=models.BookingCarRent.objects.get(id=bid)
    buyer=booking.user
    car=booking.car
    status='approved'
    booking.approval_status='approved'
    booking.save()
    models.Approvedcarrenters(buyer=buyer,car=car,status=status).save()
    alert_message = f"""
    <script>
        alert('The buyer is approved');
        window.location.href='/listcarrenters/{car.id}/';  // Redirect after alert
    </script>
    """
    
    return HttpResponse(alert_message)

def rejectinsterestedrenters(request,bid):
    booking=models.BookingCarRent.objects.get(id=bid)
    buyer=booking.user
    car=booking.car
    status='reject'
    booking.approval_status='reject'
    booking.save()
    models.Approvedcarrenters(buyer=buyer,car=car,status=status).save()
    alert_message = f"""
    <script>
        alert('The buyer is rejected');
        window.location.href='/listcarrenters/{car.id}/';  // Redirect after alert
    </script>
    """
    
    return HttpResponse(alert_message)



from django.shortcuts import redirect, get_object_or_404
from .models import carrent

def set_availability(request, id):
    car = get_object_or_404(carrent, id=id)
    
    # Toggle availability between 'Available' and 'Unavailable'
    if car.availability == 'Available':
        car.availability = 'Unavailable'
    else:
        car.availability = 'Available'
    
    car.save()
    
    return redirect('carrentlist')  # Replace 'car_list' with your actual URL name

def set_availability1(request, id):
    bike = get_object_or_404(bikerent, id=id)
    
    # Toggle availability between 'Available' and 'Unavailable'
    if bike.availability == 'Available':
        bike.availability = 'Unavailable'
    else:
        bike.availability = 'Available'
    
    bike.save()
    
    return redirect('bikerentlist')  # Replace 'car_list' with your actual URL name



from datetime import datetime

def booknowcarrent(request, id):
    car = get_object_or_404(carrent, id=id)
    
    semail = request.session.get('email')  # Get email from session
    user_obj = get_object_or_404(user, email=semail)  # Fetch user from DB

    if request.method == 'POST':
        rentalperiod_start = request.POST.get('rentalperiod_start')
        rentalperiod_end = request.POST.get('rentalperiod_end')

        # Convert string dates to datetime objects
        start_date = datetime.strptime(rentalperiod_start, '%Y-%m-%d')
        end_date = datetime.strptime(rentalperiod_end, '%Y-%m-%d')

        # Calculate day gap
        day_gap = (end_date - start_date).days

        # Ensure the rental period is valid
        if day_gap <= 0:
            return render(request, 'booknowcarrent.html', {'car': car, 'user': user_obj, 'error': 'Invalid rental period'})

        # Calculate total price
        total_price = car.rentamount * day_gap

        # Save booking details
        BookingCarRent.objects.create(
            user=user_obj,  # Assign the correct user object
            car=car,
            startdate=start_date,
            enddate=end_date,
            totalprice=total_price,
        )

        return redirect('mybookingcar_R')

    return render(request, 'booknowcarrent.html', {'car': car, 'user': user_obj})


def mybookingcar_R(request):
    email=request.session.get('email')
    user=models.user.objects.get(email=email)

    bookings=models.BookingCarRent.objects.filter(user=user)
    return render(request, 'mybookingcar_R.html',{'bookings':bookings,'RAZOR_KEY_ID': settings.RAZOR_KEY_ID})


def bikerent1(request):
    semail=request.session.get('email')
    user=models.user.objects.get(email=semail)
    if request.method=="POST":
        brand=request.POST.get('brand')
        model=request.POST.get('model')
        year=request.POST.get('year')
        fuel=request.POST.get('fuel')
        km=request.POST.get('km')
        owner=request.POST.get('owner')
        rentamount=request.POST.get('rentamount')
        description=request.POST.get('description')
        image=request.FILES.get('image')    
        class1=models.bikerent(usr=user,brand=brand,model=model,year=year,fuel=fuel,km=km,owner=owner,rentamount=rentamount,description=description,image=image).save()
        return redirect('bikerentlist')
    return render(request,'bikerent.html')

def bikerentlist(request):
    email=request.session.get('email')
    user=models.user.objects.get(email=email)
    u=bikerent.objects.filter(usr=user)
    return render(request,'bikerentlist.html',{'user':u})
   

def deluser4(request,id):
    d=bikerent.objects.get(id=id)
    d.delete()
    return redirect('bikerentlist')    

def edit_bike1(request, id):
    bike = bikerent.objects.get(id=id)

    if request.method == 'POST':
        bike.brand = request.POST.get('brand')
        bike.model = request.POST.get('model')
        bike.year = request.POST.get('year')
        bike.fuel = request.POST.get('fuel')
        bike.km = request.POST.get('km')
        bike.owner = request.POST.get('owner')
        bike.rentamount=request.POST.get('rentamount')
        bike.description = request.POST.get('description')

        if 'image' in request.FILES:
            bike.image = request.FILES['image']
        
        bike.save()  
        return redirect('bikerentlist')  

    return render(request, 'bikerentlist_edit.html', {'bike': bike})

def bookbikerent(request):
    semail=request.session.get('email')
    user=models.user.objects.get(email=semail)
    bike=bikerent.objects.exclude(usr=user)
    return render(request,'bookbikerent.html',{'bike':bike})

def listbikerenters(request, bike_id):
    bike = models.bikerent.objects.get(id=bike_id)
    bookings = models.BookingBikeRent.objects.filter(bike=bike)
    
    for booking in bookings:
        # Assuming booking.date is a datetime.date object, convert it to datetime if necessary
        booking_startdate = booking.startdate

        # Convert the booking's date to datetime (set the time to midnight)
        booking_datetime = datetime.combine(booking_startdate, datetime.min.time())
        
        # Get the current datetime
        current_datetime = datetime.now()

        # Compare the datetime objects
        if booking_datetime < current_datetime:
            # Handle your logic here (e.g., automatically reject after 2 minutes)
            pass

    return render(request, 'listbikerenters.html', {'bookings': bookings})


def approveinsterestedbikerenters(request,bid):
    booking=models.BookingBikeRent.objects.get(id=bid)
    buyer=booking.user
    bike=booking.bike
    status='approved'
    booking.approval_status='approved'
    booking.save()
    models.Approvedbikerenters(buyer=buyer,bike=bike,status=status).save()
    # alert="<script>alert('The buyer is approved')window.location.href='/listcarbuyers/'</script>"
    return redirect('listbikerenters',bike_id=bike.id)
    alert_message = f"""
    <script>
        alert('The buyer is approved');
        window.location.href='/listbikerenters/{bike.id}/';  // Redirect after alert
    </script>
    """
    return HttpResponse(alert_message)

def rejectinsterestedbikerenters(request,bid):
    booking=models.BookingBikerent.objects.get(id=bid)
    buyer=booking.user
    bike=booking.bike
    status='reject'
    booking.approval_status='reject'
    booking.save()
    models.Approvedbikerenters(buyer=buyer,bike=bike,status=status).save()
    alert_message = f"""
    <script>
        alert('The buyer is rejected');
        window.location.href='/listbikerenters/{bike.id}/';  // Redirect after alert
    </script>
    """
    
    return HttpResponse(alert_message)


from datetime import datetime

def booknowbikerent(request, id):
    bike = get_object_or_404(bikerent, id=id)
    
    semail = request.session.get('email')  # Get email from session
    user_obj = get_object_or_404(user, email=semail)  # Fetch user from DB

    if request.method == 'POST':
        rentalperiod_start = request.POST.get('rentalperiod_start')
        rentalperiod_end = request.POST.get('rentalperiod_end')

        # Convert string dates to datetime objects
        start_date = datetime.strptime(rentalperiod_start, '%Y-%m-%d')
        end_date = datetime.strptime(rentalperiod_end, '%Y-%m-%d')

        # Calculate day gap
        day_gap = (end_date - start_date).days

        # Ensure the rental period is valid
        if day_gap <= 0:
            return render(request, 'booknowbikerent.html', {'bike': bike, 'user': user_obj, 'error': 'Invalid rental period'})

        # Calculate total price
        total_price = bike.rentamount * day_gap

        # Save booking details
        BookingBikeRent.objects.create(
            user=user_obj,  # Assign the correct user object
            bike=bike,
            startdate=start_date,
            enddate=end_date,
            totalprice=total_price,
        )

        return redirect('mybookingbike_R')

    return render(request, 'booknowbikerent.html', {'bike': bike, 'user': user_obj})


def mybookingbike_R(request):
    email=request.session.get('email')
    user=models.user.objects.get(email=email)

    bookings=models.BookingBikeRent.objects.filter(user=user)
    return render(request, 'mybookingbike_R.html',{'bookings':bookings,'RAZOR_KEY_ID': settings.RAZOR_KEY_ID})


#Car Sell Payment
import razorpay
from django.http import JsonResponse
from django.shortcuts import redirect
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers.json import DjangoJSONEncoder
from decimal import Decimal
from . import models 
@csrf_exempt
def initiate_payment(request, cid):
    email = request.session.get('email')
    if email:
        try:
            car = models.carsell.objects.get(id=cid)
            am = car.price
            amount = int(am) * 100 
            client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))

            payment_order = client.order.create({
                'amount': amount, 
                'currency': 'INR', 
                'payment_capture': '1'
            })
            order_id = payment_order['id']
            user = models.user.objects.get(email=email)

            buyer_data = {
                'buyer': {
                    'id': user.id,
                    'name': user.username,
                    'email': user.email,
                    'phone': str(user.phonenumber),  
                    'product_dtls': car.id,
                }
            }

            response_data = {
                'order_id': order_id,
                'amount': amount,
            }
            response_data.update(buyer_data)

            return JsonResponse(response_data, encoder=DjangoJSONEncoder)

        except razorpay.errors.BadRequestError as e:
            return JsonResponse({'error': 'Bad Request: ' + str(e)}, status=400)
        except models.carsell.DoesNotExist:
            return JsonResponse({'error': 'Car not found'}, status=404)
        except models.user.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': 'Internal Error: ' + str(e)}, status=500)
    else:
        return JsonResponse({'error': 'User is not logged in'}, status=401)
@csrf_exempt
def confirm_payment(request, order_id, payment_id, crti_id):
    try:
        client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
        payment = client.payment.fetch(payment_id)

        if payment['order_id'] == order_id and payment['status'] == 'captured':
            pemail = payment.get('email')
            amount = payment.get('amount')
            crt_id = crti_id  

            if pemail:
                usr = models.user.objects.get(email=pemail)
                car = models.carsell.objects.get(id=crt_id) 
                amount_in_rupees = Decimal(amount) / Decimal(100)  

                trns = models.Car_selling_transactions(
                    user=usr,
                    car=car,
                    amount=amount_in_rupees,
                    order_id=order_id,
                    payment_status='Completed'
                )
                trns.save()
                booking = models.BookingCarsell.objects.filter(user=usr, car=car).first()               
                booking.delete()

                car.soldoutstatus='SOLDOUT'
                car.save()

               
                return redirect('home') 
                return JsonResponse({'status': 'failure', 'error': 'User email not found'}, status=400)
        else:
            return JsonResponse({'status': 'failure', 'error': 'Payment not captured or order mismatch'}, status=400)

    except razorpay.errors.BadRequestError as e:
        print('Error:', e)
        return JsonResponse({'status': 'failure', 'error': 'Bad Request'}, status=400)
    except models.user.DoesNotExist:
        return JsonResponse({'status': 'failure', 'error': 'User not found'}, status=404)
    except models.carsell.DoesNotExist:
        return JsonResponse({'status': 'failure', 'error': 'Car not found'}, status=404)
    except Exception as e:
        print('Error:', str(e))
        return JsonResponse({'status': 'failure', 'error': 'Internal Server Error'}, status=500)

#Bike Sell Payment
import razorpay
from django.http import JsonResponse
from django.shortcuts import redirect
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers.json import DjangoJSONEncoder
from decimal import Decimal
from . import models 
@csrf_exempt
def initiate_payment_bikesell(request,cid):
    email = request.session.get('email')
    if email:
        try:
            bike = models.bikesell.objects.get(id=cid)
            am = bike.price
            amount = int(am) * 100 
            client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
            payment_order = client.order.create({
                'amount': amount, 
                'currency': 'INR', 
                'payment_capture': '1'
            })
            order_id = payment_order['id']
            user = models.user.objects.get(email=email)
            buyer_data = {
                'buyer': {
                    'id': user.id,
                    'name': user.username,
                    'email': user.email,
                    'phone': str(user.phonenumber),  
                    'product_dtls': bike.id,
                }
            }
            response_data = {
                'order_id': order_id,
                'amount': amount,
            }
            response_data.update(buyer_data)
            return JsonResponse(response_data, encoder=DjangoJSONEncoder)
        except razorpay.errors.BadRequestError as e:
            return JsonResponse({'error': 'Bad Request: ' + str(e)}, status=400)
        except models.bikesell.DoesNotExist:
            return JsonResponse({'error': 'Car not found'}, status=404)
        except models.user.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': 'Internal Error: ' + str(e)}, status=500)
    else:
        return JsonResponse({'error': 'User is not logged in'}, status=401)
    
@csrf_exempt
def confirm_payment_bikesell(request, order_id, payment_id, crti_id):
    try:
        client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
        payment = client.payment.fetch(payment_id)

        if payment['order_id'] == order_id and payment['status'] == 'captured':
            pemail = payment.get('email')
            amount = payment.get('amount')
            crt_id = crti_id  

            if pemail:
                usr = models.user.objects.get(email=pemail)
                bike = models.bikesell.objects.get(id=crt_id)
                print('cf',bike) 
                amount_in_rupees = Decimal(amount) / Decimal(100)  

                trns = models.Bike_selling_transactions(
                    user=usr,
                    bike=bike,
                    amount=amount_in_rupees,
                    order_id=order_id,
                    payment_status='Completed'

                )
                trns.save()
                booking=models.BookingBikesell.objects.filter(user=usr,bike=bike).first()
                booking.delete()

                bike.soldoutstatus='SOLDOUT'
                bike.save()

                
                return redirect('home') 
        else:
            return JsonResponse({'status': 'failure', 'error': 'Payment not captured or order mismatch'}, status=400)

    except razorpay.errors.BadRequestError as e:
        print('Error:', e)
        return JsonResponse({'status': 'failure', 'error': 'Bad Request'}, status=400)
    except models.user.DoesNotExist:
        return JsonResponse({'status': 'failure', 'error': 'User not found'}, status=404)
    except models.bikesell.DoesNotExist:
        return JsonResponse({'status': 'failure', 'error': 'Car not found'}, status=404)
    except Exception as e:
        print('Error:', str(e))
        return JsonResponse({'status': 'failure', 'error': 'Internal Server Error'}, status=500)

# Car Rental payment
import razorpay
from django.http import JsonResponse
from django.shortcuts import redirect
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers.json import DjangoJSONEncoder
from decimal import Decimal
from . import models 
@csrf_exempt
def rent_initiate_payment(request,cid):
    email = request.session.get('email')
    if email:
        try:
            booking = models.BookingCarRent.objects.get(id=cid)
            am = booking.totalprice
            amount = int(am) * 100 
            client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))

            payment_order = client.order.create({
                'amount': amount, 
                'currency': 'INR', 
                'payment_capture': '1'
            })
            order_id = payment_order['id']
            user = models.user.objects.get(email=email)

            buyer_data = {
                'buyer': {
                    'id': user.id,
                    'name': user.username,
                    'email': user.email,
                    'phone': str(user.phonenumber),  
                    'product_dtls': booking.id,
                }
            }

            response_data = {
                'order_id': order_id,
                'amount': amount,
            }
            response_data.update(buyer_data)

            return JsonResponse(response_data, encoder=DjangoJSONEncoder)

        except razorpay.errors.BadRequestError as e:
            return JsonResponse({'error': 'Bad Request: ' + str(e)}, status=400)
        except models.carsell.DoesNotExist:
            return JsonResponse({'error': 'Car not found'}, status=404)
        except models.user.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': 'Internal Error: ' + str(e)}, status=500)
    else:
        return JsonResponse({'error': 'User is not logged in'}, status=401)
@csrf_exempt
def rent_confirm_payment(request, order_id, payment_id, book_id):
    try:
        client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
        payment = client.payment.fetch(payment_id)

        if payment['order_id'] == order_id and payment['status'] == 'captured':
            pemail = payment.get('email')
            amount = payment.get('amount')
            book_id = book_id  

            if pemail:
                usr = models.user.objects.get(email=pemail)
                booking = models.BookingCarRent.objects.filter(id=book_id).first()
                car=booking.car
                amount_in_rupees = Decimal(amount) / Decimal(100)  

                trns = models.Car_renting_transactions(
                    user=usr,
                    car=car,
                    amount=amount_in_rupees,
                    order_id=order_id,
                    payment_status='Completed'

                )
                trns.save()
                booking = models.BookingCarRent.objects.filter(user=usr, car=car).first()
                if booking:
                    booking.delete()


                

                return redirect('home') 
        else:
            return JsonResponse({'status': 'failure', 'error': 'Payment not captured or order mismatch'}, status=400)

    except razorpay.errors.BadRequestError as e:
        print('Error:', e)
        return JsonResponse({'status': 'failure', 'error': 'Bad Request'}, status=400)
    except models.user.DoesNotExist:
        return JsonResponse({'status': 'failure', 'error': 'User not found'}, status=404)
    except models.carrent.DoesNotExist:
        return JsonResponse({'status': 'failure', 'error': 'Car not found'}, status=404)
    except Exception as e:
        print('Error:', str(e))
        return JsonResponse({'status': 'failure', 'error': 'Internal Server Error'}, status=500)

#Bike Rental payment
import razorpay
import logging
from django.http import JsonResponse
from django.shortcuts import redirect
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from decimal import Decimal
from .models import user, BookingBikeRent, Bike_renting_transactions
logger = logging.getLogger(__name__)
@csrf_exempt
def rentbike_initiate_payment(request, cid):
    email = request.session.get('email')
    if not email:
        return JsonResponse({'error': 'User is not logged in'}, status=401)
    try:
        booking = BookingBikeRent.objects.get(id=cid)
        user_obj = user.objects.get(email=email)

        amount = int(booking.totalprice) * 100  # Convert to paise
        client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))

        payment_order = client.order.create({'amount': amount, 'currency': 'INR', 'payment_capture': '1'})

        return JsonResponse({
            'order_id': payment_order['id'],
            'amount': amount,
            'buyer': {
                'id': user_obj.id,
                'name': user_obj.username,
                'email': user_obj.email,
                'phone': str(user_obj.phonenumber),
                'product_dtls': booking.id,
            }
        })
    except BookingBikeRent.DoesNotExist:
        return JsonResponse({'error': 'Booking not found'}, status=404)
    except user.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)
    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
        return JsonResponse({'error': f'Internal Error: {e}'}, status=500)
@csrf_exempt
def rentbike_confirm_payment(request, order_id, payment_id, book_id):
    try:
        client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
        payment = client.payment.fetch(payment_id)

        # Validate payment details
        if payment.get('order_id') != order_id or payment.get('status') != 'captured':
            return JsonResponse({'status': 'failure', 'error': 'Payment not captured or order mismatch'}, status=400)

        # Fetch user email
        email = payment.get('email') or request.session.get('email')
        if not email:
            return JsonResponse({'status': 'failure', 'error': 'Email not provided'}, status=400)

        # Fetch user
        usr = user.objects.get(email=email)

        # Fix: Use filter().first() to avoid MultipleObjectsReturned error
        booking = BookingBikeRent.objects.filter(id=book_id).first()
        if not booking:
            return JsonResponse({'status': 'failure', 'error': 'Booking not found'}, status=404)

        # Convert amount to rupees
        amount_in_rupees = Decimal(payment.get('amount')) / 100

        # Create transaction record
        Bike_renting_transactions.objects.create(
            user=usr,
            bike=booking.bike,
            amount=amount_in_rupees,
            order_id=order_id,
            payment_status='Completed'
        )

        # Fix: Delete booking safely
        booking.delete()

        return redirect('home')

    except user.DoesNotExist:
        return JsonResponse({'status': 'failure', 'error': 'User not found'}, status=404)
    except Exception as e:
        logger.error(f'Unexpected Error: {e}')
        return JsonResponse({'status': 'failure', 'error': 'Internal Server Error'}, status=500)


#User Transaction History
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Car_selling_transactions, Car_renting_transactions, Bike_selling_transactions, Bike_renting_transactions
from django.contrib.auth.models import User


def transaction_history(request):
    # Get user email from session
    user_email = request.session.get('email')

    
    # Get user instance
    try:
        user_instance = user.objects.get(email=user_email)
    except User.DoesNotExist:
        return render(request, "error.html", {"message": "User not found."})

    # Fetch all transactions related to the user
    car_sales = Car_selling_transactions.objects.filter(user=user_instance)
    car_rentals = Car_renting_transactions.objects.filter(user=user_instance)
    bike_sales = Bike_selling_transactions.objects.filter(user=user_instance)
    bike_rentals = Bike_renting_transactions.objects.filter(user=user_instance)

    transactions = {
        "car_sales": car_sales,
        "car_rentals": car_rentals,
        "bike_sales": bike_sales,
        "bike_rentals": bike_rentals,
    }

    return render(request, "transaction_history.html", {"transactions": transactions})


# Fuel stations
import requests
from django.http import JsonResponse
from django.shortcuts import render

def get_nearby_fuel_stations(request):
    lat = request.GET.get("lat")
    lon = request.GET.get("lon")
    radius = 5000  # 5km radius

    if not lat or not lon:
        return JsonResponse({"error": "Latitude and Longitude required"}, status=400)

    # Overpass API query for fuel stations
    overpass_url = "https://overpass-api.de/api/interpreter"
    overpass_query = f"""
    [out:json];
    node["amenity"="fuel"](around:{radius},{lat},{lon});
    out body;
    """

    try:
        response = requests.get(overpass_url, params={"data": overpass_query}, timeout=10)
        response.raise_for_status()  # Ensure HTTP response is successful
        data = response.json()

        fuel_stations = []
        for element in data.get("elements", []):
            name = element.get("tags", {}).get("name", "Unnamed Fuel Station")
            lat, lon = element.get("lat"), element.get("lon")
            if lat and lon:
                fuel_stations.append({"name": name, "lat": lat, "lon": lon})

        if not fuel_stations:
            return JsonResponse({"stations": []})

        return JsonResponse({"stations": fuel_stations})

    except requests.exceptions.RequestException as e:
        print(f"Error fetching fuel station data: {e}")
        return JsonResponse({"error": "Failed to fetch fuel station data"}, status=500)

def show_map(request):
    return render(request, 'map.html')

import requests
from django.http import JsonResponse
from django.shortcuts import render

def get_nearby_workshops(request):
    lat = request.GET.get("lat")
    lon = request.GET.get("lon")
    radius = 5000  # 5km radius

    if not lat or not lon:
        return JsonResponse({"error": "Latitude and Longitude required"}, status=400)

    # Overpass API query for workshops
    overpass_url = "https://overpass-api.de/api/interpreter"
    overpass_query = f"""
    [out:json];
    node["amenity"="vehicle_repair"](around:{radius},{lat},{lon});
    out body;
    """

    try:
        response = requests.get(overpass_url, params={"data": overpass_query}, timeout=10)
        response.raise_for_status()  # Ensure HTTP response is successful
        data = response.json()

        workshops = []
        for element in data.get("elements", []):
            name = element.get("tags", {}).get("name", "Unnamed Workshop")
            lat, lon = element.get("lat"), element.get("lon")
            if lat and lon:
                workshops.append({"name": name, "lat": lat, "lon": lon})

        if not workshops:
            return JsonResponse({"workshops": []})

        return JsonResponse({"workshops": workshops})

    except requests.exceptions.RequestException as e:
        print(f"Error fetching workshop data: {e}")
        return JsonResponse({"error": "Failed to fetch workshop data"}, status=500)

def show_workshop_map(request):
    return render(request, 'workshop_map.html')






from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings
from .models import user
import random
import time

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = models.user.objects.get(email=email)
            otp = random.randint(100000, 999999)
            user.otp = otp
            user.save()

            subject = "Password Reset OTP"
            message = f"Your OTP for password reset is: {otp}"
            send_mail(subject, message, settings.EMAIL_HOST_USER, [email])

            request.session['reset_email'] = email
            request.session['otp_timestamp'] = time.time()

            return redirect('verify_otp')
        except models.user.DoesNotExist:
            return HttpResponse("<script>alert('Email not found'); window.location.href='/forgot-password/';</script>")
    return render(request, 'forgot_password.html')

def verify_otp(request):
    if request.method == 'POST':
        email = request.session.get('reset_email')
        otp_entered = request.POST.get('otp')
        otp_timestamp = request.session.get('otp_timestamp', 0)

        if time.time() - otp_timestamp > 30:
            return HttpResponse("<script>alert('OTP expired! Request a new one.'); window.location.href='/forgot-password/';</script>")
        try:
            user = models.user.objects.get(email=email)
            if str(user.otp) == otp_entered:
                return redirect('reset_password')
            else:
                return HttpResponse("<script>alert('Invalid OTP'); window.location.href='/verify-otp/';</script>")
        except models.user.DoesNotExist:
            return redirect('forgot_password')
    return render(request, 'verify_otp.html')

def reset_password(request):
    if request.method == 'POST':
        email = request.session.get('reset_email')
        new_password = request.POST.get('new_password')
        try:
            user = models.user.objects.get(email=email)
            user.password = new_password
            user.otp = None
            user.save()
            return HttpResponse("<script>alert('Password reset successful!'); window.location.href='/login/';</script>")
        except models.user.DoesNotExist:
            return redirect('forgot_password')
    return render(request, 'reset_password.html')
#work
def forgot_passwordw(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            work = models.work.objects.get(email=email)
            otp = random.randint(100000, 999999)
            work.otp = otp
            work.save()
            subject = "Password Reset OTP"
            message = f"Your OTP for password reset is: {otp}"
            send_mail(subject, message, settings.EMAIL_HOST_USER, [email])

            request.session['reset_email'] = email
            request.session['otp_timestamp'] = time.time()

            return redirect('verify_otpw')
        except models.user.DoesNotExist:
            return HttpResponse("<script>alert('Email not found'); window.location.href='/forgot-passwordw/';</script>")
    return render(request, 'forgot_passwordw.html')

def verify_otpw(request):
    if request.method == 'POST':
        email = request.session.get('reset_email')
        otp_entered = request.POST.get('otp')
        otp_timestamp = request.session.get('otp_timestamp', 0)

        if time.time() - otp_timestamp > 30:
            return HttpResponse("<script>alert('OTP expired! Request a new one.'); window.location.href='/forgot-passwordw/';</script>")
        try:
            work = models.work.objects.get(email=email)
            if str(work.otp) == otp_entered:
                return redirect('reset_passwordw')
            else:
                return HttpResponse("<script>alert('Invalid OTP'); window.location.href='/verify-otpw/';</script>")
        except models.work.DoesNotExist:
            return redirect('forgot_passwordw')
    return render(request, 'verify_otpw.html')

def reset_passwordw(request):
    if request.method == 'POST':
        email = request.session.get('reset_email')
        new_password = request.POST.get('new_password')
        try:
            work = models.work.objects.get(email=email)
            work.password = new_password
            work.otp = None
            work.save()
            return HttpResponse("<script>alert('Password reset successful!'); window.location.href='/worklogin/';</script>")
        except models.work.DoesNotExist:
            return redirect('forgot_passwordw')
    return render(request, 'reset_passwordw.html')

#show
def forgot_passwords(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            show = models.show.objects.get(email=email)
            otp = random.randint(100000, 999999)
            show.otp = otp
            show.save()

            subject = "Password Reset OTP"
            message = f"Your OTP for password reset is: {otp}"
            send_mail(subject, message, settings.EMAIL_HOST_USER, [email])

            request.session['reset_email'] = email
            request.session['otp_timestamp'] = time.time()

            return redirect('verify_otps')
        except models.show.DoesNotExist:
            return HttpResponse("<script>alert('Email not found'); window.location.href='/forgot-passwords/';</script>")
    return render(request, 'forgot_passwords.html')

def verify_otps(request):
    if request.method == 'POST':
        email = request.session.get('reset_email')
        otp_entered = request.POST.get('otp')
        otp_timestamp = request.session.get('otp_timestamp', 0)

        if time.time() - otp_timestamp > 30:
            return HttpResponse("<script>alert('OTP expired! Request a new one.'); window.location.href='/forgot-passwords/';</script>")
        try:
            show = models.show.objects.get(email=email)
            if str(show.otp) == otp_entered:
                return redirect('reset_passwords')
            else:
                return HttpResponse("<script>alert('Invalid OTP'); window.location.href='/verify-otps/';</script>")
        except models.show.DoesNotExist:
            return redirect('forgot_passwords')
    return render(request, 'verify_otps.html')

def reset_passwords(request):
    if request.method == 'POST':
        email = request.session.get('reset_email')
        new_password = request.POST.get('new_password')
        try:
            show = models.show.objects.get(email=email)
            show.password = new_password
            show.otp = None
            show.save()
            return HttpResponse("<script>alert('Password reset successful!'); window.location.href='/showlogin/';</script>")
        except models.show.DoesNotExist:
            return redirect('forgot_passwords')
    return render(request, 'reset_passwords.html')
#spare
def forgot_passwordsp(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            spare = models.spare.objects.get(email=email)
            otp = random.randint(100000, 999999)
            spare.otp = otp
            spare.save()

            subject = "Password Reset OTP"
            message = f"Your OTP for password reset is: {otp}"
            send_mail(subject, message, settings.EMAIL_HOST_USER, [email])

            request.session['reset_email'] = email
            request.session['otp_timestamp'] = time.time()

            return redirect('verify_otpsp')
        except models.spare.DoesNotExist:
            return HttpResponse("<script>alert('Email not found'); window.location.href='/forgot-passwordsp/';</script>")
    return render(request, 'forgot_passwordsp.html')

def verify_otpsp(request):
    if request.method == 'POST':
        email = request.session.get('reset_email')
        otp_entered = request.POST.get('otp')
        otp_timestamp = request.session.get('otp_timestamp', 0)

        if time.time() - otp_timestamp > 30:
            return HttpResponse("<script>alert('OTP expired! Request a new one.'); window.location.href='/forgot-passwordsp/';</script>")
        try:
            spare = models.spare.objects.get(email=email)
            if str(spare.otp) == otp_entered:
                return redirect('reset_passwordsp')
            else:
                return HttpResponse("<script>alert('Invalid OTP'); window.location.href='/verify-otpsp/';</script>")
        except models.spare.DoesNotExist:
            return redirect('forgot_passwordsp')
    return render(request, 'verify_otpsp.html')

def reset_passwordsp(request):
    if request.method == 'POST':
        email = request.session.get('reset_email')
        new_password = request.POST.get('new_password')
        try:
            spare = models.spare.objects.get(email=email)
            spare.password = new_password
            spare.otp = None
            spare.save()
            return HttpResponse("<script>alert('Password reset successful!'); window.location.href='/sparelogin/';</script>")
        except models.spare.DoesNotExist:
            return redirect('forgot_passwordsp')
    return render(request, 'reset_passwordsp.html')



from django.shortcuts import render, get_object_or_404
from .models import (
    Approvedcarbuyers, Approvedbikebuyers, Approvedcarrenters, Approvedbikerenters,
    Car_selling_transactions, Car_renting_transactions, 
    Bike_selling_transactions, Bike_renting_transactions, user
)

def approved_users_with_payment_status(request):
    # Ensure session email exists
    semail = request.session.get('email')
    if not semail:
        return render(request, 'error.html', {'message': 'User not logged in'})

    # Get the logged-in user
    logged_in_user = get_object_or_404(user, email=semail)

    # Fetch approved buyers and renters using optimized queries
    approved_car_buyers = Approvedcarbuyers.objects.filter(buyer=logged_in_user, status='approved').select_related('car')
    approved_bike_buyers = Approvedbikebuyers.objects.filter(buyer=logged_in_user, status='approved').select_related('bike')
    approved_car_renters = Approvedcarrenters.objects.filter(buyer=logged_in_user, status='approved').select_related('car')
    approved_bike_renters = Approvedbikerenters.objects.filter(buyer=logged_in_user, status='approved').select_related('bike')

    # Fetch transactions for all approved users
    car_transactions = Car_selling_transactions.objects.filter(car__in=[buyer.car_id for buyer in approved_car_buyers])
    bike_transactions = Bike_selling_transactions.objects.filter(bike__in=[buyer.bike_id for buyer in approved_bike_buyers])
    car_rent_transactions = Car_renting_transactions.objects.filter(car__in=[renter.car_id for renter in approved_car_renters])
    bike_rent_transactions = Bike_renting_transactions.objects.filter(bike__in=[renter.bike_id for renter in approved_bike_renters])

    # Prepare final list
    approved_users = []

    def add_transaction_data(user_obj, transaction, item, item_type):
        approved_users.append({
            'user': user_obj.buyer.username,
            'item': item,
            'item_type': item_type,
            'transaction_id': transaction.order_id if transaction else 'N/A',
            'paid_by': transaction.user.username if transaction and hasattr(transaction, 'user') else 'N/A',
            'amount': transaction.amount if transaction else 'N/A',
            'transaction_status': transaction.payment_status if transaction else 'No transaction'
        })

    # Loop through buyers and renters to extract payment details
    for buyer in approved_car_buyers:
        transaction = car_transactions.filter(car=buyer.car).first()
        add_transaction_data(buyer, transaction, buyer.car, 'Car Purchase')

    for buyer in approved_bike_buyers:
        transaction = bike_transactions.filter(bike=buyer.bike).first()
        add_transaction_data(buyer, transaction, buyer.bike, 'Bike Purchase')

    for renter in approved_car_renters:
        transaction = car_rent_transactions.filter(car=renter.car).first()
        add_transaction_data(renter, transaction, renter.car, 'Car Rental')

    for renter in approved_bike_renters:
        transaction = bike_rent_transactions.filter(bike=renter.bike).first()
        add_transaction_data(renter, transaction, renter.bike, 'Bike Rental')

    # Pass the data to the template
    context = {
        'approved_users': approved_users
    }

    return render(request, 'approved_users_payment_status_list.html', context)
