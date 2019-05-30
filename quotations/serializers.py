from rest_framework import serializers

from quotations import models as quotation_models


class QuotationSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = quotation_models.Quotation
        fields = '__all__'


class QuotationOnlySerializer(serializers.ModelSerializer):

    class Meta:
        model = quotation_models.Quotation
        fields = ('text',)


class AuthorSummarySerializer(serializers.ModelSerializer):
    total_quotations = serializers.IntegerField(read_only=True)

    class Meta:
        model = quotation_models.Author
        fields = ('name', 'total_quotations',)


class AuthorQuotationsSerializer(serializers.ModelSerializer):
    underquoted = QuotationOnlySerializer(many=True, read_only=True)

    class Meta:
        model = quotation_models.Author
        fields = ('name', 'underquoted',)
