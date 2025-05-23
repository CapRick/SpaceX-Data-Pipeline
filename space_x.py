import pandas as pd

data =  {
    'rocket': [
        'Falcon 1',
        'Falcon 9',
        'Falccon Heavy',
    ],
    'launches':[5,100,3],
}

df = pd.DataFrame(data)
df['success_rate'] =  [0.4,0.98,1.0]
morethan5starts_df = df[df['launches']>5]
print(df)
print(morethan5starts_df)