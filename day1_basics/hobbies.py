num_of_hobbies = (input("How many hobbies do you have?: "))
hobbies = []

if num_of_hobbies.isdigit():
    for i in range(int(num_of_hobbies)):
        hobby = input(f"Enter No {i + 1} hobby: ")
        hobbies.append(hobby)
    print("\n These are your hobbies \n")
    for hobby in hobbies:
        print(f" * {hobby}" )
else: print("Please enter a valid number")