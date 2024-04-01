"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

# from web_site.views import RolesApiView, UsersApiView
# from web_site import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("users.urls")),
    path("loans/", include("loans.urls")),
    path("payments/", include("payments.urls")),
    # # Login and signup urls
    # path("", views.index),
    # path("web_site/signup", views.signup),
    # path("web_site/login", UsersApiView.as_view()),
    # # CRUD urls for roles
    # path("web_site/roles", RolesApiView.as_view()),
    # path("web_site/role/<int:id>", RolesApiView.as_view()),
    # path("web_site/role/add", RolesApiView.as_view()),
    # path("web_site/role/update/<int:id>", RolesApiView.as_view()),
    # path("web_site/role/delete/<int:id>", RolesApiView.as_view()),
    # CRUD urls for borrowers
    # CRUD urls for user_activity_log
    # CRUD urls for loan_applications
    # CRUD urls for loans
    # CRUD urls for collaterals
    # CRUD urls for loan_history
    # CRUD urls for loan_repayment_schedule
    # CRUD urls for loan_approval_history
    # CRUD urls for payments
    # CRUD urls for loan_documents
    # CRUD urls for late_payments
    # CRUD urls for loan_audit_trail
    # CRUD urls for loan_comments
]
