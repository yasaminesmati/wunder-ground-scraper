"""
run this code for output

"""
from improve_scraper import Scraper
from rain import States

dataset = Scraper().timeDateCondition(2022, 10, 1, 5)

dataset['last Condition'] = dataset['Condition'].copy()

for row in dataset['Condition']:
    dataset['Condition'].replace(row, States().assignState(row), inplace=True)
    
dataset.to_csv("Dataset.csv")


