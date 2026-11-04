# Hyderabad Fresher Budget Analyzer - Made by Abhinay
# Made with Pandas + Numpy, on Phone in Pydroid

import pandas as pd
import numpy as np
import csv
import os

FILE_NAME = "my_expenses.csv"

def add_expense():
    print("\n--- Add Expense ---")
    date = input("Date (ex: 04-11-2026): ")
    category = input("Category (PG / Food / Bus / Recharge / Others): ")
    amount = float(input("Amount: "))
    
    file_exists = os.path.exists(FILE_NAME)
    with open(FILE_NAME, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Date", "Category", "Amount"])
        writer.writerow([date, category, amount])
    print("Saved ✅")

def analyze():
    if not os.path.exists(FILE_NAME):
        print("\nNo data yet. First add 3-4 expenses.")
        return

    # Reading CSV with Pandas
    df = pd.read_csv(FILE_NAME)
    
    print("\n====== BUDGET REPORT ======")
    print(df)

    # Maths with Numpy
    total = np.sum(df["Amount"])
    average = np.mean(df["Amount"])
    highest = np.max(df["Amount"])
    lowest = np.min(df["Amount"])

    print(f"\nTotal Expense: Rs.{total}")
    print(f"Average Expense: Rs.{average:.2f}")
    print(f"Highest Expense: Rs.{highest}")
    print(f"Lowest Expense: Rs.{lowest}")

    # Category wise Group with Pandas
    print("\n--- Category Wise Total ---")
    category_wise = df.groupby("Category")["Amount"].sum()
    print(category_wise)

    # Smart Advice - This is Unique Point
    top_category = df.groupby("Category")["Amount"].sum().idxmax()
    print(f"\n💡 Smart Advice: You are spending most on '{top_category}'.")
    print(f"If you reduce '{top_category}' by 20% next month, you can save Rs.{total * 0.20:.0f}.")

    # Compare with Salary
    try:
        salary = float(input("\nWhat is your Salary / Pocket Money? : "))
        remaining = salary - total
        print(f"Remaining Money: Rs.{remaining}")
        if remaining < 0:
            print("⚠️ Danger! You spent more than your salary.")
        elif remaining < salary * 0.2:
            print("⚠️ Careful! Your savings are very low.")
        else:
            print("✅ Super! You are saving well.")
    except:
        print("Salary not given, skipping.")

def main():
    while True:
        print("\n====== FRESHER BUDGET ANALYZER ======")
        print("1. Add Expense")
        print("2. Analyze with Pandas + Numpy")
        print("3. Exit")
        choice = input("Choice (1/2/3): ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            analyze()
        elif choice == "3":
            print("Bye Abhi!")
            break
        else:
            print("Please enter 1,2,3")

if __name__ == "__main__":
    main()