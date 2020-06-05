from .models import ReferralLinks
from .serializers import ReferralLinksSerializer
from rest_framework import generics


class ReferralLinksDetail(generics.RetrieveUpdateDestroyAPIView):
    """Endpoint to get or delete ReferralLinks instanses"""
    queryset = ReferralLinks.objects.all()
    serializer_class = ReferralLinksSerializer
    lookup_field = 'refferal_id'  # changed field to look on in url parameters and filer ReferralLinks table
