import requests

API_URL = "https://api.api-ninjas.com/v1/animals"
API_KEY = "qPpM4DtHmnoi0XzTKwMhAQ==gtvD7JXxzRmxWPo1"
HEADERS = {"X-Api-Key": API_KEY}

while True:
    user_input = input("Enter one or more animal names (comma-separated): ").strip()
    if user_input:
        break
    print("Error: You must enter at least one animal name.")

animal_names = [name.strip() for name in user_input.split(",")]

animals_data = []
for animal in animal_names:
    try:
        response = requests.get(API_URL, headers=HEADERS, params={"name": animal})
        response.raise_for_status()
        data = response.json()

        if not data:
            print(f"Warning: No data found for '{animal}'.")
        else:
            animals_data.extend(data)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for '{animal}': {e}")
        exit(1)


def serialize_animal(animal):
    name = animal.get("name", "Unknown")
    diet = animal.get("characteristics", {}).get("diet", "Unknown")
    locations = animal.get("locations", [])
    location = locations[0] if locations else "Unknown"
    type_ = animal.get("characteristics", {}).get("type", "Unknown")
    lifespan = animal.get("characteristics", {}).get("lifespan", "Unknown")
    color = animal.get("characteristics", {}).get("color", "Unknown")
    scientific_name = animal.get("taxonomy", {}).get("scientific_name", "Unknown")

    return f'''
    <li class="cards__item">
      <div class="card__title">{name}</div>
      <br/>
      <div class="card__text">
        <ul class="animal-details">
          <li class="animal-detail"><strong>Diet:</strong> {diet}</li>
          <li class="animal-detail"><strong>Location:</strong> {location}</li>
          <li class="animal-detail"><strong>Type:</strong> {type_}</li>
          <li class="animal-detail"><strong>Lifespan:</strong> {lifespan}</li>
          <li class="animal-detail"><strong>Color:</strong> {color}</li>
          <li class="animal-detail"><strong>Scientific Name:</strong> {scientific_name}</li>
        </ul>
      </div>
    </li>
    '''


try:
    with open("animals_template.html", "r", encoding="utf-8") as file:
        template_content = file.read()
except FileNotFoundError:
    print("Error: The template file 'animals_template.html' was not found.")
    exit(1)
except Exception as e:
    print(f"Error reading template file: {e}")
    exit(1)


def main():
    animals_output = "".join(serialize_animal(animal) for animal in animals_data)

    updated_html_content = template_content.replace("__REPLACE_ANIMALS_INFO__", animals_output)

    try:
        with open("animals.html", "w", encoding="utf-8") as file:
            file.write(updated_html_content)
        print("animals.html has been created successfully.")
    except Exception as e:
        print(f"Error writing to 'animals.html': {e}")
        exit(1)


if __name__ == "__main__":
    main()
