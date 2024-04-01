from .models import *
from rest_framework import serializers


class LoanRepaymentScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan_Repayment_Schedule
        fields = "__all__"


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = "__all__"


class LatePaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Late_Payments
        fields = "__all__"
