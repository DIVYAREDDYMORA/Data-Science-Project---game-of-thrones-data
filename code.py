


import pandas as pd

import numpy as np

battle = pd.read_csv('battles.csv')

battle.head()

battle.shape

#this command is to change the column name from the attacker_1 to primary_attacker in the dataset by using rename and inplace(dataset)
battle.rename(columns={'attacker_1': 'primary_attacker'},inplace=True)

battle.head()

#to know how many times the king attacked some one
battle['attacker_king'].value_counts()

#to know how many battles occured in the location 
battle['location'].value_counts()

#libraries for visualization are seaborn and matplotlib-pyplot
import seaborn as sns

from matplotlib import pyplot as plt

#to know the army size for the battle (of attackers)
sns.set(rc={'figure.figsize':(13,5)})#here 13 is width size and 5 is height of the graph
sns.barplot(x='attacker_king',y='attacker_size',data=battle)
plt.show()

#to know the army size for the battle (of defenders)
sns.set(rc={'figure.figsize':(13,5)})
sns.barplot(x='defender_king',y='defender_size',data=battle)
plt.show()

# to know the battle patterns
sns.countplot(x=battle['attacker_king'],hue=battle['battle_type'])
plt.show()

death = pd.read_csv('character-deaths.csv')
death.head()

death.shape

death['Gender'].value_counts()

death['Nobility'].value_counts()

sns.countplot(death['Death Year'])
plt.show()

sns.set(rc={'figure.figsize':(30,10)})
sns.countplot(death['Allegiances'])
plt.show()







