from django.shortcuts import render
from rest_framework import viewsets
from . import serializers
from . import models
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from django.http import HttpResponse
import razorpay
from rest_framework import permissions
from customuser.models import CustomUser
import requests
import json
import string
import random
# from cashfree.models import Beneficiary, Transactions
# from cashfree_sdk.payouts.transfers import Transfers
# from cashfree_sdk.payouts.transfers import Transfers
# from cashfree_sdk.payouts.beneficiary import Beneficiary as beneficiary
# from cashfree_sdk.payouts import Payouts
from django.shortcuts import render
from videosession.settings import DEBUG
import json
# from cashfree_sdk.exceptions.exceptions import BadRequestError, EntityDoesntExistError
import requests
client = razorpay.Client(auth=("rzp_test_LmOgpIykhftvK7",
                               "rqWbFlWkSw3OaIeLZqEGgPFg"))

client.set_app_details(
    {"title": "CodeCrux",
     "version": "3.1.3"})


class HireViewset(viewsets.ModelViewSet):
    queryset = models.Hire.objects.all()
    serializer_class = serializers.HireSerializer

    def list(self, request):
        queryset = self.queryset
        serializer = serializers.HireSerializer(queryset, many=True)
        data = serializer.data
        print('data3', data)
        for element in data:
            print('elements', element)
            try:
                sent_by_user = CustomUser.objects.get(id=element["sent_by"])
                sent_by_user_name = f'{sent_by_user.first_name} {sent_by_user.last_name}'
                print('sent_by', sent_by_user_name)
                element['sent_by'] = sent_by_user_name
            except:
                element['sent_by'] = ""
        return Response(data)

    def retrieve(self, request, pk=None):
        queryset = self.queryset
        contract = get_object_or_404(queryset, pk=pk)
        serializer = serializers.HireSerializer(contract)
        return Response(serializer.data)

    def update(self, instance, pk=None):
        print('50', self.request.data['hiring_status'])
        # instance.hiring_status=self.request.data['hiring_status']
        queryset = self.queryset
        contract = get_object_or_404(queryset, pk=pk)
        serializer = serializers.HireSerializer(
            contract, data=self.request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
        data = serializer.data
        print('data', type(data))
        try:
            sent_by_user = CustomUser.objects.get(id=data["sent_by"])
            sent_by_user_name = f'{sent_by_user.first_name} {sent_by_user.last_name}'
            print('sent_by', sent_by_user_name)
            data['sent_by'] = sent_by_user_name
        except:
            data['sent_by'] = ""
        return Response(data)

    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ('user__technology', 'user__sub_technology', 'user__topic')

# class Order(APIView):
# 	permission_classes = [permissions.AllowAny]
# 	def get(self, request):
# 		hire = models.Hire.objects.get(id=request.GET["hire_id"])
# 		order_amount = hire.budget*100 if hire.budget else 100
# 		order_currency = 'INR'
# 		order_receipt = str(hire.id)
# 		# notes = {'Shipping address': 'Bommanahalli, Bangalore'}   # OPTIONAL
# 		# reponse = client.order.create(amount=order_amount, currency=order_currency, receipt=order_receipt, )
# 		print("sfs",dict(amount=order_amount, currency='INR', receipt=order_receipt,
# 			payment_capture='1'))
# 		response = client.order.create(dict(amount=order_amount, currency='INR', receipt=order_receipt,
# 			payment_capture='1'))
# 		print("self, ",response)
# 		return HttpResponse(response["id"])


# class SuccessfulOrder(APIView):
#     permission_classes = [permissions.AllowAny]
#
#     def post(self, request):
#         orderId = request.data.get("orderId")
#         educator = request.data.get("educator")
#         # orderId = request.data.get("orderId")
#         url = 'https://test.cashfree.com'
#         appId = '60110871b19dcf536eba63ff401106'
#         secretKey = '68f496d0a73be831c7a34cca3907425d00009c6f'
#         data = {
#             "appId": appId,
#             "secretKey": secretKey,
#             "orderId": orderId
#         }
#         payment = requests.post(url+'/api/v1/order/info/status', data=data)
#         print(payment.text)
#         response = json.loads(payment.text)
#         if response["orderStatus"] == "PAID":
#             amount = float(response["orderAmount"]) - \
#                 (6*float(response["orderAmount"])/100)
#             clientId = 'CF60110C1EOB77A55OA211PLMQG'
#             clientSecret = 'c99d1c046e9ee1555974ee2e82ed18c96d50ee8d'
#             env = "TEST"
#             Payouts.init(clientId, clientSecret, env)
#             bene = Beneficiary.objects.get(user=educator)
#             print("bene ............", str(bene.beneId).replace("-", ""))
#             bene_details_response = beneficiary.get_bene_details(
#                 str(bene.beneId).replace("-", ""))
#             print(bene_details_response)
#             if bene is not None:
#                 print(bene_details_response)
#                 if json.loads(bene_details_response.text)["status"] == "SUCCESS" and json.loads(bene_details_response.text)["subCode"] == "200":
#                     transaction, trans_boolean = Transactions.objects.get_or_create(
#                         orderId=str(orderId))
#                     transaction.transferId = ''.join(random.choices(string.ascii_uppercase +
#                                                                     string.digits, k=10))
#                     transaction.amount = amount
#                     transaction.revenue = 6*float(response["orderAmount"])/100
#                     transaction.status = response["orderStatus"]
#                     transaction.save()
#                     print(amount, transaction.amount)
#                     transfer = Transfers.request_transfer(
#                         beneId=str(bene.beneId).replace("-", ""),
#                         transferId=str(
#                             transaction.transferId).replace("-", ""),
#                         amount=amount,
#                     )
#                     transfer = json.loads(transfer.text)
#                     get_transfer_status_response = Transfers.get_transfer_status(
#                         transferId=str(
#                             transaction.transferId).replace("-", ""))
#                     transaction.status = transfer["status"]
#                     transaction.save()
#         return Response(json.loads(get_transfer_status_response.text))


class Order(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        print(request.data.get("hire_id"))
        educator = request.data.get("educator")
        hire = models.Hire.objects.get(id=request.data.get("hire_id"))
        order_amount = hire.budget
        # url = 'https://api.cashfree.com'
        # appId = '105770a2b1f3a6b637431038ec077501'
        # secretKey = '3090248538fcba7f09236dbc5f654a715c93e255'
        url = 'https://test.cashfree.com'
        appId = '60110871b19dcf536eba63ff401106'
        secretKey = '68f496d0a73be831c7a34cca3907425d00009c6f'
        orderId = ''.join(random.choices(string.ascii_uppercase +
                                         string.digits, k=10))
        data = {
            "appId": appId,
            "secretKey": secretKey,
            "orderId": orderId,
            "returnUrl": "https://kodecrux.herokuapp.com/order-successful/"+str(orderId)+"/"+str(educator)+"/",
            "orderAmount": order_amount,
            "customerName": request.data.get("customerName"),
            "customerPhone": request.data.get("customerPhone"),
            "customerEmail": request.data.get("customerEmail")
        }
        payment = requests.post(url+'/api/v1/order/create', data=data)
        response = json.loads(payment.text)
        # response.update({"orderId": data["orderId"]})
        # response.update({"url": request.scheme + "://" +
        #                  request.META["HTTP_HOST"] + "/order-successful/"+str(orderId)+"/"+str(educator)+"/"})
        return Response(response)

        # if payment.status_code == 200:
        #     data={
        #         "appId": appId,
        #     "secretKey": secretKey,
        #     "orderId": data["orderId"]
        #     }
        #     paymentStatus(url,data)

        # import razorpay
        # from rest_framework import permissions
        # client = razorpay.Client(auth=("rzp_test_LmOgpIykhftvK7",
        #     "rqWbFlWkSw3OaIeLZqEGgPFg"))
        #
        # client.set_app_details(
        #     {"title" : "CodeCrux",
        #     "version" : "3.1.3"})
        # from django.shortcuts import render
        #
        # # Create your views here.
        # from django.shortcuts import render
        # from rest_framework import viewsets
        # from . import serializers
        # from . import models
        # from rest_framework.response import Response
        # from django_filters.rest_framework import DjangoFilterBackend
        # from rest_framework.views import APIView
        # from django.http import HttpResponse
        #
        # class HireViewset(viewsets.ModelViewSet):
        #     queryset = models.Hire.objects.all()
        #     serializer_class = serializers.HireSerializer
        #     # filter_backends = [DjangoFilterBackend]
        #     # filterset_fields = ('user__technology', 'user__sub_technology', 'user__topic')
        #
        # class Order(APIView):
        # 	permission_classes = [permissions.AllowAny]
        # 	def get(self, request):
        # 		hire = models.Hire.objects.get(id=1)
        # 		order_amount = 1000
        # 		order_currency = 'INR'
        # 		order_receipt = str(hire.id)
        # 		# notes = {'Shipping address': 'Bommanahalli, Bangalore'}   # OPTIONAL
        # 		# reponse = client.order.create(amount=order_amount, currency=order_currency, receipt=order_receipt, )
        # 		print("sfs",dict(amount=order_amount, currency='INR', receipt=order_receipt,
        # 			payment_capture='1'))
        # 		response = client.order.create(dict(amount=order_amount, currency='INR', receipt=order_receipt,
        # 			payment_capture='1'))
        # 		print("self, ",response)
        # 		return HttpResponse(response)
        #
