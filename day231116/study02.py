import pandas as pd

df1 = pd.DataFrame({
   'A': ['A0', 'A1', 'A2', 'A3'],
   'B': ['B0', 'B1', 'B2', 'B3'],
   'C': ['C0', 'C1', 'C2', 'C3'],
   'D': ['D0', 'D1', 'D2', 'D3']
})

df2 = pd.DataFrame({
   'A': ['A4', 'A5', 'A6', 'A7'],
   'B': ['B4', 'B5', 'B6', 'B7'],
   'C': ['C4', 'C5', 'C6', 'C7'],
   'D': ['D4', 'D5', 'D6', 'D7']
})

result = pd.concat([df1, df2])
print(df1)
print(result)

df3 = pd.DataFrame({
   'A': ['A4', 'A5', 'A6', 'A7'],
   'B': ['B4', 'B5', 'B6', 'B7'],
   'c': ['C4', 'C5', 'C6', 'C7'],
   'd': ['D4', 'D5', 'D6', 'D7']
})

result = pd.concat([df1, df3] , ignore_index=True)
print(result)

result = pd.concat([df1, df2], ignore_index=True)
print(result)



left = pd.DataFrame({
   'A': ['A0', 'A1', 'A2'],
   'B': ['B0', 'B1', 'B2']},
   index = ['K0', 'K1', 'K2']
)

right = pd.DataFrame({
   'C': ['C0', 'C2', 'C3'],
   'D': ['D0', 'D2', 'D3']},
   index = ['K0', 'K2', 'K3']
)

result = left.join(right)
print(result)

result = left.join(right, how='outer')
print(result)