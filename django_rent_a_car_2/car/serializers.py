from rest_framework import serializers

from .models import Car, Reservation

class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = (
            'id',
            'plate_number',
            'brand',
            'model',
            'year',
            'gear',
            'rent_per_day',
            'availability',
        )
    
    #! In CarSerializers, we do not need to send the availability field to the customers in the data returned, there are two different ways for this:
    #? 1- Creating a separate serailzer for customers
    #? 2- Override the get_fields method

    def get_fields(self):

        fields = super().get_fields()  # We access the fields in class Meta
        request = self.context.get('request')
        if request.user and not request.user.is_staff:
            fields.pop('availability')
        return fields


class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = (
            'id',
            'customer',
            'car',
            'start_date',
            'end_date'
        )

        #! I need to validate the data coming from the frontend first, because I have specified my customer, start_date and end_date fields as unique in the models section:

        validators = [
            serializers.UniqueTogetherValidator(
                queryset = Reservation.objects.all(), 
                fields = ('customer', 'start_date', 'end_date'),
                message = 'You alreday have a reservation beetwen these dates.'            
            )
        ]