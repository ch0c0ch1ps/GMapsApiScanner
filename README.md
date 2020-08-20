# GMapsApiScanner

GmapsAPIScan.py It's a python script froked from https://github.com/ozguralp/gmapsapiscanner that checks for common attacks for leaked/exposed GoogleMapsAPIKEY.

# PoC
![a](https://i.imgur.com/BYAUfB7.jpg)
![b](https://i.imgur.com/H7i6NJr.jpg)
![c](https://i.imgur.com/XbT3wbs.jpg)





# IMPACT

If the API keys are not met with these security configurations, below scenarios may be conducted by a malicious user:
Consuming the company’s monthly quota or can over-bill with unauthorized usage of this service and do financial damage to the company, if the company does not have any limitation settings on API budgets.
Conduct a denial of service attack specific to the service if any limitation of maximum bill control settings exist in the Google account. While this could not be too dangerous if used the application parts of such “Contact Us” pages, however it could be really dangerous if the main business/functionality of the app is handled within these maps such as Uber (Finding/tracking rides via Maps) and Booking (Searching hotels via Maps).

#Further Investigation...

https://medium.com/bugbountywriteup/unauthorized-google-maps-api-key-usage-cases-and-why-you-need-to-care-1ccb28bf21e

https://medium.com/bugbountywriteup/google-maps-api-not-the-key-bugs-that-i-found-over-the-years-781840fc82aa
