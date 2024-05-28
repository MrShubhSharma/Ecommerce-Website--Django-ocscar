from django.urls import path
from .views import PaymentDetailsView, PaymentMethodView

urlpatterns = [
    path('payment-method/', PaymentMethodView.as_view(), name='payment-method'),
    path('payment-details/', PaymentDetailsView.as_view(), name='payment-details'),
]
