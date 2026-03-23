
# Water Management System (Python)

## Project Description

This is a simple Water Management System written in Python. The program helps users calculate their daily water usage based on common household activities. It also provides feedback on whether the water usage is low, moderate, or high, encouraging water conservation.



## Files in the Project

**water.py** – Main Python program that calculates water usage.
**water_data.txt** – Stores daily water usage records 



## Features

* Calculate daily water usage
* Input water consumption for different activities
* Display total water usage
* Provide usage feedback (Low / Moderate / High)
* Option to calculate usage for multiple days
* Store usage data in a text file


## Requirements

* Python 3 installed on your system

### Program Code:
```
def calculate_water():
    print("\n--- Enter Daily Water Usage ---")

    drinking = int(input("Drinking (litres): "))
    bathing = int(input("Bathing (litres): "))
    washing = int(input("Washing clothes (litres): "))
    cooking = int(input("Cooking (litres): "))
    cleaning = int(input("Cleaning (litres): "))

    total = drinking + bathing + washing + cooking + cleaning

    print("\nTotal Water Usage:", total, "litres")

    if total < 100:
        status = "Low usage - Good job!"
    elif total <= 200:
        status = "Moderate usage - Try to save water"
    else:
        status = "High usage - Save water!"

    print(status)

    with open("water_data.txt", "a") as f:
        f.write(f"Total Usage: {total} litres - {status}\n")


def view_data():
    print("\n--- Saved Water Usage Data ---")
    try:
        with open("water_data.txt", "r") as f:
            data = f.read()
            print(data)
    except:
        print("No data found.")


def main():
    while True:
        print("\n--- Water Management System ---")
        print("1. Calculate Water Usage")
        print("2. View Saved Data")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            calculate_water()
        elif choice == "2":
            view_data()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice")


main()
```

## How to Run the Program

1. Download or clone the project
2. Open the project folder
3. Run the following command:

```bash
python water.py
```



## Example

The program will display a menu like:

```
1. Calculate Water Usage
2. View Saved Data
3. Exit
```



## Sample Output

```
Enter water used for drinking: 3
Enter water used for bathing: 50
Enter water used for washing clothes: 30
Enter water used for cooking: 10
Enter water used for cleaning: 20

Total Water Usage per Day: 113 litres
Moderate usage. Try to reduce a little.
```
### Output:
<img width="986" height="1032" alt="image" src="https://github.com/user-attachments/assets/dfcd9352-2bca-4db9-bfc5-e2c2e64a35a8" />


## Author

SHIVASRI.S  
YASHASWINI.S


