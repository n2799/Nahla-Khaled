class Admin:
    def __init__(
            self, 
            id = 0, 
            name="", 
            phone="",
            email=""
        ):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email

    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name
    
    def get_phone(self):
        return self.phone
    
    def get_email(self):
        return self.email

    def add_flight_information(self, flight_id, departure_airport, arrival_airport,
                              departure_time, arrival_time, gate_number, seat_capacity):
        """
        Add flight information to your system. 
        """
        pass

    def cancel_flight(self, flight_id):
        """Admin will take the id of flight and cancels the flight if it exists."""
        pass

    def update_flight_information(self, flight_id, new_departure_time=None, new_arrival_time=None,
                                  new_gate_number=None):
        """Admin will take the required information and update the flight info"""
        pass

    def issue_boarding_pass(self, passenger_id, flight_id):
        """Once the flight and passenger details are confirmed, admin will issue the boarding pass to the passenger for the selected flight"""
        pass

    def __str__(self):
        """
        Returns a string representation of the admin details.

        Returns:
            str: A formatted string containing admin information.
        """
        return f"Admin ID: {self.get_id()}\n" \
            f"Name: {self.get_name()}\n" \
            f"Phone: {self.get_phone()}\n" \
            f"Email: {self.get_email()}"