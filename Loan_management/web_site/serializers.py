from rest_framework import serializers
from .models import *


class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = "__all__"


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"


class BorrowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrowers
        fields = "__all__"


class UserActivityLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrowers
        fields = "__all__"


class LoanApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan_Applications
        fields = "__all__"


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loans
        fields = "__all__"


class CollateralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collaterals
        fields = "__all__"


class LoanHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan_History
        fields = "__all__"


class LoanRepaymentScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan_Repayment_Schedule
        fields = "__all__"


class LoanApprovalHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan_Approval_History
        fields = "__all__"


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = "__all__"


class LoanDocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan_Documents
        fields = "__all__"


class LatePaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Late_Payments
        fields = "__all__"


class LoanAuditTrailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan_Audit_Trail
        fields = "__all__"
