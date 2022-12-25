vehicles = {
    'dream': 'Honda 250T',
    'roadster': 'BMW R1100',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
    'roadster': 'Yamaha XT650',
}

vehicles["starfighter"] = "Lockhead F-104"
vehicles["learjet"] = "Bombardier Learjet 75"
vehicles["toy"] = "Glider"

#upgrade the virago
vehicles['virago']="Yamaha XV535"

#deleting items in the dictionary
del vehicles["starfighter"]
result =  vehicles.pop("F1", None)
print(result)
plane = vehicles.pop("learjet")
print(plane)
bike = vehicles.pop("tenere", "not present")
print(bike)
print()


# my_car = vehicles['fiesta']
# print(my_car)
# commuter = vehicles['virago']
# print(commuter)
# learner = vehicles.get("ER5".casefold())
# print(learner)


# for key in vehicles:
#     print(key, vehicles[key], sep=", ")
for key, value in vehicles.items():
    print(key, value, sep=", ")
