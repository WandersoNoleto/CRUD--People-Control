![apresentation-tip](https://github.com/WandersoNoleto/TourismSpots-Api/blob/main/documentation/assets/logo-api.png)

## TouristSpots-API 

## About

This API empowers users to effortlessly gather details about various tourist spots and register new points of interest, along with their key attractions. Designed with travel guides in mind, it provides a seamless experience for creating comprehensive travel itineraries. Whether you're developing a travel app or crafting a digital travel guide, this API is your go-to solution for efficiently handling tourist information without the constraints of a pre-existing database. Additionally, it integrates with the Open Weather API to provide weather information for the tourist spots.

### :clipboard: Tecnologies and Tolls
* Python
* Django REST Framework
* Open Weather API | [click here](https://openweathermap.org/api) for more details
  
### Features
* CRUD operations for tourist spots
* Filtering tourist spots by city, state or country
* Provide a location in latitude and longitude to search for nearby points
* Get the current weather of a tourist spot
* Get detailed weather or a summary for the next five days

## Model

Below we have the Django ORM related to the tourist spot model:
![RecipeModel](https://github.com/WandersoNoleto/TouristSpots-Api/blob/main/documentation/assets/SpotsModel.png)
After being serialized, this is how the data travels via JSON:
```
{
	"id": 1,
	"name": "Sugarloaf Mountain",
	"description": "Sugarloaf Mountain is a peak situated in Rio de Janeiro, Brazil.",
	"resources": "Hiking trails, cable cars, breathtaking views",
	"city": "Rio de Janeiro",
	"state": "Rio de Janeiro",
	"country": "Brazil",
	"image": null,
	"latitude": -22.9519,
	"longitude": -43.1654
}
```
## :gear: Installation Guide
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 



What things you need to install the software and how to install them

First, clone the repository
```
git clone https://github.com/WandersoNoleto/TouristSpots-Api.git
```
Install the dependencies listed in the requirements.txt file
```
pip install -r requirements.txt
```
###### :key: Create a .env file and set the variables according to the [.env.example](https://github.com/WandersoNoleto/TouristSpots-Api/blob/main/tourism_spots/.env.example).
###### :key: To get an Open Weather API key [click here](https://openweathermap.org/price)
Generate a new Django key and assign it to SECRET_KEY (in Python CLI)
```
from django.core.management import utils
print(utils.get_random_secret_key())
```

Use the command to run the service
```
python3 manage.py runserver
```

## :world_map: API Endpoints

| HTTP Verbs | Endpoints | Action |
| --- | --- | --- |
| GET | /tourist-spots/| View all tourist spots / Filter: name, id, city, state and country|
| GET | /tourist-spots/int:id/ | View tourist spot details |
| POST | /tourist-spots/| Register a new tourist spot |
| PATCH | /tourist-spots/int:id/| To update tourist spot values |
| DELETE |  /tourist-spots/int:id/ | Delete a tourist spot |
| GET |  /tourist-spots/nearby/ | Provide latitude and longitude to search for nearby points / radius (optional) |
| GET |  /tourist-spots/weather/int:id/ | To get a current weather data for a tourist spot |
| GET |  /tourist-spots/weather-5/int:id/ | Get weather data for a tourist spot for the next 5 days (3 hours) |
| GET |  /tourist-spots/weather-5-summary/int:id/ | Get weather summary data for a tourist spot for the next 5 days |
