# Tokyo Olympics Data Transformation Example

import pandas as pd

athletes = pd.read_csv('../data/athletes.csv')
coaches = pd.read_csv('../data/coaches.csv')
medals = pd.read_csv('../data/medals.csv')

# Basic cleaning
athletes = athletes.drop_duplicates()
coaches = coaches.drop_duplicates()

print("Athletes Dataset Shape:", athletes.shape)
print("Coaches Dataset Shape:", coaches.shape)

# Example transformation
team_counts = athletes.groupby("Team").size().reset_index(name="Total Athletes")

print(team_counts.head())
