# Matthew Tyler
# 09/19/25
#Hot Dog

hotdog = 3.50
chillidog = 4.50
cheese = 0.50
peppers = 0.75
onions = 1.00

baseprice = 0.0
toppingprice = 0.0

def basetype():
  global baseprice
  dogtype = (input("What type of Dog do you want, 'hotdog' or 'chillidog'"))
  if dogtype == ("hotdog"):
    baseprice = hotdog
  elif dogtype == ("chillidog"):
    baseprice = chillidog


def toppingstype():
  global toppingprice
  toppingQuestion = input("Do you want toppings, 'yes' or 'no'?")
  if toppingQuestion == "no":
    print("ok")
    toppingprice = 0.0
  elif toppingQuestion == "yes":
    topping = input("Would you like 'cheese', 'peppers', or 'onions'?") 
    if topping == "cheese":
      toppingprice = cheese
    elif topping == "peppers":
      toppingprice = peppers
    elif topping == "onions":
      toppingprice = onions
    else:
      print("sorry we do not have that, no topping added")
      toppingprice = 0.0
      

def calculatePrice():
  subtotal = baseprice + toppingprice 
  Total = subtotal * 1.07
  print("Subtotal: $",subtotal)
  print("Total: $", format(Total, '.2f'))
  
basetype()
toppingstype()
calculatePrice()

    
    
