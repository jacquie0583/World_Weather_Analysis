#  World_Weather_Analysis
##  Let’s Plan That Trip
##  Background

### Taking the PlanMyTrip app, our company incorporates advanced technology to make a few changes to take the app to the next level. Specifically, by incorporating a weather description to the weather data. Followed by using the beta testers to input statements to filter the data for participants’ weather preferences, which will be used to identify potential travel destinations and nearby hotels. Then, generating a list of potential travel destinations, the beta tester filters out four cities to create a travel itinerary. Finally, utilizing the Google Maps Directions API, a travel route between the four cities is generated as well as a marker layer map.

###  Part I – Weather Database:  Retrieve Weather Data
To begin, a Python script was created to visualize the weather of 500+ cities across the world of varying distance from the equator. Utilizing a Python library and the OpenWeatherMap API,  a representative model was created to illustrate the following:

     • Randomly select at least 500 unique (non-repeat) cities based on latitude and longitude.
     • Perform a weather check on each of the cities using a series of successive API calls and acquiring the following:  
         o	Latitude and longitude
         o	Maximum temperature
         o	Percent humidity
         o	Percent cloudiness
         o	Wind speed
         o	Weather description (for example, clouds, fog, light rain, clear sky) 
         
      • Include a log of each city as it’s being processed with the city number and city name.
      • Save a CSV of all retrieved data 
      
![Image 1](https://github.com/jacquie0583/World_Weather_Analysis/blob/main/Image%201.png)
      
 ###  Part II – Vacation Search:  Create a Customer Travel Destinations Map
Using input statements to retrieve customer weather preferences, a map was generated with the following tech tools:   gmaps and the Google Places API.   Those preferences were applied to identify potential travel destinations and nearby hotels. To give the customers a chance to visualize their vacation, a marker layered map with pop-up markers shows those destinations.

 ![Image 2 WeatherPy_vacation_map.png]( https://github.com/jacquie0583/World_Weather_Analysis/blob/main/Image%202%20WeatherPy_vacation_map.png)
 
 ###  Part III – Vacation Itinerary:  Create a Travel Itinerary Map
Narrowing down according to the criteria given, locations of the hotels and a road map were designed with leaving and arriving at the same location.  Using the Google Directions API to create a travel itinerary shows the route between four cities chosen for the customer’s possible travel destinations. Then, a marker layered map with a pop-up markers for each city on the itinerary was designed.  The waypoints are the three other cities, and the travel mode was either "DRIVING", "BICYCLING", or "WALKING".  "Driving" was chosen as the mode of travel.  The directions layer map between the cities and the travel map created:

![Image 3 WeatherPy_travel_map.png]( https://github.com/jacquie0583/World_Weather_Analysis/blob/main/Image%203%20WeatherPy_travel_map.png)

Also, available to assist in the travel arrangements, a table was designed with respect to the specifics of trip:

![Image 4.png](https://github.com/jacquie0583/World_Weather_Analysis/blob/main/Image%204.png)

A marker layer map with a pop-up markers for the cities on the itinerary was created and each marker has the following information: 

         o	Hotel name
         o	City
         o	Country
         o	Current weather description with the maximum temperature

![Image 5 WeatherPy_travel_map_markers.png](https://github.com/jacquie0583/World_Weather_Analysis/blob/main/Image%205%20WeatherPy_travel_map_markers.png)

#  Summary
 The World Weather Analysis was an amazing project to be involved in and grateful that you chose us to further business objectives.
 

