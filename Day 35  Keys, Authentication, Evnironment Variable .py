# DAY 35 KEYS, AUTHENTICATION, AND ENVIRONMENT VARIABLES SEND SMS

# API AUTHENTICATION (API KEYS)
import requests
import os
# from twilio.rest import Client
# from twilio.http.http_client import TwilioHttpClient






OWN_Endpoint ="http://"
API_KEY =""
account_sid = ""
auth_token = os.environ.get("AUTH_TOKEN")


weather_params = {
    "lat": 6.524379,
    "lon": 3.379206,
    "appid": API_KEY,
    "exclude": "currently,minutely,daily"

}

response = requests.get(OWN_Endpoint, params= weather_params)  

# print(response.json())

response.raise_for_status
weather_data = response.json()
wili_rain = False 

weather_slice = weather_data["hourly"][:12] 
for hour_data in weather_slice:
    condition_code = (hour_data["weather"][0]['id'])
    if int(condition_code) < 700:
        will_rain = True

# if will_rain:
#     proxy_client = TwilioHttpClient()
#     proxy_client.seession.proxies = {'https': os.environ['https_proxy']}


#     client = Client(account_sid, auth_token, http_client=proxy_client)
    # message =  client.message \
    #     .create(
    #         body = "Onlymide",
    #         from_ = '+2349059254549',
    #         to = "Sunshine"
    #     )


# print(message.status)

# Using Twilio

# print(weather_data ["hourly"][0]["weather"][0]["id"])




