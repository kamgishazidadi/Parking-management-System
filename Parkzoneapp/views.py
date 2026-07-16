from django.shortcuts import render
# from rest_framework.decorators import api_view
from .models import *
from .serializer import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
# Simple_jwt security features
# from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


# Create your views here.

# Customer table api



'''
@api_view(['GET','POST'])
def get_and_post(request):
    if request.method == 'GET':
        cust = Customer.objects.all()
        serializer = CustomerSerializer(cust, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CustomerSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response (serializer.errors)
        
@api_view(['GET','PUT','DELETE'])
def cusustomer_view(request,id):
    try:
        cust = Customer.objects.get(id = id)
    except Customer.DoesNotExist:
        return Response({'message':'Id not exists!'})
    if request.method == 'GET':
        seralizer = CustomerSerializer(cust)
        return Response(seralizer.data)

    elif request.method == 'PUT':
        serializer = CustomerSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response (serializer.errors)

        

    elif request.method == 'DELETE':
        cust.delete()
        return Response(f"Customer has been deleted")

'''


def generic_api(model_class, serializer_class):
    @api_view(['GET','POST', 'DELETE', 'PUT'])
    # @permission_classes([IsAuthenticated])


    def api(request, id = None):
        if request.method == 'GET':
            if id:
                try:
                    instance = model_class.objects.get(id = id)
                    serializer = serializer_class(instance)
                    return Response(serializer.data)
                except model_class.DoesNotExist:
                    return Response({'message':'Object Not Found'}, status=status.HTTP_404_NOT_FOUND)
            else:
                instance = model_class.objects.all()
                serializer = serializer_class(instance, many = True)
                return Response(serializer.data)

        elif request.method == 'POST':
            serializer = serializer_class(data=request.data)
            if serializer.is_valid():
                    serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Success
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # If serializer is invalid


        elif request.method == 'DELETE':
            if id:
                try:
                    instance = model_class.objects.get(id = id)
                    instance.delete()
                    return Response({'message':'Delete Successfully'})
                except model_class.DoesNotExist:
                    return Response({'message':'Object Not Found'}, status=status.HTTP_404_NOT_FOUND)
                

        elif request.method == 'PUT':
            if id:
                try:
                    instance = model_class.objects.get(id=id)
                    serializer = serializer_class(instance, data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                    return Response(serializer.data)
                
                        
                except model_class.DoesNotExist:
                    return Response({'message': 'Object not found'}, status=status.HTTP_404_NOT_FOUND)

    return api



manage_customer = generic_api(Customer, CustomerSerializer)
        
manage_ParkingLot = generic_api(ParkingLot, ParkingLotSerializer)
  
manage_Reservation = generic_api(Reservation, ReservationSerializer)
        
manage_Payment = generic_api(Payment, PaymentSerializer)
      

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def protected_view(request):
#     return Response({"message": "This is a protected view!"})


# New view of login
#
# from django.contrib.auth.models import User
# from django.http import JsonResponse
# from django.contrib.auth import authenticate
#
# def customer_login(request):
#     if request.method == "POST":
#         import json
#         data = json.loads(request.body)
#         email = data.get("email")
#         password = data.get("password")
#
#         try:
#             # Check if a user with the email exists
#             user = User.objects.get(email=email)
#             # Authenticate the user
#             authenticated_user = authenticate(username=user.username, password=password)
#             if authenticated_user:
#                 return JsonResponse({
#                     "success": True,
#                     "customer": {
#                         "id": user.id,
#                         "name": user.first_name,
#                         "email": user.email,
#                     }
#                 }, status=200)
#             else:
#                 return JsonResponse({"success": False, "error": "Invalid credentials"}, status=401)
#         except User.DoesNotExist:
#             return JsonResponse({"success": False, "error": "User not found"}, status=404)
#
#     return JsonResponse({"error": "Invalid request method"}, status=400)

  



#Login view for customer

class CustomerLoginAPIView(APIView):
    def post(self, request):
        serializer = CustomerLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            try:
                customer = Customer.objects.get(email=email)
                if customer.password == password:
                    return Response({
                        'message': 'Login successful',
                        'customer_id': customer.id,
                        'name': customer.name,
                        'email': customer.email,
                        'phone': customer.phone,
                        'residence': customer.residence,
                    })
                else:
                    return Response({'error': 'Invalid password'}, status=status.HTTP_401_UNAUTHORIZED)
            except Customer.DoesNotExist:
                return Response({'error': 'Customer not found'}, status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

