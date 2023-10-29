#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      HP
#
# Created:     29/10/2023
# Copyright:   (c) HP 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#task 3
class CarParkPaymentSystem:
    def __init__(self):
        self.prices = {
            "Sunday": (8, 2.0, 2.0),
            "Monday": (2, 10.0, 2.0),
            "Tuesday": (2, 10.0, 2.0),
            "Wednesday": (2, 10.0, 2.0),
            "Thursday": (2, 10.0, 2.0),
            "Friday": (2, 10.0, 2.0),
            "Saturday": (4, 3.0, 2.0)
        }
        self.discount_rate = 0.5
        self.daily_total = 0.0  # Initialize daily total to zero

    def calculate_price(self, day, arrival_hour, hours_parked, frequent_parking_number=None):
        if day not in self.prices:
            return "Invalid day"

        max_stay, price_per_hour, discount_hour = self.prices[day]

        arrival_hour = int(arrival_hour)  # Convert to integer
        hours_parked = int(hours_parked)  # Convert to integer

        if arrival_hour < 8 or arrival_hour >= discount_hour:
            discount_rate = 0.1
        else:
            discount_rate = self.discount_rate

        if arrival_hour < 16:  # Calculate price before 16:00
            price = min(hours_parked, max_stay) * price_per_hour * (1 - discount_rate)
        else:
            # Calculate price before 16:00
            price_before_4pm = min(16 - arrival_hour, max_stay) * price_per_hour * (1 - discount_rate)

            # Calculate price after 16:00
            price_after_4pm = max(hours_parked - (16 - arrival_hour), 0) * price_per_hour

            price = price_before_4pm + price_after_4pm

        return price

    def validate_frequent_parking_number(self, number):
        if number < 10000 or number >= 100000:
            return False

        check_digit = number % 10
        number_without_check_digit = number // 10

        total = 0
        factor = 1

        while number_without_check_digit > 0:
            digit = number_without_check_digit % 10
            total += digit * factor
            factor += 1
            number_without_check_digit //= 10

        calculated_check_digit = total % 11
        return calculated_check_digit == check_digit

    def process_customer_payment(self, price, amount_paid):
        if amount_paid >= price:
            self.daily_total += price
            return "Payment accepted. Thank you!"
        else:
            return "Insufficient payment. Please pay the correct amount."

    def end_of_day_report(self):
        return f"Daily Total: ${self.daily_total:.2f}"


# Example usage
if __name__ == "__main__":
    car_park = CarParkPaymentSystem()

    while True:
        day = input("Enter your day: ")
        arrival_hour = input("Enter your arrival hour: ")
        hours_parked = input("Enter your stay hours: ")
        frequent_parking_number = input("Enter your parking number: ")

        price = car_park.calculate_price(day, arrival_hour, hours_parked, frequent_parking_number)
        print(f"Price to pay: ${price:.2f}")

        amount_paid = float(input("Enter the amount you paid: "))
        result = car_park.process_customer_payment(price, amount_paid)
        print(result)

        more_customers = input("Is there another customer? (yes/no): ").lower()
        if more_customers != "yes":
            break

    end_of_day_total = car_park.end_of_day_report()
    print(end_of_day_total)

