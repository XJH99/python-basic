import pandas as pd

print(pd.__version__)

# 二维数据集
myDataSet = {
    'site': ['google', 'common', 'doc'],
    'num': [1, 2, 3]
}

data = pd.DataFrame(myDataSet)
print(data)