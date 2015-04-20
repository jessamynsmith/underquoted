from rest_framework import serializers

from underquoted.apps.quotations import models as quotation_models


class QuotationSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = quotation_models.Quotation
