metric_list = {
    "length":{"mm":0.001, "cm":0.01, "m" :1.0, "km":1000.0},
    "mass":{"mg": 0.001,"g": 1.0, "kg": 1000.0},
    "volume":{"ml": 0.001, "cl": 0.01, "dl": 0.1, "l": 1.0, "kl": 1000.0}}
print("=================================")
print("Welcome to METRIC CONVERSION TOOL")
print("=================================")
print("")

while True:
    metric_choice = input("""Length: (mm, cm, m, km)
Mass: (mg, g, kg)
Volume: (ml, cl, dl, l, kl)
Select a Category: 'length', 'mass', or 'volume': """).lower().strip()
    if metric_choice in metric_list:
        break
    else:
        print("Invalid input!")

while True:
    try:
        value = float(input("\nWhat is the numeric value you want to convert? "))
        break
    except:
        print("Invalid Input! Please enter a valid number.")

available_unit = ", ".join(metric_list[metric_choice].keys())

while True:
    current_metric = input(f"\nWhat unit is this currently in?({available_unit}): ").lower().strip()
    if current_metric in metric_list[metric_choice].keys():
        current_metric_value = metric_list[metric_choice][current_metric]
        break
    else:
        print("Invalid input!")
while True:
    target_metric = input(f"\nWhat unit do you want to convert it to?({available_unit}): ").lower().strip()
    if target_metric in metric_list[metric_choice].keys():
        target_metric_value = metric_list[metric_choice][target_metric]
        break
    else:
        print("Invalid input!")

base = value * current_metric_value
final_value = base / target_metric_value

print(f"\nThe value of {value}{current_metric} in {target_metric} is {final_value}{target_metric}.")