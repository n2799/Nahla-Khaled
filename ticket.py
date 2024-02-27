class Ticket:
    def __init__(
            self, 
            number=0, 
            passenger=None, 
            flight=None, 
            seat_assigned=0, 
            fare_class="", 
            departure_city="", 
            arrival_city=""
        ):
        self.ticket_number = number
        self.passenger = passenger
        self.flight = flight
        self.seat_assigned = seat_assigned
        self.fare_class = fare_class
        self.departure_city = departure_city
        self.arrival_city = arrival_city

    def get_departure_city(self):
        return self.departure_city

    def get_arrival_city(self):
        return self.arrival_city

    def get_ticket_number(self):
        return self.ticket_number
    
    def get_passenger(self):
        return self.passenger
    
    def get_flight(self):
        return self.flight
    
    def get_seat(self):
        return self.seat_assigned
    
    def get_fare_class(self):
        return self.fare_class
    
    def set_seat_number(self, seat_number):
        self.number = seat_number
    
    def set_passenger(self, passenger):
        self.passenger = passenger
    
    def set_flight(self, flight):
        self.flight = flight
    
    def set_seat(self, seat_assigned):
        self.gate_number = seat_assigned
    
    def set_fare_class(self, fare_class):
        self.fare_class = fare_class

    def __str__(self):
        """
        Returns a string representation of the ticket details.

        Returns:
            str: A formatted string containing ticket information.
        """
        return f"Ticket Number: {self.get_ticket_number()}\n" \
            f"Passenger: {self.get_passenger()}\n" \
            f"Flight: {self.get_flight()}\n" \
            f"Seat Assigned: {self.get_seat()}\n" \
            f"Fare Class: {self.get_fare_class()}\n" \
            f"Departure City: {self.get_departure_city()}\n" \
            f"Arrival City: {self.get_arrival_city()}"