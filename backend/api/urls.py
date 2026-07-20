from Parkzoneapp import views
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    # CUSTOMER API'S
    path('customers/',views.manage_customer),
    path('customers/<int:id>',views.manage_customer),
    # path('customers/login/', views.customer_login, name='customer_login'),

    # RESERVATION API'S
    path('reservations/',views.manage_Reservation),
    path('reservations/<int:id>', views.manage_Reservation),
    # PARKING LOTS API'S
    path('parkinglots/',views.manage_ParkingLot),
    path('parkinglots/<int:id>',views.manage_ParkingLot),
    # PAYMENT API'S
    path('payments/',views.manage_Payment),
    path('payments/<int:id>',views.manage_Payment),
    # path('customer/<int:id>',views.cusustomer_view)

    path('customers/login', views.CustomerLoginAPIView.as_view(), name='customer_login_api'),


    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
