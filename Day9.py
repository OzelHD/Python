# Write a Python script that: 
# 1️⃣ Fetches a random joke from the API (https://official-joke-api.appspot.com/random_joke).
# 2️⃣ Handles errors if the request fails.
# 3️⃣ Asks the user if they want another joke and loops until they say no.


#response.status_code == 200:   means "OK"
import requests
again = "y"
while again == "y":

    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke", timeout=5)
        response.raise_for_status()
    
        joke = response.json()
        print(f"{joke['setup']} - {joke['punchline']} --- {joke['id']}\n")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching joke: {e}")
    
    again = input("Do you want to hear another joke? (y / n) => ").strip().lower()
    print("\n")
print("Goodbye.\n")