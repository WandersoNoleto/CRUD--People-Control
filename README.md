![apresentation-tip](https://github.com/WandersoNoleto/TourismSpots-Api/blob/main/documentation/assets/logo-api.png)

## TourismSpots-API 




## About

This API enables users to effortlessly gather details about different tourist spots and register new points of interest, along with their key attractions. Designed with travel guides in mind, it provides a seamless experience for creating comprehensive travel itineraries. Notably, our API operates independently, devoid of any integrated databases, granting users the flexibility to manage and organize their tourist data as they see fit. Whether you're developing a travel app or crafting a digital travel guide, this API is your go-to solution for efficiently handling tourist information without the constraints of a pre-existing database

### :clipboard: Tecnologies and Tolls
* Python
* Django REST Framework
  
### Features
* CRUD operations for tourist spots
* Filtering tourist spots by city, state or country
* Provide a location in latitude and longitude and search for nearby points

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
| GET | /spots/| View all tourist spots / Filter: name, id, city, state and country|
| GET | /spots/int:id/ | View tourist spot details |
| POST | /spots/| Register a new tourist spot |
| PATCH | /spots/int:id/| To update tourist spot values |
| DELETE |  /spots/int:id/ | Delete a tourist spot |
| DELETE |  /spots/nearby/ | Provide latitude and longitude to search for nearby points / radius (optional) |
