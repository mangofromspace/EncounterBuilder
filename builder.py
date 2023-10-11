import csv
import random
import pandas as pd

#player difficulty based on exp values given by Wizard's of the Coast in their Dungeon Master Guide Book
playerdif = {}

class Encounter:

    def __init__(self):
        self.monster =  {}
        self.names = []
        self.exp = []
        #TODO: import info from csv into object Encounter 
        #import info from dd5e_monsters.csv from https://www.kaggle.com/datasets/patrickgomes/dungeons-and-dragons-5e-monsters/data
         #monsters only from monster manual
        df =pd.read_csv('Dd5e_monsters.csv')
        name = df['Name']
        size = df['Size']
        df[['Race', 'Alignment']] = df['Race + alignment'].str.split(",",n=1,expand=True)
        race = df['Race']
        alignment = df['Alignment']
        #Could drop the original column with:
        #df.drop('Race + alignment', axis=1, inplace=True)
        #cleaning unused columns
        df.drop(['HP','Armor','Speed'], axis=1, inplace=True)
        


    
    #TODO: Calculate Difficulties
    #TODO: Make a random generator that generates a encounter that is practical and meets the rerquirement
    #TODO: Make the monsters already chosen have a higher weight of being chosen
    #TODO: Calculate Modifier based on party size
