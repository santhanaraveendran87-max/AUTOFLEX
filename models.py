import random
from django.db import models

# Create your models here.
class user(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    phonenumber=models.IntegerField()
    password=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    pincode=models.IntegerField()
    image=models.ImageField(upload_to='images/')
    bio=models.CharField(max_length=100,blank=True,null=True)
    STATUS=(
        ('applied','Applied'),
        ('approved','Approved'),
        ('reject','Reject')
    )
    status=models.CharField(max_length=20,choices=STATUS,default='applied')
    otp = models.IntegerField(null=True, blank=True)  # Store OTP for verification


    def generate_otp(self):
        self.otp = random.randint(100000, 999999)  # Generate 6-digit OTP
        self.save()
        return self.otp




class work(models.Model):
    workname=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=50)
    phonenumber=models.IntegerField()
    workaddress=models.CharField(max_length=100)
    workregno=models.CharField(max_length=50, null=True, blank=True)
    image=models.ImageField(null=True,blank=True,upload_to='images/')

    STATUS=(
        ('applied','Applied'),
        ('approved','Approved'),
        ('reject','Reject')
    )
    status=models.CharField(max_length=20,choices=STATUS,default='applied')
    otp = models.IntegerField(null=True, blank=True)  # Store OTP for verification


    def generate_otp(self):
        self.otp = random.randint(100000, 999999)  # Generate 6-digit OTP
        self.save()
        return self.otp


class Services(models.Model):
    workshop=models.ForeignKey(work,on_delete=models.CASCADE)
    services=models.TextField(max_length=50)    
    service_id=models.IntegerField(unique=True)
    price_range=models.CharField(max_length=50,null=True,blank=True)
    workername=models.CharField(max_length=50,null=True,blank=True)
    phoneno=models.IntegerField(null=True,blank=True)


class Bookingworkshop(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    services= models.ForeignKey(Services, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    approval_status=models.CharField(max_length=20,default='pending',blank=True,null=True)


class Approvedworkshops(models.Model):
    user=models.ForeignKey(user,on_delete=models.CASCADE)
    services=models.ForeignKey(Services,on_delete=models.CASCADE)
    STATUS=(
        ('pending','Pending'),
        ('approved','Approved'),
        ('reject','Reject')
    )
    status=models.CharField(max_length=20,choices=STATUS,default='pending')

class show(models.Model):
    showname=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=50)
    phonenumber=models.IntegerField()
    showaddress=models.CharField(max_length=100)
    showregno=models.CharField(max_length=50, null=True, blank=True)
    image=models.ImageField(null=True,blank=True,upload_to='images/')
    STATUS=(
        ('applied','Applied'),
        ('approved','Approved'),
        ('reject','Reject')
    )
    status=models.CharField(max_length=20,choices=STATUS,default='applied')
    otp = models.IntegerField(null=True, blank=True)  # Store OTP for verification


    def generate_otp(self):
        self.otp = random.randint(100000, 999999)  # Generate 6-digit OTP
        self.save()
        return self.otp


class S_services(models.Model):
    showroom=models.ForeignKey(show,on_delete=models.CASCADE)
    services=models.TextField(max_length=50)    
    service_id=models.IntegerField(unique=True)
    price_range=models.CharField(max_length=50,null=True,blank=True)

class Bookingshowroom(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    services= models.ForeignKey(S_services, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    approval_status=models.CharField(max_length=20,default='pending',blank=True,null=True)

class Approvedshowroomss(models.Model):
    user=models.ForeignKey(user,on_delete=models.CASCADE)
    services=models.ForeignKey(S_services,on_delete=models.CASCADE)
    STATUS=(
        ('pending','Pending'),
        ('approved','Approved'),
        ('reject','Reject')
    )
    status=models.CharField(max_length=20,choices=STATUS,default='pending')

class showpost(models.Model):
    show=models.ForeignKey(show,on_delete=models.CASCADE,blank=True,null=True)
    brand=models.CharField(max_length=50)
    model=models.CharField(max_length=50)
    price=models.IntegerField()
    location = models.CharField(max_length=100, null=True, blank=True)  
    description=models.CharField(max_length=200)
    image=models.ImageField(upload_to='images/')  

class Bookingtestdrive(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    testdrive= models.ForeignKey(showpost, on_delete=models.CASCADE)
    date = models.DateField()
    approval_status=models.CharField(max_length=20,default='pending',blank=True,null=True)

class Approvedtestdrive(models.Model):
    user=models.ForeignKey(user,on_delete=models.CASCADE)
    testdrive= models.ForeignKey(showpost, on_delete=models.CASCADE)
    STATUS=(
        ('pending','Pending'),
        ('approved','Approved'),
        ('reject','Reject')
    )
    status=models.CharField(max_length=20,choices=STATUS,default='pending')

class spare(models.Model):
    sparename=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=50)
    phonenumber=models.IntegerField()
    spareaddress=models.CharField(max_length=100)
    spareregno=models.CharField(max_length=50, null=True, blank=True)
    image=models.ImageField(null=True,blank=True,upload_to='images/')
    STATUS=(
        ('applied','Applied'),
        ('approved','Approved'),
        ('reject','Reject')
    )
    status=models.CharField(max_length=20,choices=STATUS,default='applied')
    otp = models.IntegerField(null=True, blank=True)  # Store OTP for verification


    def generate_otp(self):
        self.otp = random.randint(100000, 999999)  # Generate 6-digit OTP
        self.save()
        return self.otp


class sparepost(models.Model):
    spare=models.ForeignKey(spare,on_delete=models.CASCADE,blank=True,null=True)
    productname=models.CharField(max_length=50)
    price=models.IntegerField()
    location = models.CharField(max_length=100, null=True, blank=True)  
    description=models.CharField(max_length=200)
    image=models.ImageField(upload_to='images/')  





class feedback(models.Model):
    RATING_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    ]
    feedback_text = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rating: {self.rating}, feedback: {self.feedback_text[:50]}..."
    

class carsell(models.Model):
    usr=models.ForeignKey(user,on_delete=models.CASCADE,blank=True,null=True)

    brand=models.CharField(max_length=50)
    model=models.CharField(max_length=50)
    price = models.IntegerField()  
    location = models.CharField(max_length=100, null=True, blank=True)  
    variant=models.CharField(max_length=50,null=True,blank=True)
    year=models.IntegerField()
    fuel=models.CharField(max_length=50)
    transmission=models.CharField(max_length=50)
    km=models.IntegerField()
    owners=models.IntegerField(null=True,blank=True) 
    description=models.CharField(max_length=200,null=True,blank=True)
    image=models.ImageField(upload_to='images/')
    b_status=(
        ('BOOK','book'),
        ('BOOKED','booked'),
    )
    bookingstatus=models.CharField(max_length=10,choices=b_status,default='book',blank=True,null=True)
    s_status=(
        ('AVAILABLE','available'),
        ('UNAVAILABLE','unavailable'),
        ('SOLDOUT','soldout'),
    )
    soldoutstatus=models.CharField(max_length=11,choices=s_status,default='available',blank=True,null=True)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

class bikesell(models.Model):
    usr=models.ForeignKey(user,on_delete=models.CASCADE,blank=True,null=True)

    brand=models.CharField(max_length=50)
    model=models.CharField(max_length=50,null=True,blank=True)
    price = models.IntegerField(default=0)  
    location = models.CharField(max_length=100, null=True, blank=True)  
    year=models.IntegerField()
    fuel=models.CharField(max_length=50)
    km=models.IntegerField()
    owners=models.IntegerField() 
    description=models.CharField(max_length=200)
    image=models.ImageField(upload_to='images/')  
    b_status=(
        ('BOOK','book'),
        ('BOOKED','booked'),
    )
    bookingstatus=models.CharField(max_length=10,choices=b_status,default='book',blank=True,null=True)
    s_status=(
        ('AVAILABLE','available'),
        ('UNAVAILABLE','unavailable'),
        ('SOLDOUT','soldout'),
    )
    soldoutstatus=models.CharField(max_length=11,choices=s_status,default='available',blank=True,null=True)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

class carrent(models.Model):
    usr=models.ForeignKey(user,on_delete=models.CASCADE,blank=True,null=True)
    brand=models.CharField(max_length=50)
    model=models.CharField(max_length=50,null=True,blank=True)
    year=models.IntegerField()
    fuel=models.CharField(max_length=50)
    km=models.IntegerField()
    owner=models.IntegerField()
    rentamount=models.IntegerField()
    description=models.CharField(max_length=200)
    image=models.ImageField(upload_to='images/')  
    availability=models.CharField(max_length=20,blank=True,null=True,default='Available')


    def __str__(self):
        return f"{self.brand} {self.model}')"

class bikerent(models.Model):
    usr=models.ForeignKey(user,on_delete=models.CASCADE,blank=True,null=True)
    brand=models.CharField(max_length=50,null=True,blank=True)
    model=models.CharField(max_length=50,null=True,blank=True)
    year=models.IntegerField()
    fuel=models.CharField(max_length=50)
    km=models.IntegerField()
    owner=models.IntegerField()
    rentamount=models.IntegerField()
    description=models.CharField(max_length=200)
    image=models.ImageField(upload_to='images/')  
    availability=models.CharField(max_length=20,blank=True,null=True,default='Available')


    def __str__(self):
        return f"{self.brand} {self.model}')"


class BookingCarRent(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    car = models.ForeignKey(carrent, on_delete=models.CASCADE)
    startdate = models.DateField()
    enddate = models.DateField() 
    totalprice=models.IntegerField(null=True,blank=True,default=0)
    approval_status=models.CharField(max_length=20,default='pending',blank=True,null=True)  
    
class BookingBikeRent(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    bike = models.ForeignKey(bikerent, on_delete=models.CASCADE)
    startdate = models.DateField()
    enddate = models.DateField() 
    totalprice=models.IntegerField(null=True,blank=True,default=0)
    approval_status=models.CharField(max_length=20,default='pending',blank=True,null=True)

class BookingCarsell(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    car = models.ForeignKey(carsell, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    approval_status=models.CharField(max_length=20,default='pending',blank=True,null=True)
    
class BookingBikesell(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    bike = models.ForeignKey(bikesell, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    approval_status=models.CharField(max_length=20,default='pending',blank=True,null=True)


class Approvedcarbuyers(models.Model):
    buyer=models.ForeignKey(user,on_delete=models.CASCADE)
    car=models.ForeignKey(carsell,on_delete=models.CASCADE)
    STATUS=(
        ('pending','Pending'),
        ('approved','Approved'),
        ('reject','Reject')
    )
    status=models.CharField(max_length=20,choices=STATUS,default='pending')
    
class Approvedbikebuyers(models.Model):
    buyer=models.ForeignKey(user,on_delete=models.CASCADE)
    bike=models.ForeignKey(bikesell,on_delete=models.CASCADE)
    STATUS=(
        ('pending','Pending'),
        ('approved','Approved'),
        ('reject','Reject')
    )
    status=models.CharField(max_length=20,choices=STATUS,default='pending')
    
class Approvedcarrenters(models.Model):
    buyer=models.ForeignKey(user,on_delete=models.CASCADE)
    car=models.ForeignKey(carrent,on_delete=models.CASCADE)
    STATUS=(
        ('pending','Pending'),
        ('approved','Approved'),
        ('reject','Reject')
    )
    status=models.CharField(max_length=20,choices=STATUS,default='pending')   

class Approvedbikerenters(models.Model):
    buyer=models.ForeignKey(user,on_delete=models.CASCADE)
    bike=models.ForeignKey(bikerent,on_delete=models.CASCADE)
    STATUS=(
        ('pending','Pending'),
        ('approved','Approved'),
        ('reject','Reject')
    )
    status=models.CharField(max_length=20,choices=STATUS,default='pending')   

class Car_selling_transactions(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    car = models.ForeignKey(carsell, on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=15,decimal_places=2)
    order_id=models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
    payment_status = models.CharField(max_length=20, default='pending', choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')])


class Car_renting_transactions(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    car = models.ForeignKey(carrent, on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=15,decimal_places=2)
    order_id=models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
    payment_status = models.CharField(max_length=20, default='pending', choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')])

class Bike_selling_transactions(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    bike = models.ForeignKey(bikesell, on_delete=models.CASCADE)
    amount=models.DecimalField(max_digits=15,decimal_places=2)
    order_id=models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
    payment_status = models.CharField(max_length=20, default='pending', choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')])

class Bike_renting_transactions(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    bike = models.ForeignKey(bikerent, on_delete=models.CASCADE,blank=True,null=True)  # ✅ Corrected field name
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    order_id = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
    payment_status = models.CharField(max_length=20, default='pending', choices=[('pending', 'Pending'), ('completed', 'Completed'), ('failed', 'Failed')])



