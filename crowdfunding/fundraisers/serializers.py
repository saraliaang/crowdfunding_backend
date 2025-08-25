from rest_framework import serializers
from .models import Pledge, Fundraiser

class FundraiserSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    amount_raised = serializers.ReadOnlyField()
    total_lightyear = serializers.ReadOnlyField()
    current_lightyear = serializers.ReadOnlyField()
    target = serializers.ReadOnlyField() 


    class Meta:
        model = Fundraiser
        fields = '__all__'
        #we want to serialize all the fields

class PledgeSerilaizer(serializers.ModelSerializer):
    supporter = serializers.ReadOnlyField(source='supporter.id')
    class Meta:
        model = Pledge
        fields= '__all__'

class FundraiserDetialSerializer(FundraiserSerializer):
    pledges = PledgeSerilaizer(many=True, read_only=True)


#when we taking in something for class, it means inheretance, whearas in funciton, it measn parameter 
#create FundraiserSerializer then FundraiserDetialSerializer is because we only want to see the detail of pledges when one fundraiser is pulled. To prevent the bloating of base serializer