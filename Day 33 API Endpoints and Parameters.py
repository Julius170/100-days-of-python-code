# API ENDPOINTS AND PARAMETERS


# API ENDPOINTS
import requests
from datetime import datetime
import time
import smtplib


MY_EMAIL = "juliusayoola5@yahoo.com"
MY_PASSWORD = "3c7hL#Uyxn~-zYu"
# response = requests.get(url= "http://api.open-notify.org/iss-now.json")


# # response.raise_for_status()

# longitude = response.json()["iss_position"]["longitude"]
# latitude = response.json()["iss_position"]["latitude"]


# iss_position = (longitude, latitude)
# print(iss_position)


# EXECISE KANYE'S QUOTES
# from  tkinter import *

# def get_quote():
#     response = requests.get(url= "http://api.kanye.rest")
#     response.raise_for_status()
#     kanye = response.json()
#     kanye_quote = kanye["quote"]
#     canvas.itemconfig(quote_text, text=kanye_quote)


# window = Tk()
# window.title("Kanye Says...")
# window.config(padx= 50, pady=50)


# canvas = Canvas.grid(width=340, height=414)
# background_img = PhotoImage(file="background.png")
# canvas.create_image(150, 207, image=background_img)
# quote_text = canvas.create_text(150, 207, text='', font=("Ariel", 65, "bold") )
# canvas.grid(row=0, column=0)


# kanye_img = PhotoImage(file="kanye.png")
# kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)



# API PARAMETERS


MY_LAT = 6.524379
MY_LNG = 3.379206

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0 
}

def is_iss_above():
    response = requests.get("http://api.open-notify.org/iss-now.json", params=parameters)
    response.raise_for_status()
    data = response.json()
    


    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])


    if MY_LAT-5  <= iss_latitude <=  MY_LAT+5 and MY_LNG-5 <= iss_longitude <= MY_LNG+5:
        return True

def is_night():
        
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0 
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    data = response.json()
    print(response.sunrise.split("T")[1].split(":")[0])
    print(response.sunset.split("T")[1].split(":")[0])


    time_now = datetime.now()
    

    if time_now >= response.sunset or time_now <= response.sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_above() and is_night():
        connection = smtplib.SMTP("smtp.yahoo.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr = MY_EMAIL,
            to_addr = MY_EMAIL,
            msg="Subject:Look Up😊😊😊\n\n The ISS is above you int the sky."
        )

# FINITE