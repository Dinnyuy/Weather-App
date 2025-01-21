from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  # For displaying weather icons
import requests
from io import BytesIO

# Function to fetch and display current weather data
def fetch_weather():
    region = com.get()  # Get the selected region
    if region:
        url = f"https://wttr.in/{region}?format=%C|%t|%P|%w|%m|%M|%e"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                weather_data = response.text.split("|")
                # Update weather labels
                w_label1.config(text=weather_data[0].strip())  # Condition
                temp_label1.config(text=weather_data[1].strip())  # Temperature
                per_label1.config(text=weather_data[2].strip())  # Pressure
                wind_label1.config(text=weather_data[3].strip())  # Wind Speed
                morning_label1.config(text=weather_data[4].strip())  # Morning
                afternoon_label1.config(text=weather_data[5].strip())  # Afternoon
                evening_label1.config(text=weather_data[6].strip())  # Evening
                update_icon(region)  # Fetch and display the icon
            else:
                show_error()
        except Exception:
            show_error()
    else:
        w_label1.config(text="Select a region")
        clear_labels()

# Function to fetch and display future predictions
def fetch_predictions():
    region = com.get()
    if region:
        url = f"https://wttr.in/{region}?2n"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                pred_label.config(text=response.text.strip())  # Display raw prediction
            else:
                pred_label.config(text="Error fetching predictions")
        except Exception:
            pred_label.config(text="Error fetching predictions")
    else:
        pred_label.config(text="Select a region")

# Function to fetch and display weather icons
def update_icon(region):
    try:
        icon_url = f"https://wttr.in/{region}.png"
        response = requests.get(icon_url)
        if response.status_code == 200:
            img_data = BytesIO(response.content)
            img = Image.open(img_data)
            img = img.resize((100, 100))  # Resize the image
            tk_img = ImageTk.PhotoImage(img)
            icon_label.config(image=tk_img)
            icon_label.image = tk_img  # Keep a reference to prevent garbage collection
        else:
            icon_label.config(image="", text="No Icon")
    except Exception:
        icon_label.config(image="", text="No Icon")

# Function to display an error message
def show_error():
    w_label1.config(text="Error fetching data")
    clear_labels()

def clear_labels():
    temp_label1.config(text="--")
    per_label1.config(text="--")
    wind_label1.config(text="--")
    morning_label1.config(text="--")
    afternoon_label1.config(text="--")
    evening_label1.config(text="--")
    pred_label.config(text="")

# GUI setup
win = Tk()
win.title("Weather App - Cameroon")
win.geometry("800x800")
win.config(bg="#87CEEB")  # Sky blue background

# App Title
name_label = Label(
    win,
    text="Weather App - Cameroon",
    font=("Helvetica", 28, "bold"),
    fg="white",
    bg="#4682B4"  # Steel blue
)
name_label.place(x=50, y=20, height=60, width=700)

# Dropdown for regions
list_name = [
    "Northwest", "Southwest", "Littoral", "Center", "South",
    "East", "Far North", "North", "Adamawa", "West"
]
com = ttk.Combobox(win, values=list_name, font=("Helvetica", 14))
com.place(x=50, y=100, height=35, width=400)

# Fetch Weather Button
button = Button(
    win,
    text="Get Weather",
    font=("Comic Sans MS", 16, "bold"),
    bg="#32CD32",  # Lime green
    fg="white",
    command=fetch_weather
)
button.place(x=470, y=100, height=35, width=150)

# Fetch Predictions Button
pred_button = Button(
    win,
    text="Get Predictions",
    font=("Comic Sans MS", 16, "bold"),
    bg="#FFA500",  # Orange
    fg="white",
    command=fetch_predictions
)
pred_button.place(x=470, y=150, height=35, width=200)

# Labels for displaying weather data
w_label = Label(win, text="Condition:", font=("Arial", 16, "bold"), bg="#87CEEB")
w_label.place(x=50, y=200)
w_label1 = Label(win, text="", font=("Arial", 16), bg="#ADD8E6")
w_label1.place(x=250, y=200, width=500)

temp_label = Label(win, text="Temperature:", font=("Arial", 16, "bold"), bg="#87CEEB")
temp_label.place(x=50, y=260)
temp_label1 = Label(win, text="", font=("Arial", 16), bg="#ADD8E6")
temp_label1.place(x=250, y=260, width=500)

per_label = Label(win, text="Pressure:", font=("Arial", 16, "bold"), bg="#87CEEB")
per_label.place(x=50, y=320)
per_label1 = Label(win, text="", font=("Arial", 16), bg="#ADD8E6")
per_label1.place(x=250, y=320, width=500)

wind_label = Label(win, text="Wind Speed:", font=("Arial", 16, "bold"), bg="#87CEEB")
wind_label.place(x=50, y=380)
wind_label1 = Label(win, text="", font=("Arial", 16), bg="#ADD8E6")
wind_label1.place(x=250, y=380, width=500)

morning_label = Label(win, text="Morning:", font=("Arial", 16, "bold"), bg="#87CEEB")
morning_label.place(x=50, y=440)
morning_label1 = Label(win, text="", font=("Arial", 16), bg="#ADD8E6")
morning_label1.place(x=250, y=440, width=500)

afternoon_label = Label(win, text="Afternoon:", font=("Arial", 16, "bold"), bg="#87CEEB")
afternoon_label.place(x=50, y=500)
afternoon_label1 = Label(win, text="", font=("Arial", 16), bg="#ADD8E6")
afternoon_label1.place(x=250, y=500, width=500)

evening_label = Label(win, text="Evening:", font=("Arial", 16, "bold"), bg="#87CEEB")
evening_label.place(x=50, y=560)
evening_label1 = Label(win, text="", font=("Arial", 16), bg="#ADD8E6")
evening_label1.place(x=250, y=560, width=500)

# Label to display future predictions
pred_label = Label(
    win,
    text="",
    font=("Arial", 14),
    bg="#ADD8E6",
    wraplength=700,
    justify="left"
)
pred_label.place(x=50, y=620, width=700, height=100)

# Label for weather icon
icon_label = Label(win, text="", bg="#87CEEB")
icon_label.place(x=650, y=150, width=100, height=100)

# Footer with credits
footer_label = Label(
    win,
    text="Powered by wttr.in",
    font=("Helvetica", 12),
    fg="white",
    bg="#4682B4",
)
footer_label.place(x=0, y=780, height=30, width=800)

win.mainloop()
