import math

def get_plan(current_production, months, percent):
    production_plan = []
    current_production = math.floor(current_production)
    print(current_production)
    for month in range(months):
        increment = math.floor(current_production*(percent/100))
        current_production += increment
        production_plan.append(current_production)
    return production_plan

print(get_plan(10, 4, 30))
