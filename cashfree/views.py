# from cashfree_sdk.payouts.transfers import Transfers
# from cashfree_sdk.payouts.beneficiary import Beneficiary as bene
# from cashfree_sdk.payouts.validations import Validations
# from cashfree_sdk.payouts import Payouts
# from django.shortcuts import render
# from videosession.settings import DEBUG
# import json
# from cashfree_sdk.exceptions.exceptions import BadRequestError, EntityDoesntExistError
# import requests
# from .serializers import BeneficiarySerializer
# from .models import Beneficiary
# from rest_framework.response import Response
# from rest_framework import viewsets
# from rest_framework import permissions
# # Create your views here.
# if DEBUG == True:
#     url = 'https://test.cashfree.com'
#     appId = '60110871b19dcf536eba63ff401106'
#     secretKey = '68f496d0a73be831c7a34cca3907425d00009c6f'
# else:
#     url = 'https://api.cashfree.com'
#
# data = {
#     "appId": appId,
#     "secretKey": secretKey,
#     "orderId": 1,
#     "orderAmount": 100,
#     "customerName": "John Doe",
#     "customerPhone": 9876543210,
#     "customerEmail": "johndoe@dummy.com",
#     "returnUrl": "https://www.google.com/"
# }
#
#
# class Cashfree:
#     # To create payment link
#     def createPaymentLink(self, data):
#         payment = requests.post(url+'/api/v1/order/create', data=data)
#         response = payment.text
#         return response
#
#     # Returns payment status of an existing order
#     def paymentStatus(self, data):
#         payment = requests.post(url+'/api/v1/order/info/status', data=data)
#         response = payment.text
#         return response
#
#     # Returns payment link for an existing order
#     def existingOrderPaymentLink(self, data):
#         payment = requests.post(url+'/api/v1/order/info/link', data=data)
#         response = payment.text
#         return response
#
#
# if DEBUG == True:
#     payout_url = 'https://payout-gamma.cashfree.com'
# else:
#     payout_url-'https://payout-api.cashfree.com'
#
#
# def Payouts(self):
#     clientId: 'CF60110C1EOB77A55OA211PLMQG'
#     clientSecret: 'c99d1c046e9ee1555974ee2e82ed18c96d50ee8d'
#     env = "TEST"
#
#     beneId = "JOHN180129091524352"
#     transferId = "tranfer001232347"
#
#     bene = {
#         "beneId": beneId,
#         "name": "john doe",
#         "email": "johndoe@cashfree.com",
#         "phone": "9876543213",
#         "bankAccount": "00011020001672",
#         "ifsc": "HDFC0000001",
#         "address1": "ABC Street",
#         "city": "Bangalore",
#         "state": "Karnataka",
#         "pincode": "560001"
#     }
#
#     transfer = {
#         "beneId": beneId,
#         "transferId": transferId,
#         "amount": "1.00",
#     }
#
#     try:
#         Payouts.init(clientId, clientSecret, env)
#         try:
#             bene_details_response = Beneficiary.get_bene_details(
#                 bene["beneId"])
#             bene_details_response_content = json.loads(
#                 bene_details_response.content)
#             print("get beneficary details")
#             print(bene_details_response_content)
#         except EntityDoesntExistError as err:
#             bene_add_response = Beneficiary.add(beneId=bene['beneId'], name=bene['name'], email=bene['email'], phone=bene['phone'], bankAccount=bene['bankAccount'],
#                                                 ifsc=bene['ifsc'], address1=bene['address1'], city=bene['city'], state=bene['state'], pincode=bene['pincode'])
#             print("beneficiary addition response")
#             print(bene_add_response.content)
#
#         request_transfer_response = Transfers.request_transfer(
#             beneId=transfer['beneId'], transferId=transfer['transferId'], amount=transfer['amount'])
#         print("request transfer response")
#         print(request_transfer_response.content)
#
#         get_transfer_status_response = Transfers.get_transfer_status(
#             transferId=transferId)
#         print("get transfer status response")
#         print(get_transfer_status_response.content)
#
#     except Exception as err:
#         print("err occurred")
#         print(err)
#
#
# class addToBeneficiary(viewsets.ModelViewSet):
#     serializer_class = BeneficiarySerializer
#     queryset = Beneficiary.objects.all()
#     permission_classes = [permissions.AllowAny]
#
#     def create(self, request):
#         data = request.data
#         serializer = BeneficiarySerializer(data=request.data)
#         if serializer.is_valid():
#             v_det = Validations.bank_details_validation(
#                 name=request.data.get("name"),
#                 phone=request.data.get("phone"),
#                 bankAccount=request.data.get("bankAccount"),
#                 ifsc=request.data.get("ifsc"))
#             v_det = json.loads(v_det)
#             if v_det["status"] == "SUCCESS":
#                 bene_add_response = bene.add(
#                     beneId=request.data.get("beneId"),
#                     name=request.data.get("name"),
#                     email=request.data.get("email"),
#                     phone=request.data.get("phone"),
#                     bankAccount=request.data.get("bankAccount"),
#                     ifsc=request.data.get("ifsc"),
#                     address1=request.data.get("address"),
#                     city=request.data.get("city"),
#                     stat=request.data.get("state"),
#                     pincode=request.data.get("pincode")
#                 )
#                 response = json.loads(bene_add_response.text)
#                 if response["status"] == "SUCCESS":
#                     serializer.save()
#                 return Response(response)
#             else:
#                 return Response(v_det)
