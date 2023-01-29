import pandas as pd

# Import the data from the csv file
data = pd.read_csv("heighwidth.csv")

# Find the mean of the "Weight(Pounds)" column
mean_height = data["Weight(Pounds)"].mean()

# Find the median of the "Weight(Pounds)" column
median_height = data["Weight(Pounds)"].median()

# Find the mode of the "Weight(Pounds)" column
mode_height = int(data["Weight(Pounds)"].mode()[0])

# Print the results
print("Mean height:", mean_height)
print("Median height:", median_height)
print("Mode height:", mode_height)
