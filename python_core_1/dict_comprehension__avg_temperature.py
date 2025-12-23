def average_temperature(months: dict, temperature: int) -> dict:
    return {month: months[month] for month in months if months[month] > temperature}





months = {'Jun': 18, 'Jul': 23.8, 'Aug': 22.9}
temperature = 20
print(average_temperature(months, temperature)) # == {'Jul': 23.8, 'Aug': 22.9}