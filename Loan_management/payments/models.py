from django.db import models
from loans.models import *
from users.models import *

# Create your models here.
# Enum for status codes
PAYMENT_CODES = ((0, "pending"), (1, "paid"))


class Loan_Repayment_Schedule(models.Model):
    id = models.AutoField(primary_key=True)
    loan_id = models.ForeignKey("loans.Loans", on_delete=models.CASCADE)
    installment_number = models.IntegerField(null=False)
    due_date = models.DateField(null=False)
    amount_due = models.FloatField(null=False)
    status = models.CharField(max_length=1, choices=PAYMENT_CODES, default="0")


class Payments(models.Model):
    id = models.AutoField(primary_key=True)
    loan_id = models.ForeignKey("loans.Loans", on_delete=models.CASCADE)
    amount = models.FloatField(null=False)
    payment_date = models.DateField(null=False)


class Late_Payments(models.Model):
    id = models.AutoField(primary_key=True)
    loan_id = models.ForeignKey("loans.Loans", on_delete=models.CASCADE)
    payment_id = models.ForeignKey("Payments", on_delete=models.CASCADE)
    late_fee = models.FloatField(null=False)
    late_fee_paid_date = models.DateField()
