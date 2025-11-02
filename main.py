from pyscript import document, display

restaurant_name = "Bistro Del Sol"
owner_name = "Maria Santos"
year_established = 2015
popular_item_price = 249.50
has_delivery = True
product_names = ["Pasta Primavera", "Beef Tapa", "Mango Cheesecake"]

business_hours = {
    "opening": "8:00 AM",
    "closing": "10:00 PM"
}
menu_prices = {
    "Pasta Primavera": 249.50,
    "Beef Tapa": 199.00,
    "Mango Cheesecake": 175.00,
    "Iced Latte": 120.00,
    "Lemon Iced Tea": 90.00
}
common_allergens = ["Dairy", "Gluten", "Peanuts"]
tax_rate = 0.08
print(f"Welcome to {restaurant_name} owned by {owner_name}!")
print(f"Established in {year_established}.")
print(f"Our popular item: {product_names[0]} - ₱{popular_item_price}")
print(f"Open from {business_hours['opening']} to {business_hours['closing']}.")
print(f"Delivery Available: {has_delivery}")
