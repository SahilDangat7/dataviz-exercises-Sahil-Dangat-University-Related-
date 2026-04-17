import pandas as pd
import numpy as np


df = pd.read_csv(r"/Users/sahilsantoshdangat/Downloads/world_happiness_2023.csv")

print(df.head(5))

# Lecture 2 — Class Exercise
# Bar Charts: World Happiness Report 2023
# Your task: Create 2 polished bar charts using the World Happiness Report dataset.
# Push to: week02/lecture02_exercise.ipynb in your own GitHub repo before the end of class.

# Rules (these will be checked in the model answer review next week)
# Every bar chart must have a zero baseline — no exceptions (SWD p.51)
# Every chart must have an insight title, not a topic title (SWD p.29)
# Aim for professional quality — clean background, readable font, no clutter
# Horizontal bars for long category names (SWD p.57)
# Setup — Run this cell first
import pandas as pd
import numpy as np

# World Happiness Report 2023 — representative data
# Source: https://www.kaggle.com/datasets/ajaypalsinghlo/world-happiness-report-2023

df = pd.read_csv(r"/Users/sahilsantoshdangat/Downloads/world_happiness_2023.csv")
df.columns = ['Country','Region','Happiness_Score','GDP','Social_Support',
              'Life_Expectancy','Freedom','Generosity','Corruption']


print(f"Dataset: {len(df)} countries, {len(df.columns)} columns")
print(df.head())
import plotly.express as px
import plotly.graph_objects as go

# Explore the dataset before you start
print("Regions in dataset:")
print(df['Region'].value_counts())
print("\nScore range:", df['Happiness_Score'].min(), "–", df['Happiness_Score'].max())
print("\nBottom 10 countries:")
print(df.nsmallest(10, 'Happiness_Score')[['Country','Region','Happiness_Score']])
# Task 1 — Regional Comparison Bar Chart
# What to build: A horizontal bar chart showing the average happiness score by region, sorted from highest to lowest.

# Requirements:

# Horizontal orientation (category names are long)
# Sorted by score, descending (so the happiest region is at the top)
# Zero baseline on x-axis
# At least one design choice that goes beyond the Plotly default (colour, annotation, labels, etc.)
# An insight title that answers: which region stands out and why does it matter?
# Hint: Use df.groupby('Region')['Happiness_Score'].mean() to compute the averages.

# Task 1: Regional comparison bar chart
# -------------------------------------

# Step 1: Compute average happiness score by region
region_avg = (df.groupby('Region')['Happiness_Score']
              .mean()
              .reset_index()
              .sort_values('Happiness_Score'))  # sort for horizontal bar

print(region_avg)

# Step 2: Build your chart
# YOUR CODE HERE
# Task 2 — Bottom vs. Top: A Contrast Story
# What to build: A bar chart that highlights the gap between the happiest and least happy countries, focusing on a specific insight.

# Requirements:

# Show the top 8 AND bottom 8 countries together (16 bars total)
# Use colour to distinguish the two groups (not Plotly's default rainbow)
# Add a visual separator or annotation that emphasises the gap
# Insight title that tells the story of the gap
# Hint: Use pd.concat([df.nlargest(8,'Happiness_Score'), df.nsmallest(8,'Happiness_Score')]) to get both groups.

# Stretch goal: Add a vertical reference line showing the global average.

# Task 2: Top 8 vs. Bottom 8 contrast
# ------------------------------------

# Step 1: Get top and bottom countries
top8 = df.nlargest(8, 'Happiness_Score').copy()
top8['Group'] = 'Top 8'
bottom8 = df.nsmallest(8, 'Happiness_Score').copy()
bottom8['Group'] = 'Bottom 8'

combined = pd.concat([bottom8, top8]).sort_values('Happiness_Score')
global_avg = df['Happiness_Score'].mean()
print(f"Global average: {global_avg:.2f}")

# Step 2: Build your chart
# YOUR CODE HERE
# Done? Stretch Goal
# If you finish both tasks with time to spare, try this:

# Task 3 (stretch): Build a grouped bar chart comparing 2 sub-factors (e.g. GDP_per_capita and Freedom) across the 5 most populated regions. Use colour meaningfully and write an insight title.

# Regions to include: 'Western Europe', 'Latin America', 'East Asia', 'Sub-Saharan Africa', 'South Asia'

# Task 3: GDP vs Freedom comparison across selected regions
# --------------------------------------------------------

import plotly.graph_objects as go

# Step 1: Filter required regions
regions_of_interest = [
    'Western Europe',
    'Latin America',
    'East Asia',
    'Sub-Saharan Africa',
    'South Asia'
]

filtered_df = df[df['Region'].isin(regions_of_interest)]

# Step 2: Compute averages
region_factors = (filtered_df.groupby('Region')[['GDP', 'Freedom']]
                  .mean()
                  .reset_index())

# Sort by GDP for better storytelling
region_factors = region_factors.sort_values('GDP', ascending=False)

print(region_factors)

# Step 3: Build grouped bar chart
fig = go.Figure()

# GDP bars
fig.add_trace(go.Bar(
    x=region_factors['Region'],
    y=region_factors['GDP'],
    name='GDP',
))

# Freedom bars
fig.add_trace(go.Bar(
    x=region_factors['Region'],
    y=region_factors['Freedom'],
    name='Freedom',
))

# Step 4: Layout improvements
fig.update_layout(
    barmode='group',
    title="Wealth does not always translate to freedom: regional gaps in GDP vs Freedom",
    xaxis_title="Region",
    yaxis_title="Average Score",
    yaxis=dict(range=[0, max(region_factors[['GDP','Freedom']].max()) * 1.2]),  # zero baseline enforced
    template='plotly_white',
    legend_title="Factor"
)

# Step 5: Clean look (remove clutter)
fig.update_traces(marker_line_width=0)

fig.show()