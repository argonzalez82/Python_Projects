# hour_2_exercise
# Chapter 2 page26
# small program to figure total price including discount

supplies_cost =10
print("supplies_cost = $",supplies_cost) 

discount =supplies_cost * 30 / 100
print("discount =  $",discount)
print("*****" * 3)

shipping_cost =7.50

subtotal = (supplies_cost - discount + shipping_cost)
print("$",subtotal)

state_tax = (subtotal * 0.05)
print("$",state_tax)

print("******" * 3)

total = (subtotal + state_tax)
print("$",total)
