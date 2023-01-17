# pandas
## reading data
    import pandas as pd
    pandas.read_csv(filepath,delimiter=",",index_col=3,usecols=[1,2,3],dtype="float32",skiprows=3,skipfooter=3,skip_blank_lines=True,comment="#")
    df=pd.read_csv("abc.txt")
    df.values to get a numpy ndarray.
    df.index
    df.columns
    df.head()
    df.tail()

## intro
- it is the most important package.
- useful for processing high dimentional data.
- in numpy we can't attach a label to data.
- built on top of numpy.
- works on relational data.

## pandas objects:
- Series
- Dataframes

data wrangling is same as data cleaning.
```python
import numpy as np
import pandas as pd

```
# Series
```python
s=pd.Series([1,2,3,4,5])
"we get it like a dictionary ,there are keys called index that starts with 0 it is called implicit index"
```
- the data type is that of most expressive type.
- s.values
- s.index
- can for i in loop as well.
    - for item in zip(s.index,s.values)
    
```
mass=pd.Series([1,2,3],index=["mars","jup","uranus"])
mass["mars"] would work.
mass.mars will also work.
s=pd.Series(np.array([1,2,3]))
can make out of numpy arrays as well.
can even create from dictionaries.
mars=pd.Series(dictionary)
here if we put index parameter,only those ones are imported.


```
## indexing:
- s.loc[4] as per index defined.
- s.iloc[0:2] this is implicit indexing[0,2)
- there two are better way.
- s.loc["mass":"diameter] here both inclusive.
- : for all
- Series is 1D and Dataframe is 2D

## operations on series
- mass>100 returns boolean series.
- mass[mass>100] returns on those that satisfy as Series.
- & |~ ^ remain the same.
- mass * 2 all values,not the indexes.
- np.mean(series) also works
- same for np.amin,np.median as np and pd are compatible.
- mass[pd.isnull(mass)]
- pd.isnull(mass) gives boolean series.

### adding/removing an element:
    - mass["moon"]= 0.7
    - mass.drop(["pluto"])
- np.pi
- you can divide the series.
- np.power(a,3)
- if index not matching,then it will give Nan as output for that index.
- np.mean(mass) works even if Nans in data,it avoids them.
- density[pd.isnull(density)]=np.mean(density)
    - it  will replace all Nan's
- dictionaries are faster(2 times) for indexing,but slower for operations like 50 times.

reading Series:
- s=pd.read_csv("abc.csv",index_col=0).iloc[:,0] we get a series.
- a.head(25)
- a.tail(25)
- we can apply any np function on pd.
- np.std(series)
- indexing is magic
- pd does alignment of indices first,like when you subtract etc.
- len(array)
- pd.Timestanp(date) converts strings to data,like 01-jan-2019 to 2019-01-01 00:00:00
    - d.dayofweek returns 0 to 6
- a1.a.copy()
- series2=pd.Series(series1,index=new_index)
- np.sum(boolean array) is love,gives 1 for True and 0 for False.


# Dataframe objects:
- generalization of series.
- given a 2D array
- df=pd.DataFrame(arr) , arr can be a numpy array.and df is a typical name.
- it automatically adds row name and column name as numbers starting from 0
- df.values gives us numpy array.
- df.index 
- df.columns
- df.values[0] gives first row.
- df.index=["r1","r2","r3"]
- df.columns=["c1","c2"]

## indexing:
- df.loc["r2","c2"]
- df.iloc[2,1]
- df.iloc[2:4,1:3] slicing gives dataframe as output.
- df.loc["r2":"r4","c2":"c4"]
- df.iloc[0] gives first row,it returns a series.
- dataframe is a collection of series.
- we can make series out of a row as well as from a column.
- df.shape
- df.T
- creating a DataFrame out of Series
    - df=pd.DataFrame({"mass":mass,"diameter":diameter})
    - here now mass and diameter asre going to be the name of the columns
    - index should be same in both.

- DataFrame funtion is overloaded as it can take different kind of inputs,like dixts,arrays etc.

- df["mass"] that column
- df["mass"]["earth"] ther earth is a row index
- df["new col"]=0
- df[c][r]=33
- df.loc["earth"] accessing row
- df.loc[:,"mass"] to access a column

adding a new row:
- df.loc["row"]=0 or list of numbers
- df.drop("rowname")
- df.drop("columnname",axis=1,inplace=True)
- df.mean() to each column adn returns a series.
- df.mean(axis=1) mean for each row
- df.median()
- df.min()
- df.max()
- df.describe()
- df.info() the rows columns etc,best one.
- df.describe() gives you statistics about data,it gives us count so we can tell how many missing values.
- always use inbuilt functions first.
- dropping rows with null values:
    -df.dropna(inplace=True)

## query with dataframe
- df[(df["year"]>=100) & (df["mean"]==7)] it shows only those rows.
- df.count()

## reading json files
     df=pd.read_json("data.json")
     where data.json is like [{},{}]
     but this gives only one column maybe for {},{},{} it might give better.
    import json
    with open("data.json") as f:
        data=json.load(f)
        data=data["states_only']
        gives us list of objects.
        df=pd.json_normalize(data) here data is a dict.
- in json all are of object type.
- pd.to_numeric(df.tn) for typecasting
- df=df.appy(to_numeric) for all
- df.col1.unique() returns array of all unique values.
- if values are long strings then keep a dict for them and use abbrevations in df so size of data remains same.
- df["c2"]=df["c2"].apply(f1)
    - where f1 is a function that takes a value and returns a value.
    - it applies same function to each row.
- .count() gives no.of rows.
- df.groupby("method")["method"].count()
- pd.read_csv("abc.csv",index_col=0) to avoid creating extra column.
- Date is the best index.
- to combine frames pd.concat(df1,df2,axis=1) for sideways and 0 for beneath it.
- df.shape
- df[[c1,c2,c3]]
- pd.to_numeric(data.coffee,erros="coerce") wherever error put Nan
- data=data.coffee.astype(int)
- pd.to_datatime(data.t)
- df.describle(include="all")
- pd.read_excel("abc.xlsx
- for index,row in df.iternows()
- df.sort_values("c1",ascending=False)
    - can give a list of columns to sort basedon.
- to change position of columns
    - df=df[["c1","c3","c2"]]
    - or cols=list(df.columns.values)
- df.to_csv("abc.csv",index=False) 
- df.to_excel(same) can put sep="\t"
- of 100 gb of data
    -for df in pd.read_csv("abc.csv",chunksize=5000): for 5000 rows at a time.
    