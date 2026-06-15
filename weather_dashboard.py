import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# -----------------------------------
# Create charts folder automatically
# -----------------------------------
os.makedirs("charts", exist_ok=True)

# -----------------------------------
# API Configuration
# -----------------------------------
API_KEY = "ea7b26d63b04d4abe74c14926e495a81"

CITY = "Nellore"

URL = f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# -----------------------------------
# Fetch Data from API
# -----------------------------------
response = requests.get(URL)

if response.status_code == 200:

    data = response.json()

    weather_data = []

    for item in data['list']:

        weather_data.append({
            'DateTime': item['dt_txt'],
            'Temperature': item['main']['temp'],
            'Humidity': item['main']['humidity'],
            'Pressure': item['main']['pressure'],
            'WindSpeed': item['wind']['speed']
        })

    # -----------------------------------
    # Convert to DataFrame
    # -----------------------------------
    df = pd.DataFrame(weather_data)

    # -----------------------------------
    # Save CSV File
    # -----------------------------------
    df.to_csv("weather_data.csv", index=False)

    print("\nWeather Data:\n")
    print(df.head())

    # -----------------------------------
    # Visualization Style
    # -----------------------------------
    sns.set(style="darkgrid")

    # ===================================
    # TEMPERATURE CHART
    # ===================================
    plt.figure(figsize=(12, 6))

    sns.lineplot(
        x='DateTime',
        y='Temperature',
        data=df,
        marker='o',
        color='blue'
    )

    plt.xticks(rotation=45)

    plt.title("Temperature Forecast")

    plt.xlabel("Date and Time")

    plt.ylabel("Temperature (°C)")

    plt.tight_layout()

    plt.savefig("charts/temperature_chart.png")

    plt.close()

    # ===================================
    # HUMIDITY CHART
    # ===================================
    plt.figure(figsize=(12, 6))

    sns.barplot(
        x='DateTime',
        y='Humidity',
        data=df,
        color='green'
    )

    plt.xticks(rotation=90)

    plt.title("Humidity Forecast")

    plt.xlabel("Date and Time")

    plt.ylabel("Humidity (%)")

    plt.tight_layout()

    plt.savefig("charts/humidity_chart.png")

    plt.close()

    # ===================================
    # WIND SPEED CHART
    # ===================================
    plt.figure(figsize=(12, 6))

    sns.lineplot(
        x='DateTime',
        y='WindSpeed',
        data=df,
        marker='o',
        color='red'
    )

    plt.xticks(rotation=45)

    plt.title("Wind Speed Forecast")

    plt.xlabel("Date and Time")

    plt.ylabel("Wind Speed")

    plt.tight_layout()

    plt.savefig("charts/wind_chart.png")

    plt.close()

    # ===================================
    # SUCCESS MESSAGE
    # ===================================
    print("\nCharts Created Successfully!")

    print("\nFiles Saved:")
    print("1. weather_data.csv")
    print("2. charts/temperature_chart.png")
    print("3. charts/humidity_chart.png")
    print("4. charts/wind_chart.png")

else:

    print("Error Fetching Data")

    print("Status Code:", response.status_code)