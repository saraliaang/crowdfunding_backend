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

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance


    

#when we taking in something for class, it means inheretance, whearas in funciton, it measn parameter 
#create FundraiserSerializer then FundraiserDetialSerializer is because we only want to see the detail of pledges when one fundraiser is pulled. To prevent the bloating of base serializer