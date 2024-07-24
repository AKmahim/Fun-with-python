import pandas as pd
import json

# Load JSON data from the file
with open('gp_brac_event_day-2.json', 'r') as file:
    data = json.load(file)

# Normalize the JSON data to a flat table
df = pd.json_normalize(data['highscoreEntryList'])

# Save the DataFrame to an Excel file
df.to_excel('highscores_day_2.xlsx', index=False)

print("Data has been written to highscores.xlsx")
