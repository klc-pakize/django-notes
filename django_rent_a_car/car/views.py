from django.shortcuts import render
from django.db.models import Q

from rest_framework.viewsets import ModelViewSet

from .models import Car, Reservation
from .serializers import CarSerializer
from .permissions import IsStaffOrReadOnly

# Create your views here.

class CarView(ModelViewSet):

    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsStaffOrReadOnly]

    def get_queryset(self):
        
        #! Users who are admin will be able to view all Car 
        if self.request.user.is_staff:
            queryset = super().get_queryset()
        
        #! Non-admin users will only be able to view cars with availability = True
        else:
            queryset = super().get_queryset().filter(availability = True)
        
        #! We do a detailed filtering with query_params:
        start = self.request.query_params.get('start')
        print(start)
        end = self.request.query_params.get('end')
        print(end)

        #! Method to list cars that have no reservations between the dates entered by the user
        con1 = Q(start_date__lt = end)
        con2 = Q(end_date__gt = start)
        not_avilable = Reservation.objects.filter(con1 & con2).values_list('car_id', flat = True)

        queryset = queryset.exclude(id__in = not_avilable)
        return queryset
