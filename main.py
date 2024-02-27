from passenger import Passenger
from flight import Flight
from ticket import Ticket
from boarding_pass import BoardingPass

passenger1 = Passenger(1, "Alice Smith", "12345678", "smith@example.com")
passenger2 = Passenger(2, "Bob Jones", "11221122", "rock@example.com")

# print(passenger1) 

flight1 = Flight(flight_id="FL123", departure_airport="LAX", arrival_airport="JFK", departure_time="2024-02-25 10:00", arrival_time="2024-02-25 15:00", gate_number=3, seat_capacity=150)

# print(flight1)

ticket1 = Ticket(number=1, passenger=passenger1, flight=flight1, fare_class="Economy", seat_assigned="A1", departure_city="Los Angeles", arrival_city="New York")

# print(ticket1)

boarding_pass1 = BoardingPass(ticket=ticket1)

print(boarding_pass1)
