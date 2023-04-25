import pandas as pd

def df_sort(df, feature):
    features = [i for i in range(len(df))]
    df[feature] = features
    return df.sort_values(feature, ascending=True)

# 创建一个 DataFrame
df = pd.DataFrame({
    'name': ['Tom', 'Jack', 'Mary'],
    'age': [20, 25, 18],
    'grade': [80, 90, 85]
})

print(df_sort(df, 'ok'))