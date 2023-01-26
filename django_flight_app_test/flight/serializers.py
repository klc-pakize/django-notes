from rest_framework import serializers

from .models import Flight, Passenger, Reservation

class FlightSerializer(serializers.ModelSerializer):


    class Meta:
        model = Flight
        fields = (
            'id',
            'flight_number',
            'operation_arirline',
            'departure_city',
            'arrival_city',
            'date_of_departure',
            'etd',
        )

class PassengerSerializer(serializers.ModelSerializer):


    class Meta:
        model = Passenger
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'create_date',
        )


class ReservationSerializer(serializers.ModelSerializer):

    passenger = PassengerSerializer(many=True, required=True)
    flight = serializers.StringRelatedField()
    flight_id = serializers.IntegerField()
    user = serializers.StringRelatedField()

    class Meta:
        model = Reservation
        fields = ("id", "flight", "flight_id", "user", "passenger")

    def create(self, validated_data):
        passenger_data = validated_data.pop("passenger")
        validated_data["user_id"] = self.context["request"].user.id  # This is how we can get the id of the requesting user.
        reservation = Reservation.objects.create(**validated_data)

        for passenger in passenger_data:
            pas = Passenger.objects.create(**passenger)
            reservation.passenger.add(pas)  # We did the ManyToMany merge

        reservation.save()
        return reservation


#! We have created StaffReservationSerializers so that the User staff can see the reservation in the flight.

class StaffReservationSerializers(serializers.ModelSerializer):

    reservation = ReservationSerializer(many = True, read_only = True)
    
    class Meta:
        model = Flight
        fields = (
            'id',
            'flight_number',
            'operation_arirline',
            'departure_city',
            'arrival_city',
            'date_of_departure',
            'etd',
            'reservation',
        )
        