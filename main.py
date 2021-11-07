print("welcome to python pizza")
size = str(input("what size pizza  do you want ? S , M & L : "))
odd_pepperoni = str(input("Do you want pepperoni ? Y & N : "))
extra_cheese =  str(input("Do you want extra cheese ?  Y or N : "))
if(size == "S"):
  pizza = 15
elif(size == "M"):
  pizza = 20
else:
  pizza = 25

if(odd_pepperoni == "Y"):
  if(size == "S"):
    pizza +=2
  else:
    pizza +=3

if(extra_cheese == "Y"):
  pizza +=1

gst = str(input("do you have include GST? Y | N : "))
if(gst == "Y"):
 gst = round(pizza * 0.12, 2)

final= pizza + gst
print("your pizza is {0}".format(pizza))
print("include gst is {0}".format(gst))
print("your final bill is {0}".format(final))