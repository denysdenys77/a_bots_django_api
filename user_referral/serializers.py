from rest_framework import serializers
from .models import ReferralLinks


class ReferralLinksSerializer(serializers.ModelSerializer):
    """serializer class to deal with ReferralLinks"""

    class Meta:
        model = ReferralLinks
        fields = [
            'id',
            'refferal_id',
            'user_id',
            'user_name',
        ]
