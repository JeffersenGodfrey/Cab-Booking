class Cab:

    #initialization of cab details
    def __init__(self, cab_id, cab_type, driver_name, rate_per_km):
        self.cab_id = cab_id
        self.cab_type = cab_type
        self.driver_name = driver_name
        self.rate_per_km = rate_per_km
        self.is_available = True
    #show cab info
    def show_info(self):
        status= "Available" if self.is_available else "Booked!"
        print(f"Cab ID: {self.cab_id}, Type: {self.cab_type}, Driver: {self.driver_name}, Rate per km: {self.rate_per_km}, Status: {status}")


class Booking:

    #initialize booking manager with cab list
    def __init__(self):
        self.cabs=[
            Cab(1, "Sedan", "Ramesh", 10),
            Cab(2, "SUV", "Suresh", 12),
            Cab(3, "Hatchback", "Naresh", 8)
        ]   

    #display all cabs 
    def show_all_cabs(self):
        print("\n Available cabs: \n")
        for cab in self.cabs:
            cab.show_info()
           
    #book a cab
    def book_cab(self):
        cab_id = int(input("Enter cab ID to book: "))
        distance = float(input("Enter distance (km): "))
        for cab in self.cabs:
            if cab.cab_id == cab_id and cab.is_available:
                fare = distance * cab.rate_per_km if cab.cab_type == "Sedan" else distance * cab.rate_per_km * 1.5
                cab.is_available = False
                print(f"Cab {cab_id} booked successfully!")
                return
        print("Cab not available or invalid cab ID.")

    #cancel a booking
    def cancel_booking(self):
        cab_id = int(input("Enter cab ID to cancel booking: "))
        for cab in self.cabs:
            if cab.cab_id == cab_id and not cab.is_available:
                cab.is_available = True
                print(f"Booking for cab {cab_id} cancelled successfully!")  
                return
        print("Invalid cab ID or cab not booked.")   

#Run the CLI menu

def main():

    booking = Booking()
    while True:
        print("\n Cab Booking System")
        print("1. Show all cabs")
        print("2. Book a cab")
        print("3. Cancel booking")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            booking.show_all_cabs()
        elif choice == "2":
            booking.book_cab()
        elif choice == "3":
            booking.cancel_booking()
        elif choice == "4":
            print("Thank You for using cab app")
            break
        else:
            print("Invalid choice. Please try again.")        

#Entry point of the app
if __name__ == "__main__":
    main()                    