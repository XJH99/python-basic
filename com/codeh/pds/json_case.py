import pandas as pd
import json
"""

"""

df = pd.read_json('test.json')
print(df.to_string)

s = {
    "col1":{"row1":1,"row2":2,"row3":3},
    "col2":{"row1":"x","row2":"y","row3":"z"}
}

df1 = pd.DataFrame(s)
print(df1)

df2 = pd.read_json('https://static.runoob.com/download/sites.json')
print(df2)

with open('test.json', 'r') as f:
    data = json.loads(f.read())

df_nested_list = pd.json_normalize(data, record_path=['students'], meta=['school_name', 'class'])
print(df_nested_list)


