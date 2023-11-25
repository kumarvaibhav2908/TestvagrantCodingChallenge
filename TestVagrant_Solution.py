Basket = [
    {"product": "Leather Wallet", "price": 1100, "gst": 18, "quant": 1},
    {"product": "Umbrella", "price": 900, "gst": 12, "quant": 4},
    {"product": "Cigarette", "price": 200, "gst": 28, "quant": 3},
    {"product": "Honey", "price": 100, "gst": 0, "quant": 2},
]

#Q1
print(" ")
print(" ")
print("Q1 Identify the product whichh we paid Maximum GST Amount")
print(" ")
max_gst = max(Basket, key=lambda x: x["price"] * x["gst"] / 100)
print(f"Product with maximum GST amount is {max_gst['product']}")
print(f"Unit price of the product is {max_gst['price']}")
print(" ")
print(" ")
#Q2
print("Q2 Calculate the total amount to be paid to the shopkeeper")
print(" ")
TOTAL_AMT = 0
for i in Basket:
    price = i["price"]
    gst = i["gst"]
    quant = i["quant"]
    total_price = price * (1 + gst/ 100)
    if price >= 500:
        total_price *= 0.95
    TOTAL_AMT += total_price * quant
print(f"Total amount to be paid: {TOTAL_AMT:.2f} RS.")
print(" ")
print(" ")


#VAIBHAV KUMAR(CSE) - 1BY20CS212
#College - BMS Institute of Technology & Management
#Year of Passing - 2024
#Phone Number - 8310969807
#E-mail - kumarvaibhav149@gmail.com