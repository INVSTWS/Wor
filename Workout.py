import json

main_dict = {
    "1":"List of options",
    "2":"List of exercises"
}

dict_options = {"1":"add",
                "2":"change",
                "3":"List of exercises",
                "4":"stop"}

store_options = dict(exercise=[], amount=[])

def save_data(store_options):
    with open("store_options.json", "w") as f:
        json.dump(store_options, f)

def load_data():
    try:
        with open("store_options.json", "r+") as f:
            data = f.read()
            if data:
                return json.loads(data)
            else:
                return dict(exercise=[], amount=[])
    except FileNotFoundError:
        return dict(exercise=[], amount=[])
    

store_options = load_data()

def add_exercise(name, value):
    if name in store_options["exercise"]:
        print(f"the exercise '{name.capitalize()}' already exists")
        return 4
    else:
        store_options["exercise"].append(name)
        store_options["amount"].append(value)
        return store_options
    

def change_exercise(name, value):
    if name not in store_options["exercise"]:
        print(f"the exercise '{name.capitalize()}' does not exist")
    else:
        index = store_options["exercise"].index(name)
        store_options["amount"][index] += value
        return store_options
    
    
def list_of_exercises(store_options):
    for exercise, amount in zip(store_options["exercise"], store_options["amount"]):
        print(f"\nExercise:{exercise}\n Amount: {amount}")
    


def basic_options():
    while True:
        for key, value in dict_options.items():
            print(f"{key} - {value.capitalize()}")

        option = input("Choose your option:")
        if option not in dict_options:
            print("Invalid option")
            continue

        if dict_options[option] == 'stop':
            break
        elif dict_options[option] == "List of exercises":
            list_of_exercises(store_options)
            continue

        name = input("Enter the name of your exercise:")
        value = int(input("Enter amount of your exercises:"))
        if dict_options[option] == 'add':
            stop = add_exercise(name, value)
            if stop == 4:
                continue
        elif dict_options[option] == 'change':
            change_exercise(name, value)


def main():
    for key, value in main_dict.items():
            print(f"{key} - {value.capitalize()}")
    option = input("Choose your option:")
    if option not in main_dict:
        print("Invalid option")
        return

    if main_dict[option] == "List of options":
        basic_options()
    elif main_dict[option] == "List of exercises":
        list_of_exercises(store_options)


main()

save_data(store_options)
