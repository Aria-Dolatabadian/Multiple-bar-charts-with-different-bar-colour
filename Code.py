import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
file_path = 'data2.xlsx'  # Replace with your file path
xls = pd.ExcelFile(file_path)

# Set up the figure for the bar charts without shared x-axis
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(15, 10))

# Flatten the axes array for easier iteration
axes = axes.flatten()

# Define the maximum x-axis limits for each chart
max_x_limits = [10, 300, 20, 200]  # Adjust these values as needed for each chart

# Define labels for each subplot
labels = ['A', 'B', 'C', 'D']

# Loop through each sheet in the Excel file
for ax, sheet_name, max_x, label in zip(axes, xls.sheet_names, max_x_limits, labels):
    # Read the data from the sheet
    df = pd.read_excel(xls, sheet_name=sheet_name)

    # Clean column names by stripping whitespace
    df.columns = df.columns.str.strip()

    # Check the columns in the dataframe
    print(f"Columns in sheet '{sheet_name}': {df.columns.tolist()}")

    # Create a horizontal bar chart
    ax.barh(df['GO term'], df['Number of genes'], color=df['color'])

    # Set the title and labels
    ax.set_title(sheet_name)
    ax.set_xlabel('Number of Genes')
    ax.set_ylabel('GO term')

    # Set x-axis limits according to specified values
    ax.set_xlim(0, max_x)  # Set limit based on predefined max for each chart

    # Adjust the font size for better visibility
    ax.tick_params(axis='y', labelsize=10)  # Change y-axis label size
    ax.set_yticklabels(df['GO term'], fontsize=10)  # Adjust y-axis labels font size

    # Add the subplot label in the top-left corner
    ax.text(-0.3, 1.05, label, transform=ax.transAxes, fontsize=16, fontweight='bold', va='top')

# Adjust layout for better spacing
plt.tight_layout()
plt.show()
