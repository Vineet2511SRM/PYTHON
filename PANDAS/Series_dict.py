import pandas as pd

population_dict = {'Kerela':390,'Assam':2153,'Delhi':2020}

population = pd.Series(population_dict)
print(population)