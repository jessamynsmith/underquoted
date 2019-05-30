from rest_framework import serializers

from quotations import models as quotation_models


class KeyedListSerializerSerializer(serializers.ModelSerializer):

    def to_representation(self, data):
        response = super().to_representation(data)
        key = response.pop('id')
        return {key: response}


class QuotationSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = quotation_models.Quotation
        fields = '__all__'


class QuotationOnlySerializer(KeyedListSerializerSerializer):

    class Meta:
        model = quotation_models.Quotation
        fields = ('id', 'text',)


class AuthorSummarySerializer(serializers.ModelSerializer):
    total_quotations = serializers.IntegerField(read_only=True)

    class Meta:
        model = quotation_models.Author
        fields = ('name', 'total_quotations',)


class AuthorQuotationsSerializer(KeyedListSerializerSerializer):
    underquoted = QuotationOnlySerializer(many=True, read_only=True)

    class Meta:
        model = quotation_models.Author
        fields = ('id', 'name', 'underquoted',)
