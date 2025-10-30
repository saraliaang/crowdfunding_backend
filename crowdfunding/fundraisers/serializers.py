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

class PledgeSerializer(serializers.ModelSerializer):
    supporter = serializers.ReadOnlyField(source='supporter.id')
    supporter_username = serializers.ReadOnlyField(source='supporter.username')
    class Meta:
        model = Pledge
        fields= '__all__'

class FundraiserDetialSerializer(FundraiserSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.image = validated_data.get('image', instance.image)
        # instance.is_open = validated_data.get('is_open', instance.is_open)
        # instance.destination_year = validated_data.get('destination_year', instance.destination_year)
        # instance.target = validated_data.get('target', instance.target)
        instance.save()
        return instance
    

class PledgeDetailSerializer(PledgeSerializer):
    fundraiser = FundraiserSerializer(read_only=True)   # override

    def update(self, instance, validated_data):
        instance.anonymous = validated_data.get('anonymous', instance.anonymous)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.save()
        return instance


    

#when we taking in something for class, it means inheretance, whearas in funciton, it measn parameter 
#create FundraiserSerializer then FundraiserDetialSerializer is because we only want to see the detail of pledges when one fundraiser is pulled. To prevent the bloating of base serializer