from rest_framework import serializers

from quotations import models as quotation_models


class QuotationSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = quotation_models.Quotation
        fields = '__all__'


class AuthorSummarySerializer(serializers.ModelSerializer):
    total_quotations = serializers.IntegerField(read_only=True)

    class Meta:
        model = quotation_models.Author
        fields = ('name', 'total_quotations',)
