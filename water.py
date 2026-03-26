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