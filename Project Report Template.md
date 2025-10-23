# Electric-Vehicle-Charge-Demand-Forecasting

Electric Vehicle Charging Demand Forecasting – Project Report
1. Objective
The goal of this project is to forecast the demand for Electric Vehicle (EV) charging stations based on factors such as time, weather, and traffic conditions.
By accurately predicting charging demand, this model helps optimize charger placement, energy distribution, and customer experience.

2. Data Description
Dataset	Key Features	Source	Purpose
EV Usage Data	Date, Station ID, Charging Sessions	Simulated / Collected Data	Represents actual charging demand
Weather Data	Temperature, Rainfall, Humidity	OpenWeather / CSV	Impacts travel and charging habits
Traffic Data	Traffic Volume, Speed Index	City Traffic Reports / CSV	Correlates with EV movement and demand

3. Methodology
Data Collection & Cleaning:
Merged EV usage, weather, and traffic datasets using Python (Pandas).
Removed duplicates and filled missing values.
Filters: Weather condition, temperature range, and traffic level

5. Insights & Findings
Peak EV charging demand observed during weekends and high-traffic hours (6 PM – 8 PM).
Temperature slightly affects demand — moderate weather encourages EV use.
Forecast indicates a 10–15 % increase in demand over the next 10 days.
