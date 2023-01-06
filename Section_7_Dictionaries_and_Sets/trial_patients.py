# trial_1 = {"Georgia", "Bob", "Charley", "John"}
# trial_2 = {"Anne", "Georgia", "Eddie", "Charley"}
#
# check_set = trial_1 & trial_2
# print(check_set)

farm_animals = {"sheep", "hen", "cow", "horse", "goat"}
wild_animals = {"lion", "elephant", "tiger", "goat", "panther", "horse"}

potential_rides = {"donkey", "horse", "camel"}
intersection = farm_animals & wild_animals & potential_rides
print(intersection)
mounts=farm_animals.intersection(wild_animals,potential_rides)
print(mounts)