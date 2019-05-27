import pandas as pd
p_value = pd.Dataframe({'앞면이 나온 횟수':x, '확률': y}).query(
    '앞면 횟수 >= 15'
)['확률'].sum()
print(p_value)

# 0.020694732666
