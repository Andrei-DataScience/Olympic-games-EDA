import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

olympics_data = pd.read_csv("/kaggle/input/olympic-games/olympic_games.csv")
olympics_data.head()

missing_data = olympics_data.isnull()
missing_data_count = missing_data.sum()
print(missing_data_count)

host_countries_count = olympics_data["host_country"].value_counts().sort_values(ascending=False)
top_5_countries = host_countries_count.head()
print(top_5_countries)

host_cities_count = olympics_data["host_city"].value_counts().sort_values(ascending=False)
top_5_cities = host_cities_count.head()
print(top_5_cities)

plt.figure(figsize = (12,8))
plt.pie(x = top_5_countries.values, labels = top_5_countries.index, autopct='%1.1f%%')

plt.title("Top 5 host countries", fontweight = 'bold')

plt.tight_layout()
plt.show()

plt.figure(figsize = (12,8))
plt.pie(x = top_5_cities.values, labels = top_5_cities.index, autopct='%1.1f%%')

plt.title("Top 5 host cities", fontweight = 'bold')


plt.tight_layout()
plt.show()

def bar_plot(_x,_y,xlabel,ylabel,title):
    plt.figure(figsize = (12,8))
    sns.set(style="whitegrid")  

    sns.barplot(x=_x, y=_y, palette="crest")
    
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)

    plt.xticks(rotation=90)
  
bar_plot(host_countries_count.index, 
         host_countries_count.values, 
         xlabel="Countries",
         ylabel="Games",
         title="All host countries sorted by the number of games")

bar_plot(host_cities_count.index, 
         host_cities_count.values, 
         xlabel="Cities",
         ylabel="Games",
         title="All host cities sorted by the number of games")
