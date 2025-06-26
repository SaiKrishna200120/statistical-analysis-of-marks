import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import Patch

def plot_grade_distributions(input_file_2020, input_file_2024):
    # Read the 2020 file that is in intervals
    df_2020 = pd.read_csv(input_file_2020, header=None, delim_whitespace=True)
    df_2020.columns = ['min_score', 'max_score', 'count']

    # Generate a list of grades for each student based on the intervals and counts for 2020
    grades_2020 = []
    for index, row in df_2020.iterrows():
        grades_2020.extend(np.linspace(row['min_score'], row['max_score'], row['count'], endpoint=False))
    df_2020_array = np.array(grades_2020)

    # Calculation of mean and standard deviation for 2020
    mean_2020 = np.mean(df_2020_array)
    std_2020 = np.std(df_2020_array)

    # value V for 2020
    below_25 = df_2020[df_2020['max_score'] < 25]
    total_students = df_2020['count'].sum()
    students_below_25 = below_25['count'].sum()
    V_2020 = students_below_25 / total_students
    V_2020_percentage = V_2020 * 100

    # Read the 2024 file
    df_2024 = pd.read_csv(input_file_2024, header=None, delim_whitespace=True)
    df_2024_array = df_2024[0].to_numpy()

    # Calculation of mean and standard deviation for 2024
    mean_2024 = np.mean(df_2024_array)
    std_2024 = np.std(df_2024_array)

    # Plotting the histograms for 2020 and 2024
    plt.figure(figsize=(20, 13))
    bins = range(0, 110, 3)

    # customization of both histograms
    counts_2020, bins_2020, bars_2020 = plt.hist(df_2020_array, bins=bins, alpha=0.8, label='2020 Grades',
                                                  color='#1f77b4',
                                                  edgecolor='black', density=True)
    counts_2024, bins_2024, bars_2024 = plt.hist(df_2024_array, bins=bins, alpha=0.8, label='2024 Grades',
                                                  color='#afb41f',
                                                  edgecolor='black', density=True)

    # Highlighting the bars for V value in 2020 histogram
    for bar, bin_edge in zip(bars_2020, bins_2020):
        if bin_edge < V_2020_percentage:
            bar.set_facecolor('red')
            bar.set_alpha(0.9)
            bar.set_label('2020 grade who scored under 25')

    # Mean and standard deviation lines for 2020 and 2024, formatted to two significant figures
    plt.axvline(mean_2020, color='chocolate', linestyle='-', linewidth=1.5, label=f'2020 Mean: {mean_2020:.2f}')
    plt.axvline(mean_2020 + std_2020, color='olive', linestyle='-', linewidth=1.5,
                label=f'2020 Std Dev: {std_2020:.2f}')
    plt.axvline(mean_2024, color='darkcyan', linestyle='-', linewidth=1.5, label=f'2024 Mean: {mean_2024:.2f}')
    plt.axvline(mean_2024 + std_2024, color='deeppink', linestyle='-', linewidth=1.5,
                label=f'2024 Std Dev: {std_2024:.2f}')

    # Value V line for 2020, formatted to two significant figures
    plt.axvline(V_2020_percentage, color='darkviolet', linestyle='-', linewidth=1.5,
                label=f'2020 V : {V_2020_percentage:.2f}%')

    # Adjust the legend
    highlighted_patch = Patch(color='red', label='2020 grade who scored 25')
    handles, labels = plt.gca().get_legend_handles_labels()
    handles.append(highlighted_patch)
    by_label = dict(zip(labels, handles))  # Remove duplicates
    plt.legend(by_label.values(), by_label.keys(), fontsize=13, loc='upper right', frameon=True, framealpha=0.9,
               shadow=True, borderpad=1)

    plt.title('Grade Distributions for 2020 and 2024', fontsize=16, fontweight='medium')
    plt.xlabel('Marks in range', fontsize=20)
    plt.ylabel('Count of student', fontsize=20)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)

    plt.grid(True, linestyle='-', linewidth=0.5, color='gray')

    # Student ID
    plt.text(26, 0.017, 'Student ID: 23022047', fontsize=18, color='#1f77b4', ha='right')

    plt.show()

# Example usage of the function
plot_grade_distributions('2020input7.csv','2024input7.csv')
