from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Fundraiser, Pledge
from .serializers import FundraiserSerializer, PledgeSerilaizer, FundraiserDetialSerializer

class FundraiserList(APIView):
    def get(self, request):
        fundraisers = Fundraiser.objects.all()
        serializer = FundraiserSerializer(fundraisers, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = FundraiserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
class FundraiserDetail(APIView):
    def get_object(self,pk):
        try:
            fundraiser = Fundraiser.objects.get(pk=pk)
            return fundraiser
        except Fundraiser.DoesNotExist:
            raise Http404
            
    def get(self, request, pk):
        fundraiser = self.get_object(pk)
        serializer = FundraiserDetialSerializer(fundraiser)
        return Response(serializer.data)

class PledgeList(APIView):
    def get(self, request):
        pledges = Pledge.objects.all()
        serializer = PledgeSerilaizer(pledges, many =True)
        return Response(serializer.data)
    

    def post(self, request):
        serializer = PledgeSerilaizer(data=request.data)
        if serializer.is_valid():
            serializer.save(supporter=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

class PledgeDetail(APIView):
    def get_pledge(self,pk):
        try:    
            pledge = Pledge.objects.get(pk=pk)
            return pledge
        except Pledge.DoesNotExist:
            raise Http404
        
    def get(self,request,pk):
        pledge = self.get_pledge(pk)
        serialized = PledgeSerilaizer(pledge)
        return Response(serialized.data)
        



#seperat get() and get_object() because:Its only job is to fetch one Fundraiser from the DB or raise Http404.

# It’s reusable: if later you want to implement PUT (update) or DELETE in the same view, you can call self.get_object(pk) again, instead of repeating the query and error handling logic.

# Keeps database lookup logic in one place.