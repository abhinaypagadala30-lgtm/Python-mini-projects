import csv
import os
from datetime import date

FILE = "expenses.csv"

# Create file if it does not exist
if not os.path.exists(FILE):
    with open(FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "Item", "Amount"])

print("--- Expense Tracker ---")
item = input("What did you buy? Ex: Tiffin : ")
amount = input("How much? Ex: 50 : ")

today = str(date.today())
with open(FILE, "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([today, item, amount])

print("\nSaved Successfully!")

# Show total
total = 0
with open(FILE, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        total += int(row["Amount"])

print(f"Your Total Expense: Rs. {total}")