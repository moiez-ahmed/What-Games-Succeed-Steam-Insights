import requests
import pandas as pd

url = "https://steamspy.com/api.php?request=all"
response = requests.get(url)

data = response.json()
df = pd.DataFrame(data.values())

print(df.head())
print(df.info())
print(df.describe())

