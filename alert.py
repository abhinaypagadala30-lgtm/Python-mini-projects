# No Selenium, simple job list

jobs = [
    {"Company": "TeamLease", "Role": "Fiber Engineer", "Place": "Gurugram", "Salary": "1-3.5 LPA"},
    {"Company": "Jio", "Role": "Field Engineer", "Place": "Hyderabad", "Salary": "2.5 LPA"},
    {"Company": "Airtel", "Role": "Network Engineer", "Place": "Kakinada", "Salary": "3 LPA"},
]

print("--- Today Fresher Jobs ---")
for job in jobs:
    print(f"\nCompany: {job['Company']}")
    print(f"Role: {job['Role']}")
    print(f"Place: {job['Place']}")
    print(f"Salary: {job['Salary']}")
    print("--------------------")

print("\nThese are sample jobs. Later we will fetch live jobs from website.")