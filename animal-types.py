# Imagine that there are only these types of animals:
#   "lion"
#   "tiger"
#   "poodle"
#   "collie"
#   "badger"
#   "horse"
#   "sheep"
#   "snake"
#   "lizard"

animal = "sheep" 

is_type_of_cat = (animal == "lion") or (animal == "tiger")
is_type_of_dog = (animal == "poodle") or (animal == "collie")
is_type_of_reptile = (animal == "snake") or (animal == "lizard")
is_not_cat_or_dog = (animal == "badger") or (animal == "horse") or (animal == "sheep") or is_type_of_reptile

print animal, "is a cat:", is_type_of_cat
print animal, "is a dog:", is_type_of_dog
print animal, "is a reptile:", is_type_of_reptile
print animal, "is not a cat or a dog:", is_not_cat_or_dog
