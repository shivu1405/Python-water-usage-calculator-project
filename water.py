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