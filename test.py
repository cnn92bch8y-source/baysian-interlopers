if cat_mood == "hungry":
    meow()
elif cat_mood == "asleep":
    do_not_disturb()
else:
    destroy_furniture()

try:
    pet_the_cat()
except ClawAttack:
    print("You have betrayed the rules.")

while True:
    stare_into_void()
