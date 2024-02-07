import pulp

# Model
model = pulp.LpProblem("Production_Optimization", pulp.LpMaximize)

# Declaration of variables
lemonade = pulp.LpVariable("Lemonade", lowBound=0, cat=pulp.LpInteger)
fruit_juice = pulp.LpVariable("Fruit_Juice", lowBound=0, cat=pulp.LpInteger)

model += lemonade + fruit_juice, "Total_Product_Quantity"

# Constraints
model += 2 * lemonade + fruit_juice <= 100, "Water_Constraint"
model += lemonade <= 50, "Sugar_Constraint"
model += lemonade <= 30, "Lemon_Juice_Constraint"
model += 2 * fruit_juice <= 40, "Fruit_Puree_Constraint"

# Solving the model
model.solve()

# Results
print("Result:")
print(f"Quantity of Lemonade: {lemonade.varValue}")
print(f"Quantity of Fruit Juice: {fruit_juice.varValue}")
print(f"Maximum total product quantity: {pulp.value(model.objective)}")
