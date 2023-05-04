import pandas as pd
import random
rowNum = 200
colNum = 100
rows = []
cols = []
data = [[random.randint(0, 9) for j in range(colNum)] for i in range(rowNum)]
for i in range(rowNum):
    rows.append('tispc'+str(i+1))
for i in range(colNum):
    cols.append('label'+str(i+1))
df = pd.DataFrame(data=data, index=rows, columns=cols)
# for index, row in df.iterrows():
#     print(f"Row {index}:")
#     for col_name, value in row.iteritems():
#         print(f"Column {col_name}: {value}")
sum=0
for i in range(rowNum):
    count=0
    # 选取第二行进行归一化处理
    row_to_normalize = df.iloc[i]

    # 计算该行所有元素的和
    row_sum = row_to_normalize.sum()

    # 对该行元素进行归一化处理
    normalized_row = row_to_normalize / row_sum

    df.iloc[i]=normalized_row
    for j in range(colNum):
        if df.iloc[i,j]>=0.0153:
            count+=1
        #print(df.iloc[i,j])
    print(count)
    sum+=count
    print("----------")
df.to_csv('toolIndicatorSPC_label.csv', index=True)
print("toolIndicatorSPC-label-number:",sum)