import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = r'C:\Users\harse\Downloads\svm_data (1).csv'  # Use your dataset path
data = pd.read_csv(file_path)

# Example: Generate a bar chart for categorical data (replace 'ColumnName' with your actual column name)
column_to_visualize = 'x1'  
data[column_to_visualize].value_counts().plot(kind='bar')

# Show the plot
plt.title(f'Distribution of {column_to_visualize}')
plt.xlabel(column_to_visualize)
plt.ylabel('Count')
plt.show()

# Example: Generate a histogram for continuous data (replace 'ColumnName' with your actual column name)
column_to_visualize = 'x2'  
data[column_to_visualize].plot(kind='hist', bins=10)

# Show the plot
plt.title(f'Distribution of {column_to_visualize}')
plt.xlabel(column_to_visualize)
plt.ylabel('Frequency')
plt.show()
