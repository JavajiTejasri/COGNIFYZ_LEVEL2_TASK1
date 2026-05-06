import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("dataset.csv")

# Count table booking availability
booking_counts = df['Has Table booking'].value_counts()

print("Table Booking Availability:")
print(booking_counts)

# Calculate percentage
percentage = (booking_counts / booking_counts.sum()) * 100

print("\nPercentage Distribution:")
print(percentage)

# Plot graph
booking_counts.plot(kind='pie', autopct='%1.1f%%')

plt.title("Table Booking Availability")

plt.ylabel("")

# Save figure
plt.savefig("table_booking_distribution.png")

plt.show()