from rest_framework import serializers

from quotations import models as quotation_models


class KeyedListSerializerSerializer(serializers.ModelSerializer):

    def to_representation(self, data):
        response = super().to_representation(data)
        key = response.pop('id')
        return {key: response}


class AuthorCreateSerializer(serializers.ModelSerializer):
    tag_values = serializers.ListField(write_only=True)

    class Meta:
        model = quotation_models.Author
        fields = ('name', 'date_of_birth', 'date_of_death', 'tag_values')
        extra_kwargs = {
            'name': {'validators': []},
        }

    def create(self, validated_data):
        tag_data = validated_data.pop('tag_values')
        author, created = quotation_models.Author.objects.get_or_create(**validated_data)
        for tag_value in tag_data:
            tag, created = quotation_models.Tag.objects.get_or_create(value=tag_value)
            author.tags.add(tag)
        return author


# Can be used to create a quotation with author name and tag values.
# Will find existing author and tags if possible, otherwise will create new.
class QuotationAuthorCreateSerializer(serializers.ModelSerializer):
    author = AuthorCreateSerializer()

    class Meta:
        model = quotation_models.Quotation
        fields = ['text', 'author']

    def create(self, validated_data):
        author_data = validated_data.pop('author')
        author_serializer = AuthorCreateSerializer(data=author_data)
        author = author_serializer.create(author_data)
        quotation = quotation_models.Quotation.objects.create(author=author, **validated_data)
        return quotation


# Can be used to create a quotation by referencing an existing author id.
class QuotationCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = quotation_models.Quotation
        fields = '__all__'


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


class AuthorDetailSerializer(serializers.ModelSerializer):
    underquoted = QuotationSerializer(many=True, read_only=True)

    class Meta:
        model = quotation_models.Author
        fields = ('id', 'name', 'underquoted',)


class AuthorQuotationsSerializer(KeyedListSerializerSerializer):
    underquoted = QuotationOnlySerializer(many=True, read_only=True)

    class Meta:
        model = quotation_models.Author
        fields = ('id', 'name', 'underquoted',)
