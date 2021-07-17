import pandas as pd
mydataset = {
  'sites': ["Google", "Runoob", "Wiki"],
  'number': [1, 2, 3]
}
my = pd.DataFrame(mydataset)

a = ["Google", "Runoob", "Wiki"]

myvar = pd.Series(a,index=['x','y','z'])

sites = {'a': "Google", 'c': "Runoob", 3: "Wiki"}

myvar = pd.Series(sites,index=['a','c'])

print(myvar)