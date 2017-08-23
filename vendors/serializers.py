from rest_framework import serializers
from .models import Vendor
from .models import StatutoryRegistrations
from .models import ValidityOfLicences


class StatutoryRegistrationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = StatutoryRegistrations
        fields = '__all__'


class ValidityOfLicencesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ValidityOfLicences
        fields = '__all__'


class VendorSerializer(serializers.ModelSerializer):
    statutory_registrations = StatutoryRegistrationsSerializer(many=False)
    validity_of_licences = ValidityOfLicencesSerializer(many=False)

    class Meta:
        model = Vendor
        fields = '__all__'

    def create(self, validated_data):
        statutory_registrations_data = validated_data.pop('statutory_registrations', None)
        validity_of_licences_data = validated_data.pop('validity_of_licences', None)

        statutory_registrations_data = StatutoryRegistrations.objects.create(**statutory_registrations_data)
        validity_of_licences_data = ValidityOfLicences.objects.create(**validity_of_licences_data)

        vendor = Vendor.objects.create(**validated_data)
        vendor.statutory_registrations = statutory_registrations_data
        vendor.validity_of_licences = validity_of_licences_data

        vendor.save()

        return vendor

    def update(self, instance, validated_data):
        statutory_registrations_data = validated_data.pop('statutory_registrations', None)
        validity_of_licences_data = validated_data.pop('validity_of_licences', None)

        StatutoryRegistrations.objects.select_for_update().filter(id=instance.statutory_registrations.id).update(**statutory_registrations_data)
        ValidityOfLicences.objects.select_for_update().filter(id=instance.validity_of_licences.id).update(**validity_of_licences_data)

        Vendor.objects.select_for_update().filter(id=instance.id).update(**validated_data)

        return Vendor.objects.get(id=instance.id)

