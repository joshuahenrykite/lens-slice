toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']

prices = [2, 6, 1, 3, 2, 7, 2]\

num_pizzas = len(toppings)

print("We sell %.0f different kinds of pizza!"
     %(num_pizzas))

pizzas = list(zip(prices, toppings))

#print(pizzas)

pizzas.sort()

#print(pizzas)

cheapest_pizzas = pizzas[0]
#print(cheapest_pizzas)

priciest_pizza = pizzas[-1]
#print(priciest_pizza)

three_cheapest = pizzas[:3]
#print(three_cheapest)

num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)
