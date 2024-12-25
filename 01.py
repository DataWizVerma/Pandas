import pandas as pd
data={
    'Id':["S01","S02","S03","S04","S05"],
    'Student':["Amit","John","Jacob","David","Steve"],
    'Rank':[1,2,3,5,2],
    'Marks':[95,70,80,60,90]

}

dataFrame = pd.DataFrame(data)
print("Student Record \n,datFrame")

dataFrame.insert(2,"Roll no", [101,102,103,104,105])
print(dataFrame)

dataFrame.assign(2,"Roll no", [101,102,103,104,105])
print(dataFrame)AC