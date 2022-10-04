from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('emailresetpass/', views.emailresetpass, name='emailresetpass'),
    path('emailresetpassrecord/', views.emailresetpassrecord, name='emailresetpassrecord'),
    path('resetpass/<int:id>', views.resetpass, name='resetpass'),
    path('resetpassrecord/<int:id>', views.resetpassrecord, name='resetpassrecord'),
    path('login/', views.login, name='login'),
    path('loginlog/', views.loginlog, name='loginlog'),
    path('logout/', views.logout, name='logout'),
    path('admin/login/', views.admin_login, name='admin_login'),
    path('admin/loginlog/', views.admin_loginlog, name='admin_loginlog'),
    path('admin/logout/', views.admin_logout, name='admin_logout'),
    path('addrecord/', views.addrecord, name='addrecord'),
    path('indexx/', views.indexx, name='indexx'),
    path('results/', views.results, name='results'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('profile/', views.profile, name='profile'),
    path('adminprofile/', views.adminprofile, name='adminprofile'),
    path('editprofile/', views.editprofile, name='editprofile'),
    path('editprofilee/', views.editprofilee, name='editprofilee'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('deleteorder/<int:id>', views.deleteorder, name='deleteorder'),
    path('contact/', views.contact, name='contact'),
    path('contact/', views.mailer, name='mailer'),
    path('contactrecord/', views.contactrecord, name='contactrecord'),
    path('about_us/', views.about_us, name='about_us'),
    path('upload_file/', views.upload_file, name='upload_file'),
    path('admin/remove_screens/<int:id>', views.remove_screens, name='remove_screens'),
    path('admin/remove_screens/', views.remove_screens, name='remove_screens'),
    path('admin/removescreendel/<int:id>', views.removescreendel, name='removescreendel'),
    path('property-details/', views.property_details, name='property-details'),
    path('property-details/<int:id>', views.property_details, name='property-details'),
    path('payment-process/', views.payment_process, name='payment-process'),
    path('payment_receipt/<int:id>', views.payment_receipt, name='payment_receipt'),
    path('bookorder/<int:id>', views.bookorder, name='bookorder'),
    path('bookorderedit', views.bookorderedit, name='bookorderedit'),
    path('bookorderedit/<int:id>', views.bookorderedit, name='bookorderedit'),
    path('cancelorder/<int:id>', views.cancelorder, name='cancelorder'),
    path('bookordereditrecord/<int:id>', views.bookordereditrecord, name='bookordereditrecord'),
    path('statusedit/<int:id>', views.statusedit, name='statusedit'),
    path('statuseditrecord/<int:id>', views.statuseditrecord, name='statuseditrecord'),
    path('userstatus/<int:id>', views.userstatus, name='userstatus'),
    path('userstatusrecord/<int:id>', views.userstatusrecord, name='userstatusrecord'),
    path('admin/addscreens/', views.adminprofile, name='addscreens'),
    path('admin/screensedit/<int:id>', views.screensedit, name='screensedit'),
    path('admin/screenseditrecord/<int:id>', views.screenseditrecord, name='screenseditrecord'),
    path('deletescreen/<int:id>', views.deletescreen, name='deletescreen'),
    path('subscribe_email/<str:html>', views.subscribe_email, name='subscribe_email'),
]
