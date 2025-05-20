from customer import Customer
from coffee import Coffee


alvine = Customer("Alvine")  
latte = Coffee("Latte")  


alvine.create_order(latte, 5.5)


print(alvine.name)

alvine.name = "Clive"
print(alvine.name) 


print(latte.average_price())
