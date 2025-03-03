# Zootopia with API

This project fetches animal data from the API Ninjas Animals API and generates an HTML page displaying details about the selected animals.

## Installation

Clone the repository:
```shell
git clone https://github.com/your-username/zootopia-animal-info.git  
cd zootopia-animal-info 
```

Install dependencies:
```shell
pip install -r requirements.txt  
```

Set up the API key by creating a .env file in the project directory and adding your API Ninjas API key:
```shell
API_KEY=your_real_api_key_here 
```

## Usage

Run the script:
```sh
python animals_web_generator.py  
```

Enter one or more animal names (comma-separated) when prompted. Example input:
```shell
lion, dog, cat
```
View the generated webpage by opening animals.html in a browser.

