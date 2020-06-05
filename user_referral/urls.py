from django.urls import path
from .views import ReferralLinksDetail

urlpatterns = [
    path('refferal_link/<int:refferal_id>/', ReferralLinksDetail.as_view(), name='refferal_link')
]
