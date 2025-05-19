import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data from Excel
file_path = 'live 003.xlsx'  # Make sure this matches your uploaded file
df = pd.read_excel(file_path)

# Normalize column names
df.columns = df.columns.str.strip().str.lower()

# Print actual column names for debugging if needed
# print(df.columns)

# Set Seaborn theme
sns.set_theme(style="darkgrid")

# Dictionary to map choice to chart title
chart_titles = {
    1: "Profit Bar Plot",
    2: "Loss Bar Plot",
    3: "Profit Trend Line Plot",
    4: "Loss Trend Line Plot",
    5: "Profit vs Loss Scatter Plot",
    6: "Histogram of Profits",
    7: "Box Plot of Profits by Year",
    8: "Violin Plot of Losses by Year",
    9: "Heatmap of Profit and Loss"
}

# Function to show all selected charts in subplots
def show_multiple_charts(choices):
    n = len(choices)
    cols = 2 if n > 1 else 1
    rows = (n + 1) // 2 if n > 1 else 1

    fig, axes = plt.subplots(rows, cols, figsize=(10 * cols, 5 * rows))
    fig.suptitle("SELVA ", fontsize=32, y=1.00)

    # Ensure axes is iterable
    axes = axes.flatten() if n > 1 else [axes]

    for i, choice in enumerate(choices):
        ax = axes[i]
        title = chart_titles.get(choice, f"Chart {choice}")

        if choice == 1:
            sns.barplot(x="year", y="profit", data=df, palette="viridis", ax=ax)
        elif choice == 2:
            sns.barplot(x="year", y="loss", data=df, palette="coolwarm", ax=ax)
        elif choice == 3:
            sns.lineplot(x="year", y="profit", marker="o", color="green", data=df, ax=ax)
        elif choice == 4:
            sns.lineplot(x="year", y="loss", marker="x", color="red", data=df, ax=ax)
        elif choice == 5:
            sns.scatterplot(x="profit", y="loss", data=df, hue="year" if "year" in df.columns else None, ax=ax)
        elif choice == 6:
            sns.histplot(df['profit'], kde=True, color="purple", ax=ax)
        elif choice == 7:
            sns.boxplot(x="year", y="profit", data=df, palette="Set2", ax=ax)
        elif choice == 8:
            sns.violinplot(x="year", y="loss", data=df, palette="Set3", ax=ax)
        elif choice == 9:
            heatmap_data = pd.pivot_table(df, values=["profit", "loss"], index="year")
            sns.heatmap(heatmap_data, annot=True, fmt=".0f", cmap="coolwarm", ax=ax)

        ax.set_title(title, fontsize=18)
        ax.tick_params(axis='x', rotation=45)

    # Hide any unused subplots
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout(rect=[0, 0, 1, 0.97])
    plt.show()


# Menu interface for multiple charts
try:
    print("Select chart(s) to display (e.g. 1,3,5):")
    for i in range(1, 10):
        print(f"{i}: {chart_titles[i]}")

    user_input = input("Enter your choice(s), comma-separated: ")
    choices = [int(c.strip()) for c in user_input.split(',') if c.strip().isdigit()]
    show_multiple_charts(choices)

except Exception as e:
    print(f"An error occurred: {e}")
