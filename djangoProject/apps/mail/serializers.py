from rest_framework import serializers
from djangoProject.apps.mail.models import Letter, Parcel


class LetterSerializer(serializers.Serializer):
    sender = serializers.CharField(max_length=100)
    receiver = serializers.CharField(max_length=100)
    point_of_dispatch = serializers.CharField(max_length=100)
    point_of_receipt = serializers.CharField(max_length=100)
    index_dispatch = serializers.CharField(max_length=100)
    index_receipt = serializers.CharField(max_length=100)
    letter_type = serializers.IntegerField()
    weight = serializers.IntegerField()

    def create(self, validated_data):
        return Letter.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.sender = validated_data.get('sender', instance.sender)
        instance.receiver = validated_data.get('receiver', instance.receiver)
        instance.point_of_dispatch = validated_data.get('point_of_dispatch', instance.point_of_dispatch)
        instance.point_of_receipt = validated_data.get('point_of_dispatch', instance.point_of_receipt)
        instance.index_dispatch = validated_data.get('point_of_dispatch', instance.index_dispatch)
        instance.index_receipt = validated_data.get('index_receipt', instance.index_receipt)
        instance.letter_type = validated_data.get('letter_type', instance.letter_type)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.save()
        return instance


class ParcelSerializer(serializers.Serializer):
    sender = serializers.CharField(max_length=100)
    receiver = serializers.CharField(max_length=100)
    point_of_dispatch = serializers.CharField(max_length=100)
    point_of_receipt = serializers.CharField(max_length=100)
    index_dispatch = serializers.CharField(max_length=100)
    index_receipt = serializers.CharField(max_length=100)
    phone = serializers.CharField(max_length=11)
    parcel_type = serializers.IntegerField()
    amount = serializers.IntegerField()

    def create(self, validated_data):
        return Parcel.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.sender = validated_data.get('sender', instance.sender)
        instance.receiver = validated_data.get('receiver', instance.receiver)
        instance.point_of_dispatch = validated_data.get('point_of_dispatch', instance.point_of_dispatch)
        instance.point_of_receipt = validated_data.get('point_of_dispatch', instance.point_of_receipt)
        instance.index_dispatch = validated_data.get('point_of_dispatch', instance.index_dispatch)
        instance.index_receipt = validated_data.get('index_receipt', instance.index_receipt)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.parcel_type = validated_data.get('parcel_type', instance.parcel_type)
        instance.amount = validated_data.get('amount', instance.amount)
        instance.save()
        return instance