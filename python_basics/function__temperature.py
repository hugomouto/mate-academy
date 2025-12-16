def temperature(value):
    #  Write code here
    if value < 20:
        return "Cold"
    elif 20<=value<=50:
        return "Warm"
    else:
        return "Hot"

print(temperature(510))