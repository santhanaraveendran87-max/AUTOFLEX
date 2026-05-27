"""CARS_BIKES URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from.import views
from django.shortcuts import get_object_or_404,render,redirect,HttpResponse

urlpatterns = [
    path('index/',views.index,name='index'),
    path('',views.index,name='index'),
    path('alogout/', views.alogout, name='alogout'),


    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('home/',views.home,name='home'),
    path('userlist/',views.userlist,name='userlist'),
    path("deluser/<int:id>",views.deluser,name="deluser"),
    path('userprofile/',views.userprofile,name='userprofile'),
    path('ulogout/', views.ulogout, name='ulogout'),

    path('workreg/',views.workreg,name='workreg'),
    path('worklogin/',views.worklogin,name='worklogin'),
    path('workhome/',views.workhome,name='workhome'),
    path('worklist/',views.worklist,name='worklist'),  
    path('workprofile/',views.workprofile,name='workprofile'),
    path("delwork/<int:id>",views.delwork,name="delwork"),
    path('w_updateprou/',views.w_updateprou,name='w_updateprou'),
    path('w_proupdateu/',views.w_proupdateu,name='w|_proupdateu'),
    path('wlogout/', views.wlogout, name='wlogout'),

    path('addservices/',views.addservices,name='addservices'),
    path('services_list/',views.services_list,name='services_list'),
    path('book_services/<int:id>/', views.book_services, name='book_service'),
    path("delete_service/<int:service_id>",views.delete_service,name="delete_service"),
    path('edit_service/<int:service_id>/', views.edit_service, name='edit_service'),
    path('booknow_services/<int:service_id>/', views.booknow_services, name='booknow_services'), 
    path('mybookingworkshop/',views.mybookingworkshop,name='mybookingworkshop'),
    path('listworkbookings/<int:wid>/',views.listworkbookings,name='listworkbookings'),
    path('approveinsterestedworkshops/<int:bid>/',views.approveinsterestedworkshops,name='approveinsterestedworkshops'),
    path('rejectinsterestedworkshops/<int:bid>/',views.rejectinsterestedworkshops,name='rejectinsterestedworkshops'),
   
    path('showreg/',views.showreg,name='showreg'),
    path('showlogin/',views.showlogin,name='showlogin'),
    path('showhome/',views.showhome,name='showhome'),
    path('showlist/',views.showlist,name='showlist'),
    path('showprofile/',views.showprofile,name='showprofile'),
    path("delshow/<int:id>",views.delshow,name="delshow"),

    path('updateprou/',views.updateprou,name='updateprou'),
    path('proupdateu/',views.proupdateu,name='proupdateu'),

    path('shlogout/', views.shlogout, name='shlogout'),

    path('s_add_services/',views.s_add_services,name='s_add_services'),
    path('s_services_list/',views.s_services_list,name='s_services_list'),
    path('s_book_services/<int:id>/', views.s_book_services, name='s_book_service'),
    path("delete_service1/<int:service_id>",views.delete_service1,name="delete_service1"),
    path('edit_service1/<int:service_id>/', views.edit_service1, name='edit_service1'),
    path('s_booknow_services/<int:service_id>/', views.s_booknow_services, name='s_booknow_services'), 
    path('mybookingshowroom/',views.mybookingshowroom,name='mybookingshowroom'),
    path('listshowbookings/<int:wid>/',views.listshowbookings,name='listshowbookings'),
    path('approveinsterestedshowrooms/<int:bid>/',views.approveinsterestedshowrooms,name='approveinsterestedshowrooms'),
    path('rejectinsterestedshowrooms/<int:bid>/',views.rejectinsterestedshowrooms,name='rejectinsterestedshowrooms'),

   #testdrive
    path('booknow_testdrive/<int:test_id>/',views.booknow_testdrive,name='booknow_testdrive'),
    path('mybookingtestdrive/',views.mybookingtestdrive,name='mybookingtestdrive'),
    path('listtestdrive/<int:tid>/',views.listtestdrive,name='listtestdrive'),
    path('approveinsterestedtestdrivers/<int:bid>/',views.approveinsterestedtestdrivers,name='approveinsterestedtestdrivers'),
    path('rejectinsterestedtestdrivers/<int:bid>/',views.rejectinsterestedtestdrivers,name='rejectinsterestedtestdrivers'),

    


    path('showposts/',views.showposts,name='showposts'),
    path('showpostslist/',views.showpostslist,name='showpostslist'),
    path("delshowposts/<int:id>",views.delshowposts,name='delshowposts'),
    path('edit_showposts/<int:id>/', views.edit_showposts, name='edit_showposts'),
    path('showpostsview/',views.showpostsview,name='showpostsview'), 
    path('showpostslistu/<int:id>/',views.showpostslistu,name='showpostslistu'),


    path('adminlogin/',views.adminlogin,name='adminlogin'),
    # path('adminhome/',views.adminhome,name='adminhome'),

    path('userfeedback_rate/',views.userfeedback_rate,name='userfeedback_rate'),
    path('userfeedback_success/',views.userfeedback_success,name='userfeedback_success'),
    path('workfeedback_rate/',views.workfeedback_rate,name='workfeedback_rate'),
    path('workfeedback_success/',views.workfeedback_success,name='workfeedback_success'),
    path('showfeedback_rate/',views.showfeedback_rate,name='showfeedback_rate'),
    path('showfeedback_success/',views.showfeedback_success,name='showfeedback_success'),
    path('sparefeedback_rate/',views.sparefeedback_rate,name='sparefeedback_rate'),
    path('sparefeedback_success/',views.sparefeedback_success,name='sparefeedback_success'),
    path('feedbacklist/',views.feedbacklist,name='feedbacklist'),
    path("delfeedback/<int:id>",views.delfeedback,name="delfeedback"),
    path('adminindex/',views.adminindex,name='adminindex'),

    path('user_showlist/',views.user_showlist,name='user_showlist'),
    path('user_worklist/',views.user_worklist,name='user_worklist'),
    path('user_sparelist/',views.user_sparelist,name='user_sparelist'),
    path('work_sparelist/',views.work_sparelist,name='work_sparelist'),
    path('sparepostslist/<int:id>/',views.sparepostslist,name='sparepostslist'), 


    path('sparereg/',views.sparereg,name='sparereg'),
    path('sparelogin/',views.sparelogin,name='sparelogin'),
    path('sparehome/',views.sparehome,name='sparehome'),
    path('sparelist/',views.sparelist,name='sparelist'),  
    path('spareprofile/',views.spareprofile,name='spareprofile'),
    path("delspare/<int:id>",views.delspare,name="delspare"),
    path('sp_updateprou/',views.sp_updateprou,name='sp_updateprou'),
    path('sp_proupdateu/',views.sp_proupdateu,name='sp_proupdateu'),
    path('splogout/', views.splogout, name='splogout'),

    path('spareposts/',views.spareposts,name='spareposts'),
    path('sparepostslist/',views.sparepostslist,name='sparepostslist'),
    path("delspareposts/<int:id>",views.delspareposts,name='delspareposts'),
    path('edit_spareposts/<int:id>/', views.edit_spareposts, name='edit_spareposts'),
    path('sparepostsview/',views.sparepostsview,name='sparepostsview'), 
    path('sparepostslistu/<int:id>/',views.sparepostslistu,name='sparepostslistu'),
    path('sparepostslistw/<int:id>/',views.sparepostslistw,name='sparepostslistw'),



    path('update_status/',views.update_status,name='update_status'),
    path('update_status2/',views.update_status2,name='update_status2'),
    path('update_status3/',views.update_status3,name='update_status3'),
    path('update_status4/',views.update_status4,name='update_status4'),


    
    path('carsell/',views.carsell1,name='carsell1'),
    path('carselllist/',views.carselllist,name='carselllist'),
    path("deluser1/<int:id>",views.deluser1,name='deluser1'),
    path('editcar/<int:id>/', views.edit_car, name='editcar'), 
    path('bookcarsell/',views.bookcarsell,name='bookcarsell'),
    path('booknowcarsell/<int:id>/', views.booknowcarsell, name='booknowcarsell'), 
    path('mybookingcar_S/',views.mybookingcar_S,name='mybookingcar_S'),
    path('listcarbuyers/<int:cid>/',views.listcarbuyers,name='listcarbuyers'),
    path('approveinsterestedbuyers/<int:bid>/',views.approveinsterestedbuyers,name='approveinsterestedbuyers'),
    path('rejectinsterestedbuyers/<int:bid>/',views.rejectinsterestedbuyers,name='rejectinsterestedbuyers'),


    path('bikesell/',views.bikesell1,name='bikesell1'),
    path('bikeselllist/',views.bikeselllist,name='bikeselllist'),
    path("deluser2/<int:id>",views.deluser2,name='deluser2'),
    path('editbike/<int:id>/', views.edit_bike, name='editbike'), 
    path('bookbikesell/', views.bookbikesell, name='bookbikesell'), 
    path('booknowbikesell/<int:id>/', views.booknowbikesell, name='booknowbikesell'), 
    path('mybookingbike_S/',views.mybookingbike_S,name='mybookingbike_S'),
    path('listbikebuyers/<int:bike_id>/',views.listbikebuyers,name='listbikebuyers'),
    path('approveinsterestedbikebuyers/<int:bid>/',views.approveinsterestedbikebuyers,name='approveinsterestedbikebuyers'),
    path('rejectinsterestedbikebuyers/<int:bid>/',views.rejectinsterestedbikebuyers,name='rejectinsterestedbikebuyers'),

    path('carrent/',views.carrent1,name='carrent1'),
    path('carrentlist/',views.carrentlist,name='carrentlist'),
    path("delcar_rent/<int:id>", views.deluser2, name='delcar_rent'),
    path('bookcarrent/',views.bookcarrent,name='bookcarrent'),
    path('set_availability/<int:id>/',views.set_availability,name='set_availability'),
    path('booknowcarrent/<int:id>/', views.booknowcarrent, name='booknowcarrent'),
    path('mybookingcar_R/',views.mybookingcar_R,name='mybookingcar_R'),
    path('listcarrenters/<int:car_id>/',views.listcarrenters,name='listcarrenters'),
    path('approveinsterestedrenters/<int:bid>/',views.approveinsterestedrenters,name='approveinsterestedrenters'),
    path('rejectinsterestedrenters/<int:bid>/',views.rejectinsterestedrenters,name='rejectinsterestedrenters'),






    path('bikerent/',views.bikerent1,name='bikerent'),
    path('bikerentlist/',views.bikerentlist,name='bikerentlist'),
    path("delbike_rent/<int:id>", views.deluser4, name='delbike_rent'),
    path('bookbikerent/',views.bookbikerent,name='bookbikerent'),
    path('set_availability1/<int:id>/',views.set_availability1,name='set_availability1'),
    path('booknowbikerent/<int:id>/', views.booknowbikerent, name='booknowbikerent'),
    path('mybookingbike_R/',views.mybookingbike_R,name='mybookingbike_R'),
    path('listbikerenters/<int:bike_id>/',views.listbikerenters,name='listbikerenters'),
    path('approveinsterestedbikerenters/<int:bid>/',views.approveinsterestedbikerenters,name='approveinsterestedbikerenters'),
    path('rejectinsterestedbikerenters/<int:bid>/',views.rejectinsterestedbikerenters,name='rejectinsterestedbikerenters'),

    # path('paymenthandler/<int:car_id>/', views.paymenthandler, name='paymenthandler'),

    #  path('payment/<int:car_id>/', views.payment, name='payment'),
    # path('pay_success/', views.pay_success, name='pay_success'),
    # path('pay_failed/', views.pay_failed, name='pay_failed'),

   
    path('initiate-payment/<cid>/',views.initiate_payment,name='initial-payment'),
    path('confirm-payment/<order_id>/<payment_id>/<crti_id>/',views.confirm_payment,name='confirm-paymment'),

    path('initiate-payment_bikesell/<cid>/',views.initiate_payment_bikesell,name='initiate_payment_bikesell'),
    path('confirm-payment_bikesell/<order_id>/<payment_id>/<crti_id>/',views.confirm_payment_bikesell,name='confirm_payment_bikesell'),

    path('rent_initiate-payment/<cid>/',views.rent_initiate_payment,name='rent_initial-payment'),
    path('rent_confirm-payment/<order_id>/<payment_id>/<book_id>/',views.rent_confirm_payment,name='rent_confirm-paymment'),

    path('rentbike_initiate-payment/<cid>/',views.rentbike_initiate_payment,name='rentbike_initial-payment'),
    path('rentbike_confirm-payment/<order_id>/<payment_id>/<book_id>/',views.rentbike_confirm_payment,name='rentbike_confirm-paymment'),

    path('transactions/', views.transaction_history, name='transaction_history'),



    path('show_map/', views.show_map, name='map'),
    path('get-nearby-fuel-stations/', views.get_nearby_fuel_stations, name='get_nearby_fuel_stations'),
    path('get_nearby_workshops/', views.get_nearby_workshops, name='get_nearby_workshops'),
    path('show_workshop_map/', views.show_workshop_map, name='show_workshop_map'),




    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('reset-password/', views.reset_password, name='reset_password'),

    path('forgot-passwordw/', views.forgot_passwordw, name='forgot_passwordw'),
    path('verify-otpw/', views.verify_otpw, name='verify_otpw'),
    path('reset-passwordw/', views.reset_passwordw, name='reset_passwordw'),

    path('forgot-passwords/', views.forgot_passwords, name='forgot_passwords'),
    path('verify-otps/', views.verify_otps, name='verify_otps'),
    path('reset-passwords/', views.reset_passwords, name='reset_passwords'),

    path('forgot-passwordsp/', views.forgot_passwordsp, name='forgot_passwordsp'),
    path('verify-otpsp/', views.verify_otpsp, name='verify_otpsp'),
    path('reset-passwordsp/', views.reset_passwordsp, name='reset_passwordsp'),

    path('approved-users-payment-status/', views.approved_users_with_payment_status, name='approved_users_payment_status'),
    
    path('s_updateprou/',views.s_updateprou,name='s_updateprou'),
    path('s_proupdateu/',views.s_proupdateu,name='s_proupdateu'),
    path('edit_bike1/<int:id>/', views.edit_bike1, name='edit_bike1'), 
    path('edit_car1/<int:id>/', views.edit_car1, name='edit_car1'), 


]