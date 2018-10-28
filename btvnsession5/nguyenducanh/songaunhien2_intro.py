import random
# print (random.randint(0, 100))
numberRandom = random.randint(0, 100)
print(numberRandom)
if numberRandom < 30:
    print ("rainy")
elif numberRandom >= 30 and numberRandom < 60:
    print ("cloudy")
else:
    print ("sunny")