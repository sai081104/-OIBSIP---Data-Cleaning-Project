# Data Cleaning - OIBSIP Data Analytics Task

# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv("AB_NYC_2019.csv")

# Display first 5 rows
print("Dataset Preview:\n", data.head())

# Check for missing values
print("\nMissing Values:\n", data.isnull().sum())

# Drop columns with more than 30% missing values
threshold = len(data) * 0.3
data = data.dropna(thresh=threshold, axis=1)

# Handling remaining missing values
data["reviews_per_month"].fillna(0, inplace=True)

# Check data types
print("\nData Types:\n", data.dtypes)

# Convert 'last_review' to datetime
data["last_review"] = pd.to_datetime(data["last_review"], errors='coerce')

# Standardize 'price' column (Remove outliers)
q1 = data["price"].quantile(0.25)
q3 = data["price"].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

# Filter out outliers
data = data[(data["price"] >= lower_bound) & (data["price"] <= upper_bound)]

# Remove duplicates
data.drop_duplicates(inplace=True)

# Visualization: Distribution of Price
plt.figure(figsize=(12, 6))
sns.histplot(data["price"], bins=30, kde=True, color="blue")
plt.title("Price Distribution After Outlier Removal")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# Visualization: Room Type Distribution
plt.figure(figsize=(10, 6))
sns.countplot(x="room_type", data=data, palette="viridis")
plt.title("Room Type Distribution")
plt.xlabel("Room Type")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# Check for remaining missing values
print("\nRemaining Missing Values:\n", data.isnull().sum())
