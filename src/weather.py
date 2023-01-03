#weather report
#Importing Beautifulsoup Library
from bs4 import BeautifulSoup
#importing requests module
import requests

#header user agent is a string allows the server to identify the O.S and application
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36' (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
#defining the weather function

def weather(city):
# Replaces the space with + operator
city=city.replace(" ","+")
#requests and get function to get the information from the URL provided
res=requests.get(f'https://www.google.com/search?q={city}&oq={city}’
                f'&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid='
                       f'chrome&ie=UTF-8',headers=headers)
#searches the information from google
    print("Searching in google......\n")
#Navigates on that particular website ,extract and store the data in soup object
    soup = BeautifulSoup(res.text,'html.parser')
#gets the information of location 
    location = soup.select('#wob_loc')[0].getText().strip()
#gets the information of time
    time = soup.select('#wob_dts')[0].getText().strip()
#gets the desired information
    info = soup.select('#wob_dc')[0].getText().strip()
#gets the weather information
    weather = soup.select('#wob_tm')[0].getText().strip()

#prints location
    print(location)
#prints time
    print(time)
#prints info 
    print(info)
#prints the weather in degree celcius
    print(weather+"°C")

#enter the city name
print("enter the city name")
city=input()

#Concatenating the city name and weather 
city=city+" weather"

#passing the city object to weather function
weather(city)
