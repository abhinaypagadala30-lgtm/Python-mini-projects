import urllib.request
import json

print("--- Kakinada Weather ---")
try:
    url = "https://wttr.in/Kakinada?format=j1"
    with urllib.request.urlopen(url, timeout=10) as response:
        data = json.loads(response.read())
    
    temp = data["current_condition"][0]["temp_C"]
    desc = data["current_condition"][0]["weatherDesc"][0]["value"]
    print(f"Right now in Kakinada: {temp}°C, {desc}")
except Exception as e:
    print("No Internet / Site not opening. Please try again.")
    print(f"Error: {e}")