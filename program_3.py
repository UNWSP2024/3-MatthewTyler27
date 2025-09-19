# Matthew Tyler
# 09/19/25
#Shipping Charges

def weight_conversion(weight):
    # Calculate the shipping charge for each weight range.
    shippingCost = 0.0
    if weight < 0:
        print("Weight cannot be less than zero")
        return 0.0
    if weight <= 2:
        shippingCost = weight * 1.50
    elif weight <= 6:
        shippingCost = weight * 3.00
    elif weight <= 10:
        shippingCost = weight * 4.00
    else: 
        shippingCost = weight * 4.75
    
    return shippingCost

#### This piece of the code has been done for you,
#### you only need to worry about the actual shipping 
#### charge logic in the weight_conversion function
if __name__ == '__main__':
    # Local variables
    weight = 0.0
    shippingCost = 0.0
    # Get package weight from the user.
    weight = float(input('Enter the weight of the package: '))
    # Display the shipping charge.
    shippingCost = weight_conversion(weight)
    print ('Shipping charge: $', format(shippingCost, '.2f'))
