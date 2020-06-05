from django.db import models


class ReferralLinks(models.Model):
    refferal_id = models.IntegerField(blank=False, null=False)
    user_id = models.IntegerField(blank=False, null=False)
    user_name = models.CharField(max_length=50)

    class Meta:
        """providing indexing to optemize instanse search"""
        indexes = [models.Index(fields=['refferal_id'])]

    def __str__(self):
        return f'User: {self.user_name}. User ID: {self.user_id}. ' \
               f'Refferal ID: {self.refferal_id}'
