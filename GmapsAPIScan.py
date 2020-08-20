import requests
import warnings 
import json
import pyfiglet
import webbrowser
import os
from colorama import init, Fore, Back, Style

ascii_banner = pyfiglet.figlet_format("GmapsAPIScan")
print(ascii_banner)
print(Fore.BLUE + "Original from Ozguralp https://github.com/ozguralp/gmapsapiscanner , Forked by Ch0c0ch1ps")
print(Fore.WHITE)

vulnerable_apis = []
warnings.filterwarnings("ignore")
apikey = input("Please enter the Google Maps API key you wanted to test: ")
url = "https://maps.googleapis.com/maps/api/staticmap?center=45%2C10&zoom=7&size=400x400&key="+apikey 
response = requests.get(url, verify=False)
if response.status_code == 200:
	print("API key is \033[1;31;40m vulnerable \033[0m for Staticmap API! Here is the PoC link which can be used directly via browser:")
	print(url)
	vulnerable_apis.append("Staticmap")
else:
	print("API key is not vulnerable for Staticmap API.")
	print("Reason: "+ str(response.content))

url = "https://maps.googleapis.com/maps/api/streetview?size=400x400&location=40.720032,-73.988354&fov=90&heading=235&pitch=10&key="+apikey 
response = requests.get(url, verify=False)
if response.status_code == 200:
	print("API key is \033[1;31;40m vulnerable \033[0m for Streetview API! Here is the PoC link which can be used directly via browser:")
	print(url)
	vulnerable_apis.append("Streetview")
else:
	print("API key is not vulnerable for Streetview API.")
	print("Reason: "+ str(response.content))

url = "https://www.google.com/maps/embed/v1/place?q=Seattle&key="+apikey 
response = requests.get(url, verify=False)
if response.status_code == 200:
	print("API key is \033[1;31;40m vulnerable \033[0m for Embed (Basic-Free) API! Here is the PoC HTML code which can be used directly via browser:")
	print("<iframe width=\"600\" height=\"450\" frameborder=\"0\" style=\"border:0\" src=\""+url+"\" allowfullscreen></iframe>")
	vulnerable_apis.append("Embed (Basic-Free)")
else:
	print("API key is not vulnerable for Embed (Basic-Free) API.")
	print("Reason: "+ str(response.content))

url = "https://www.google.com/maps/embed/v1/search?q=record+stores+in+Seattle&key="+apikey 
response = requests.get(url, verify=False)
if response.status_code == 200:
	print("API key is \033[1;31;40m vulnerable \033[0m for Embed (Advanced-Paid) API! Here is the PoC HTML code which can be used directly via browser:")
	print("<iframe width=\"600\" height=\"450\" frameborder=\"0\" style=\"border:0\" src=\""+url+"\" allowfullscreen></iframe>")
	vulnerable_apis.append("Embed (Advanced-Paid)")
else:
	print("API key is not vulnerable for Embed (Advanced-Paid) API.")
	if len(response.content.decode().split("\"")) < 77:
		print("Reason: "+ str(response.content))
	else:
		print("Reason: "+ response.content.decode().split("\"")[77])

url = "https://maps.googleapis.com/maps/api/directions/json?origin=Disneyland&destination=Universal+Studios+Hollywood4&key="+apikey
response = requests.get(url, verify=False)
if response.text.find("error_message") < 0:
	print("API key is \033[1;31;40m vulnerable \033[0m for Directions API! Here is the PoC link which can be used directly via browser:")
	print(url)
	vulnerable_apis.append("Directions")
else:
	print("API key is not vulnerable for Directions API.")
	print("Reason: "+ str(response.json()["error_message"]))

url = "https://maps.googleapis.com/maps/api/geocode/json?latlng=40,30&key="+apikey 
response = requests.get(url, verify=False)
if response.text.find("error_message") < 0:
	print("API key is \033[1;31;40m vulnerable \033[0m for Geocode API! Here is the PoC link which can be used directly via browser:")
	print(url)
	vulnerable_apis.append("Geocode")
else:
	print("API key is not vulnerable for Geocode API.")
	print("Reason: "+ response.json()["error_message"])

url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=40.6655101,-73.89188969999998&destinations=40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.6905615%2C-73.9976592%7C40.659569%2C-73.933783%7C40.729029%2C-73.851524%7C40.6860072%2C-73.6334271%7C40.598566%2C-73.7527626%7C40.659569%2C-73.933783%7C40.729029%2C-73.851524%7C40.6860072%2C-73.6334271%7C40.598566%2C-73.7527626&key="+apikey 
response = requests.get(url, verify=False)
if response.text.find("error_message") < 0:
	print("API key is \033[1;31;40m vulnerable \033[0m for Distance Matrix API! Here is the PoC link which can be used directly via browser:")
	print(url)
	vulnerable_apis.append("Distance Matrix")
else:
	print("API key is not vulnerable for Distance Matrix API.")
	print("Reason: "+ response.json()["error_message"])

url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?input=Museum%20of%20Contemporary%20Art%20Australia&inputtype=textquery&fields=photos,formatted_address,name,rating,opening_hours,geometry&key="+apikey
response = requests.get(url, verify=False) 
if response.text.find("error_message") < 0:
	print("API key is \033[1;31;40m vulnerable \033[0m for Find Place From Text API! Here is the PoC link which can be used directly via browser:")
	print(url)
	vulnerable_apis.append("Find Place From Text")
else:
	print("API key is not vulnerable for Find Place From Text API.")
	print("Reason: "+ response.json()["error_message"])

url = "https://maps.googleapis.com/maps/api/place/autocomplete/json?input=Bingh&types=%28cities%29&key="+apikey 
response = requests.get(url, verify=False)
if response.text.find("error_message") < 0:
	print("API key is \033[1;31;40m vulnerable \033[0m for Autocomplete API! Here is the PoC link which can be used directly via browser:")
	print(url)
	vulnerable_apis.append("Autocomplete")
else:
	print("API key is not vulnerable for Autocomplete API.")
	print("Reason: "+ response.json()["error_message"])

url = "https://maps.googleapis.com/maps/api/elevation/json?locations=39.7391536,-104.9847034&key="+apikey 
response = requests.get(url, verify=False)
if response.text.find("error_message") < 0:
	print("API key is \033[1;31;40m vulnerable \033[0m for Elevation API! Here is the PoC link which can be used directly via browser:")
	print(url)
	vulnerable_apis.append("Elevation")
else:
	print("API key is not vulnerable for Elevation API.")
	print("Reason: "+ response.json()["error_message"])

url = "https://maps.googleapis.com/maps/api/timezone/json?location=39.6034810,-119.6822510&timestamp=1331161200&key="+apikey 
response = requests.get(url, verify=False)
if response.text.find("errorMessage") < 0:
	print("API key is \033[1;31;40m vulnerable \033[0m for Timezone API! Here is the PoC link which can be used directly via browser:")
	print(url)
	vulnerable_apis.append("Timezone")
else:
	print("API key is not vulnerable for Timezone API.")
	print("Reason: "+ response.json()["errorMessage"])

url = "https://roads.googleapis.com/v1/nearestRoads?points=60.170880,24.942795|60.170879,24.942796|60.170877,24.942796&key="+apikey 
response = requests.get(url, verify=False)
if response.text.find("error") < 0:
	print("API key is \033[1;31;40m vulnerable \033[0m for Roads API! Here is the PoC link which can be used directly via browser:")
	print(url)
	vulnerable_apis.append("Roads")	
else:
	print("API key is not vulnerable for Roads API.")
	print("Reason: "+ response.json()["error"]["message"])

url = "https://www.googleapis.com/geolocation/v1/geolocate?key="+apikey 
postdata = {'considerIp': 'true'}
response = requests.post(url, data=postdata, verify=False)
if response.text.find("error") < 0:
	print("API key is \033[1;31;40m vulnerable \033[0m for Geolocation API! Here is the PoC curl command which can be used from terminal:")
	print("curl -i -s -k  -X $'POST' -H $'Host: www.googleapis.com' -H $'Content-Length: 22' --data-binary $'{\"considerIp\": \"true\"}' $'"+url+"'")
	vulnerable_apis.append("Geolocation")
else:
	print("API key is not vulnerable for Geolocation API.")
	print("Reason: "+ response.json()["error"]["message"])



print(Fore.RED + "Javascript API Vulnerability TEST requires Manual CHECK \n")

html_str = """
<!DOCTYPE html>
<html>
  <head>
    <title>Simple Map</title>
    <script src="https://polyfill.io/v3/polyfill.min.js?features=default"></script>
    <script
      src="https://maps.googleapis.com/maps/api/js?key={APITEST}&callback=initMap&libraries=&v=weekly"
      defer
    ></script>
    <style type="text/css">
      /* Always set the map height explicitly to define the size of the div
       * element that contains the map. */
      #map {{
        height: 100%;
      }}

      /* Optional: Makes the sample page fill the window. */
      html,
      body {{
        height: 100%;
        margin: 0;
        padding: 0;
      }}
    </style>
    <script>
      "use strict";

      let map;

      function initMap() {{
        map = new google.maps.Map(document.getElementById("map"), {{
          center: {{
            lat: -34.397,
            lng: 150.644
          }},
          zoom: 8
        }});
      }}
    </script>
  </head>
  <body>
    <div id="map"></div>
  </body>
</html>
"""
new_message= html_str.format(APITEST=apikey)
Html_file= open("PoCJvascriptAPIKEY.html","w")
Html_file.write(new_message)
Html_file.close()

ascii_banner = pyfiglet.figlet_format("-------------")
print(ascii_banner)
print(Fore.GREEN + "Please check the HTML FILE in debugging options in your browser, if it doesn't print any error, then it's vulnerable \n")

url= "PoCJvascriptAPIKEY.html"
webbrowser.open(url)

for i in range (len(vulnerable_apis)):
    print ("- " + vulnerable_apis[i])
    
    
    
