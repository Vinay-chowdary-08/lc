import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    x = animals[animals["weight"] >100]
    sorted_values = x.sort_values(by = "weight", ascending = False )
    return sorted_values[["name"]]