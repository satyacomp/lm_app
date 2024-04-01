from django.db import models
from users.models import *


# Create your models here.
# enum for application status field
APPLICATION_STATUS_CODES = ((0, "pending"), (1, "approved"), (2, "rejected"))


class Loan_Applications(models.Model):
    id = models.AutoField(primary_key=True)
    borrower_id = models.ForeignKey("users.Borrowers", on_delete=models.CASCADE)
    amount = models.FloatField(null=False)
    purpose = models.CharField(max_length=255)
    application_date = models.DateTimeField(null=False)
    application_status = models.CharField(
        max_length=1, choices=APPLICATION_STATUS_CODES, default="0"
    )


# enum for loan_status
LOAN_STATUS_CODES = ((0, "active"), (1, "closed"))


class Loans(models.Model):
    id = models.AutoField(primary_key=True)
    borrower_id = models.ForeignKey("users.Borrowers", on_delete=models.CASCADE)
    loan_application_id = models.ForeignKey(
        "Loan_Applications", on_delete=models.CASCADE
    )
    amount = models.FloatField(null=False)
    interest_rate = models.FloatField(null=False)
    term_months = models.IntegerField(null=False)
    start_date = models.DateField(null=False)
    status = models.CharField(max_length=1, choices=LOAN_STATUS_CODES, default="0")


class Collaterals(models.Model):
    id = models.AutoField(primary_key=True)
    loan_id = models.ForeignKey("Loans", on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    estimated_value = models.FloatField()


class Loan_History(models.Model):
    id = models.AutoField(primary_key=True)
    loan_id = models.ForeignKey("Loans", on_delete=models.CASCADE)
    event_date = models.DateTimeField()
    description = models.TextField()


# enum for approval codes
APPROVAL_CODES = ((0, "rejected"), (1, "approved"))


class Loan_Approval_History(models.Model):
    id = models.AutoField(primary_key=True)
    loan_id = models.ForeignKey("Loans", on_delete=models.CASCADE)
    approval_date = models.DateField(null=False)
    approved_by_user_id = models.ForeignKey("users.Users", on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=APPROVAL_CODES)
    comments = models.TextField()


class Loan_Documents(models.Model):
    id = models.AutoField(primary_key=True)
    loan_id = models.ForeignKey("Loans", on_delete=models.CASCADE)
    document_name = models.CharField(max_length=255, null=False)
    document_path = models.CharField(max_length=255, null=False)
    upload_date = models.DateField(null=False)


class Loan_Audit_Trail(models.Model):
    id = models.AutoField(primary_key=True)
    loan_id = models.ForeignKey("Loans", on_delete=models.CASCADE)
    event_type = models.CharField(max_length=255, null=False)
    description = models.TextField()
    event_date = models.DateTimeField(null=False)


class Loan_Comments(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey("users.Users", on_delete=models.CASCADE)
    loan_id = models.ForeignKey("Loans", on_delete=models.CASCADE)
    comments = models.TextField(null=False)
    comment_date = models.DateTimeField(null=False)
