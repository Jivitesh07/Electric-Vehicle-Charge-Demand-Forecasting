# ----------------------------------------------------------
# Step 1: Import Libraries
# ----------------------------------------------------------
import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

# ----------------------------------------------------------
# Step 2: Load the CSV Data
# ----------------------------------------------------------
# Make sure the file "ev_charging_data.csv" is in the same folder as this script
data = pd.read_csv(r"C:\Users\jivit\OneDrive\Documents\Matplotib & Seaborn\zInternship\ev_charging_data.csv")
print (data)
# Display first few rows
print("✅ EV Charging Data Loaded Successfully!\n")
print(data.head())

# ----------------------------------------------------------
# Step 3: Prepare the Data for Prophet
# ----------------------------------------------------------
# Prophet needs columns named 'ds' (date) and 'y' (value to forecast)
df = data.rename(columns={'date': 'ds', 'charging_sessions': 'y'})

# Convert date column to datetime type
df['ds'] = pd.to_datetime(df['ds'])

# ----------------------------------------------------------
# Step 4: Create and Train the Prophet Model
# ----------------------------------------------------------
model = Prophet()
model.fit(df)

# ----------------------------------------------------------
# Step 5: Make Future Predictions
# ----------------------------------------------------------
future = model.make_future_dataframe(periods=10)  # predict next 10 days
forecast = model.predict(future)

# ----------------------------------------------------------
# Step 6: Visualize the Forecast
# ----------------------------------------------------------
model.plot(forecast)
plt.title("🔋 EV Charging Demand Forecast")
plt.xlabel("Date")
plt.ylabel("Predicted Charging Sessions")
plt.show()

# ----------------------------------------------------------
# Step 7: Display the Forecasted Values
# ----------------------------------------------------------
print("\n📊 Forecasted Charging Demand for the Next 10 Days:")
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(10))

# ----------------------------------------------------------
# Step 8: (Optional) Save Forecast to CSV
# ----------------------------------------------------------
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].to_csv("forecast_results.csv", index=False)
print("\n💾 Forecast saved to 'forecast_results.csv'")