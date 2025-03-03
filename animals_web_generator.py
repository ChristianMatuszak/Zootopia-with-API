import data_fetcher

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

def generate_website():
    user_input = input("Enter one or more animal names (comma-separated): ").strip()

    if not user_input:
        print("Error: You must enter at least one animal name.")
        return

    animal_names = [name.strip() for name in user_input.split(",")]
    animals_data = data_fetcher.fetch_data(animal_names)

    if not animals_data:
        print("No valid data available. Exiting.")
        return

    try:
        with open("animals_template.html", "r", encoding="utf-8") as file:
            template_content = file.read()
    except FileNotFoundError:
        print("Error: The template file 'animals_template.html' was not found.")
        return
    except Exception as e:
        print(f"Error reading template file: {e}")
        return

    animals_output = "".join(serialize_animal(animal) for animal in animals_data)

    updated_html_content = template_content.replace("__REPLACE_ANIMALS_INFO__", animals_output)

    try:
        with open("animals.html", "w", encoding="utf-8") as file:
            file.write(updated_html_content)
        print("animals.html has been created successfully.")
    except Exception as e:
        print(f"Error writing to 'animals.html': {e}")

if __name__ == "__main__":
    generate_website()