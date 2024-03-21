from django.db import models


# Create your models here.
class Roles(models.Model):
    id = models.AutoField(primary_key=True)
    role_name = models.CharField(max_length=255, null=False)


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100, null=False)
    role_id = models.ForeignKey("Roles", on_delete=models.CASCADE)
    is_approved = models.BooleanField(default=False)


class Borrowers(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey("Users", on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False)
    email = models.CharField(max_length=255, unique=True, null=False)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()


class User_Activity_Log(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey("Users", on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100, null=False)
    description = models.TextField()
    activity_date = models.DateTimeField()


# enum for application status field
APPLICATION_STATUS_CODES = ((0, "pending"), (1, "approved"), (2, "rejected"))


class Loan_Applications(models.Model):
    id = models.AutoField(primary_key=True)
    borrower_id = models.ForeignKey("Borrowers", on_delete=models.CASCADE)
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
    borrower_id = models.ForeignKey("Borrowers", on_delete=models.CASCADE)
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


# Enum for status codes
PAYMENT_CODES = ((0, "pending"), (1, "paid"))


class Loan_Repayment_Schedule(models.Model):
    id = models.AutoField(primary_key=True)
    loan_id = models.ForeignKey("Loans", on_delete=models.CASCADE)
    installment_number = models.IntegerField(null=False)
    due_date = models.DateField(null=False)
    amount_due = models.FloatField(null=False)
    status = models.CharField(max_length=1, choices=PAYMENT_CODES, default="0")


# enum for approval codes
APPROVAL_CODES = ((0, "rejected"), (1, "approved"))


class Loan_Approval_History(models.Model):
    id = models.AutoField(primary_key=True)
    loan_id = models.ForeignKey("Loans", on_delete=models.CASCADE)
    approval_date = models.DateField(null=False)
    approved_by_user_id = models.ForeignKey("Users", on_delete=models.CASCADE)
    status = models.CharField(max_length=1, choices=APPROVAL_CODES)
    comments = models.TextField()


class Payments(models.Model):
    id = models.AutoField(primary_key=True)
    loan_id = models.ForeignKey("Loans", on_delete=models.CASCADE)
    amount = models.FloatField(null=False)
    payment_date = models.DateField(null=False)


class Loan_Documents(models.Model):
    id = models.AutoField(primary_key=True)
    loan_id = models.ForeignKey("Loans", on_delete=models.CASCADE)
    document_name = models.CharField(max_length=255, null=False)
    document_path = models.CharField(max_length=255, null=False)
    upload_date = models.DateField(null=False)


class Late_Payments(models.Model):
    id = models.AutoField(primary_key=True)
    loan_id = models.ForeignKey("Loans", on_delete=models.CASCADE)
    payment_id = models.ForeignKey("Payments", on_delete=models.CASCADE)
    late_fee = models.FloatField(null=False)
    late_fee_paid_date = models.DateField()


class Loan_Audit_Trail(models.Model):
    id = models.AutoField(primary_key=True)
    loan_id = models.ForeignKey("Loans", on_delete=models.CASCADE)
    event_type = models.CharField(max_length=255, null=False)
    description = models.TextField()
    event_date = models.DateTimeField(null=False)


class Loan_Comments(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey("Users", on_delete=models.CASCADE)
    loan_id = models.ForeignKey("Loans", on_delete=models.CASCADE)
    comments = models.TextField(null=False)
    comment_date = models.DateTimeField(null=False)
