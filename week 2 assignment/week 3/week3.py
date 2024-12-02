def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount if the discount is 20% or higher.
    
    Parameters:
        price (float): The original price of the item.
        discount_percent (float): The discount percentage to be applied.
        
    Returns:
        float: The final price after the discount (if applicable), or the original price.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    return price

# Main program to interact with the user
try:
    # Get user input for price and discount percentage
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    # Calculate the final price
    final_price = calculate_discount(original_price, discount_percentage)
    
    # Print the result
    if final_price < original_price:
        print(f"The final price after applying the discount is: ${final_price:.2f}")
    else:
        print(f"No discount applied. The original price remains: ${original_price:.2f}")
except ValueError:
    print("Please enter valid numerical values for price and discount percentage.")
