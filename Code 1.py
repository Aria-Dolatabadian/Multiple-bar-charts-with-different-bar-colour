import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
file_path = 'data.xlsx'  # Replace with your actual file path
excel_data = pd.ExcelFile(file_path)

# Set up the figure size and subplot grid
fig, axes = plt.subplots(3, 6, figsize=(18, 10))  # 3 rows by 6 columns for 18 charts
axes = axes.flatten()  # Flatten to iterate over axes easily

# Loop through each sheet and create a bar plot
for i, sheet_name in enumerate(excel_data.sheet_names):
    # Read data from each sheet
    df = pd.read_excel(excel_data, sheet_name=sheet_name)

    # Extract x and y values
    x = df['Days post inoculation']
    y = df['Mean']
    yerr = df['SE']  # Standard error

    # Define custom colours for specific bars
    colours = ['cornflowerblue' if val not in ['450_14-5-1','447_14-5-1', '450_DOAB','447_DOAB']
               else 'red' if val == '450_14-5-1'
               else '#a9a9a9' if val == '447_14-5-1'
               else 'green' if val == '450_DOAB'
               else '#505050' if val == '447_DOAB'
               else 'tomato' for val in x]

    # Plot each bar chart in its corresponding subplot
    axes[i].bar(x, y, yerr=yerr, capsize=5, color=colours)
    axes[i].set_title(sheet_name)  # Title with sheet name
    axes[i].set_xlabel('Days post inoculation')
    axes[i].set_ylabel('Relative Expression')

    # Rotate x-axis labels for clarity
    axes[i].tick_params(axis='x', rotation=45)

# Hide any unused subplots if there are fewer than 18 sheets
for j in range(i + 1, len(axes)):
    fig.delaxes(axes[j])

# Adjust layout for better spacing
plt.tight_layout()
plt.show()
