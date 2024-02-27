import datetime

class BoardingPass:
    def __init__(
            self,  
            ticket=None
        ):
        self.ticket = ticket
        self.boarding_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    def get_boarding_time(self):
        return self.boarding_time
    
    def get_ticket(self):
        return self.ticket

    def __str__(self):
        """
        Returns a string representation of the boarding pass details.

        Returns:
            str: A formatted string containing boarding pass information.
        """
        return f"Passenger Name: {self.ticket.passenger.get_name()}\n" \
            f"Passenger ID: {self.ticket.passenger.get_id()}\n" \
            f"Flight ID: {self.ticket.flight.get_flight_id()}\n" \
            f"Boarding Time: {self.get_boarding_time()}\n" \
            f"Gate Number: {self.ticket.flight.get_gate_number()}\n" \
            f"Departure Airport: {self.ticket.flight.get_departure_airport()}\n" \
            f"Arrival Airport: {self.ticket.flight.get_arrival_airport()}\n" \
            f"Departure Time: {self.ticket.flight.get_departure_time()}\n" \
            f"Arrival Time: {self.ticket.flight.get_arrival_time()}\n" \
            f"Ticket Number: {self.ticket.get_ticket_number()}\n" \
            f"Seat: {self.ticket.get_seat()}\n" \
            f"Fare Class: {self.ticket.get_fare_class()}\n" \
            f"Departure City: {self.ticket.get_departure_city()}\n" \
            f"Arrival City: {self.ticket.get_arrival_city()}"