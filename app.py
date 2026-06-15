import requests
import pandas as pd
import matplotlib.pyplot as plt
import os

# -----------------------------------
# OpenWeatherMap API Configuration
# -----------------------------------
API_KEY = "ea7b26d63b04d4abe74c14926e495a81"
CITY = "Nellore"

URL = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# -----------------------------------
# Fetch Weather Data
# -----------------------------------
response = requests.get(URL)
weather_data = response.json()

# -----------------------------------
# Check API Response
# -----------------------------------
if weather_data["cod"] != "200":
    print("Error fetching data:", weather_data["message"])
    exit()

print("Weather data fetched successfully!")

# -----------------------------------
# Extract Required Data
# -----------------------------------
data_list = []

for item in weather_data["list"]:
    data_list.append({
        "datetime": item["dt_txt"],
        "temperature": item["main"]["temp"],
        "humidity": item["main"]["humidity"],
        "wind_speed": item["wind"]["speed"]
    })

# -----------------------------------
# Create DataFrame
# -----------------------------------
df = pd.DataFrame(data_list)

print("\nWeather Data Preview:\n")
print(df.head())

# -----------------------------------
# Create Folders
# -----------------------------------
os.makedirs("data", exist_ok=True)
os.makedirs("visualizations", exist_ok=True)

# -----------------------------------
# Save CSV File
# -----------------------------------
csv_path = "data/weather_data.csv"
df.to_csv(csv_path, index=False)

# -----------------------------------
# Temperature Visualization
# -----------------------------------
plt.figure(figsize=(12, 5))

plt.plot(
    df["datetime"],
    df["temperature"],
    marker='o',
    color='red'
)

plt.xticks(rotation=45)

plt.title(f"Temperature Forecast for {CITY}")
plt.xlabel("Date & Time")
plt.ylabel("Temperature (°C)")

plt.tight_layout()

temp_plot = "visualizations/temperature_plot.png"
plt.savefig(temp_plot)
plt.close()

# -----------------------------------
# Humidity Visualization
# -----------------------------------
plt.figure(figsize=(12, 5))

plt.plot(
    df["datetime"],
    df["humidity"],
    marker='o',
    color='blue'
)

plt.xticks(rotation=45)

plt.title(f"Humidity Forecast for {CITY}")
plt.xlabel("Date & Time")
plt.ylabel("Humidity (%)")

plt.tight_layout()

humidity_plot = "visualizations/humidity_plot.png"
plt.savefig(humidity_plot)
plt.close()

# -----------------------------------
# Wind Speed Visualization
# -----------------------------------
plt.figure(figsize=(12, 5))

plt.plot(
    df["datetime"],
    df["wind_speed"],
    marker='o',
    color='green'
)

plt.xticks(rotation=45)

plt.title(f"Wind Speed Forecast for {CITY}")
plt.xlabel("Date & Time")
plt.ylabel("Wind Speed (m/s)")

plt.tight_layout()

wind_plot = "visualizations/wind_speed_plot.png"
plt.savefig(wind_plot)
plt.close()

# -----------------------------------
# Success Message
# -----------------------------------
print("\nProject completed successfully!")

print("\nFiles Created:")
print(f"1. {csv_path}")
print(f"2. {temp_plot}")
print(f"3. {humidity_plot}")
print(f"4. {wind_plot}")