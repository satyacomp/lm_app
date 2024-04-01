from rest_framework import serializers
from .models import *


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


class LoanApprovalHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan_Approval_History
        fields = "__all__"


class LoanDocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan_Documents
        fields = "__all__"


class LoanAuditTrailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan_Audit_Trail
        fields = "__all__"


class LoanComments(serializers.ModelSerializer):
    class Meta:
        model = Loan_Comments
        fields = "__all__"
