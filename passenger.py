class Passenger:
    def __init__(
            self, 
            id=0, 
            name="", 
            phone="", 
            email=""
        ) -> None:
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email
        self.tickets = []

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_phone(self):
        return self.phone

    def get_email(self):
        return self.email
    
    def get_tickets(self):
        return self.tickets
    
    def set_name(self, name):
        self.name = name

    def set_phone(self, phone):
        self.phone = phone

    def set_email(self, email):
        self.email = email
    
    def book_ticket(self):
        """
        Passenger should be asked for the flight id. If that flight id is not found, the passenger should be notified. If the flight id is found, the passenger should be asked for the seat assignment. The seat assignment should be sent to the airline.
        """
        pass

    def request_cancelation(self):
        """
        Passenger should be asked for the ticket id to be cancelled. If that ticket id is not found, the passenger should be notified.
        If the ticket is found, the passenger should be asked if they want to cancel the ticket. If they do, the request for ticket cancellation should be sent to the airline.
        """
        pass

    def view_boarding_pass(self):
        """
        Passenger should be asked for the ticket id. If that ticket id is not found, the passenger should be notified. If the ticket id is found, the passenger should be notified of the boarding pass.
        """
        pass
    
    def __str__(self):
        """
        Returns a string representation of the passenger details.

        Returns:
            str: A formatted string containing passenger information.
        """
        return f"Passenger ID: {self.get_id()}\n" \
            f"Name: {self.get_name()}\n" \
            f"Phone: {self.get_phone()}\n" \
            f"Email: {self.get_email()}"