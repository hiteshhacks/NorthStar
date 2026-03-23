import pandas as pd

def demographic_parity(df, sensitive, target):
    groups = df.groupby(sensitive)[target].mean()
    return groups.to_dict()


def disparate_impact(df, sensitive, target):
    groups = df.groupby(sensitive)[target].mean()
    min_val = groups.min()
    max_val = groups.max()
    
    if max_val == 0:
        return 0
    
    return float(min_val / max_val)