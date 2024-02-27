class Flight:
    def __init__(
            self, 
            flight_id=0, 
            departure_airport="", 
            arrival_airport="", 
            departure_time="", 
            arrival_time="", 
            gate_number=0, 
            seat_capacity=0
        ):
        self.flight_id = flight_id
        self.departure_airport = departure_airport
        self.arrival_airport = arrival_airport
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.gate_number = gate_number
        self.seat_capacity = seat_capacity

    def get_flight_id(self):
        return self.flight_id
    
    def get_departure_airport(self):
        return self.departure_airport
    
    def get_arrival_airport(self):
        return self.arrival_airport
    
    def get_departure_time(self):
        return self.departure_time
    
    def get_arrival_time(self):
        return self.arrival_time
    
    def get_gate_number(self):
        return self.gate_number
    
    def get_seat_capacity(self):
        return self.seat_capacity
    
    def set_flight_id(self, flight_id):
        self.flight_id = flight_id

    def set_departure_airport(self, departure_airport):
        self.departure_airport = departure_airport

    def set_arrival_airport(self, arrival_airport):
        self.arrival_airport = arrival_airport

    def set_departure_time(self, departure_time):
        self.departure_time = departure_time

    def set_arrival_time(self, arrival_time):
        self.arrival_time = arrival_time

    def set_gate_number(self, gate_number):
        self.gate_number = gate_number

    def set_seat_capacity(self, seat_capacity):
        self.seat_capacity = seat_capacity

    def __str__(self):
        """
        Returns a string representation of the flight details.

        Returns:
            str: A formatted string containing flight information.
        """
        return  f"Flight ID: {self.get_flight_id()}\n" \
            f"Departure Airport: {self.get_departure_airport()}\n" \
            f"Arrival Airport: {self.get_arrival_airport()}\n" \
            f"Departure Time: {self.get_departure_time()}\n" \
            f"Arrival Time: {self.get_arrival_time()}\n" \
            f"Gate Number: {self.get_gate_number()}\n" \
            f"Seat Capacity: {self.get_seat_capacity()}"