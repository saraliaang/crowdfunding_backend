from rest_framework import serializers
from django.apps import apps

class FundraiserSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = apps.get_model('fundraisers.Fundraiser')
        fields = '__all__'
        #we want to serialize all the fields

class PledgeSerilaizer(serializers.ModelSerializer):
    supporter = serializers.ReadOnlyField(source='supporter.id')
    class Meta:
        model = apps.get_model('fundraisers.Pledge')
        fields= '__all__'

class FundraiserDetialSerializer(FundraiserSerializer):
    pledges = PledgeSerilaizer(many=True, read_only=True)

#when we taking in something for class, it means inheretance, whearas in funciton, it measn parameter 