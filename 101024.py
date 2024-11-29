import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'usa_rain_prediction_dataset_2024_2025.csv'
data = pd.read_csv(file_path)

# Create a boxplot for Temperature
plt.figure(figsize=(8, 6))
plt.boxplot(data['Temperature'])
plt.title('Boxplot of Temperature')
plt.ylabel('Temperature (°F)')
plt.show()

# Create a scatterplot for Temperature vs. Humidity
plt.figure(figsize=(8, 6))
plt.scatter(data['Temperature'], data['Humidity'], alpha=0.6)
plt.title('Scatterplot of Temperature vs. Humidity')
plt.xlabel('Temperature (°F)')
plt.ylabel('Humidity (%)')
plt.show()


