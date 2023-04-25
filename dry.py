import pandas as pd

def df_sort(df):
    return df.sort_values('grade', ascending=True)

# 创建一个 DataFrame
df = pd.DataFrame({
    'name': ['Tom', 'Jack', 'Mary'],
    'age': [20, 25, 18],
    'grade': [80, 90, 85]
})

print(df_sort(df))