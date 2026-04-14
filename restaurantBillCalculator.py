SERVICE_CHARGE_RATE = 0.10  # Service charge is 10% of the meal cost
TAX_RATE = 0.05  # Tax is 5% of the amount after service charge
TIP_RATE = 0.05  # Tip is 5% of the amount after service charge

def calculate_restaurant_bill(meal_cost):
    
    print(f"Meal Cost: {meal_cost}")

    service_charge = meal_cost * SERVICE_CHARGE_RATE
    print(f"Service Charge (10%): {service_charge}")

    amount_after_service = meal_cost + service_charge
    print(f"Amount after service: {amount_after_service}")

    tax = amount_after_service * TAX_RATE
    print(f"Tax (5%): {tax}")

    tip = amount_after_service * TIP_RATE
    print(f"Tip (5%): {tip}")

    total_bill = amount_after_service + tax + tip
    print(f"Total Bill: {total_bill}")

calculate_restaurant_bill(int(input("Enter meal cost: ")))