import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://api.api-ninjas.com/v1/animals"
API_KEY = os.getenv("API_KEY")
HEADERS = {"X-Api-Key": API_KEY}

def fetch_data(animal_names):
    """
    Fetches the animals' data for the given list of animal names.
    Returns a list of dictionaries, each representing an animal.
    """
    if not API_KEY:
        print("Error: API key is missing. Please check your .env file.")
        return []

    animals_data = []

    for animal_name in animal_names:
        try:
            response = requests.get(API_URL, headers=HEADERS, params={"name": animal_name})
            response.raise_for_status()
            data = response.json()

            if not data:
                print(f"Warning: No data found for '{animal_name}'.")
            else:
                animals_data.extend(data)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data for '{animal_name}': {e}")

    return animals_data
