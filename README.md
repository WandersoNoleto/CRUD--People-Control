![apresentation-tip](https://github.com/WandersoNoleto/TourismSpots-Api/blob/main/documentation/assets/logo-api.png)

## TourismSpots-API ![Static Badge](https://img.shields.io/badge/status-developing-yellow)




## About

This API enables users to effortlessly gather details about different tourist spots and register new points of interest, along with their key attractions. Designed with travel guides in mind, it provides a seamless experience for creating comprehensive travel itineraries. Notably, our API operates independently, devoid of any integrated databases, granting users the flexibility to manage and organize their tourist data as they see fit. Whether you're developing a travel app or crafting a digital travel guide, this API is your go-to solution for efficiently handling tourist information without the constraints of a pre-existing database

### :clipboard: Tecnologies and Tolls
* Python
* Django REST Framework

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 



What things you need to install the software and how to install them

First, clone the repository
```
git clone https://github.com/WandersoNoleto/TourismSpots-Api.git
```
Install the dependencies listed in the requirements.txt file
```
pip install -r requirements.txt
```
###### :key: Create a .env file and set the variables according to the [.env.example](https://github.com/WandersoNoleto/TourismSpots-Api/blob/main/tourism_spots/.env.example).
Generate a new Django key and assign it to SECRET_KEY (in Python CLI)
```
from django.core.management import utils
print(utils.get_random_secret_key())
```

Use the command to run the service
```
python3 manage.py runserver
```

