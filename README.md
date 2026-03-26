
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
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from datetime import datetime
import os

# ---------------- CALCULATE & SAVE ----------------
def calculate_water():
    try:
        drinking = int(entry_drinking.get().strip())
        bathing = int(entry_bathing.get().strip())
        washing = int(entry_washing.get().strip())
        cooking = int(entry_cooking.get().strip())
        cleaning = int(entry_cleaning.get().strip())

        total = drinking + bathing + washing + cooking + cleaning

        if total < 100:
            status = "Low usage - Good job!"
        elif total <= 200:
            status = "Moderate usage - Try to save water"
        else:
            status = "High usage - Save water!"

        today = datetime.now().strftime("%Y-%m-%d")

        # Save data
        with open("water_data.txt", "a") as f:
            f.write(f"{today},{total}\n")

        messagebox.showinfo("Saved", f"Total: {total} litres\n{status}")

        # Clear fields after saving
        entry_drinking.delete(0, tk.END)
        entry_bathing.delete(0, tk.END)
        entry_washing.delete(0, tk.END)
        entry_cooking.delete(0, tk.END)
        entry_cleaning.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Error", "Enter ONLY numbers")

# ---------------- SHOW GRAPH ----------------
def show_graph():
    try:
        data = {}

        # Check file existence
        if not os.path.exists("water_data.txt"):
            messagebox.showerror("Error", "No data file found. Save data first!")
            return

        with open("water_data.txt", "r") as f:
            lines = f.readlines()

            if not lines:
                messagebox.showerror("Error", "File is empty!")
                return

            for line in lines:
                parts = line.strip().split(",")

                # Skip invalid lines
                if len(parts) != 2:
                    continue

                date, total = parts

                try:
                    year = date.split("-")[0]
                    total = int(total)
                except:
                    continue

                data[year] = data.get(year, 0) + total

        if not data:
            messagebox.showerror("Error", "No valid data to display!")
            return

        years = list(data.keys())
        usage = list(data.values())

        # Plot graph
        plt.figure()
        plt.plot(years, usage, marker='o')
        plt.title("Yearly Water Usage")
        plt.xlabel("Year")
        plt.ylabel("Total Litres")
        plt.grid()
        plt.show()

    except Exception as e:
        messagebox.showerror("Error", str(e))

# ---------------- GUI ----------------
root = tk.Tk()
root.title("Water Management System")
root.geometry("350x420")

tk.Label(root, text="Enter Daily Water Usage", font=("Arial", 14)).pack(pady=10)

def create_field(label):
    tk.Label(root, text=label).pack()
    entry = tk.Entry(root)
    entry.pack(pady=3)
    return entry

entry_drinking = create_field("Drinking (litres)")
entry_bathing = create_field("Bathing (litres)")
entry_washing = create_field("Washing clothes (litres)")
entry_cooking = create_field("Cooking (litres)")
entry_cleaning = create_field("Cleaning (litres)")

tk.Button(root, text="Calculate & Save", command=calculate_water).pack(pady=10)
tk.Button(root, text="Show Yearly Graph", command=show_graph).pack(pady=10)

root.mainloop()
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


