## Filter Function Python
`map` this function takes 2 parameters, the first parameter is the function that you want to apply to the map iteratable, ane the second parameter will be a collection of iteratable.

  
<p align="center">
  <img src="https://img.shields.io/static/v1?label=language&message=python&color=green"/>
</p>

### Examples
1. map on sets `lambda-function`:

```python 

my_set = {i for i in range(10)}                                                   
result = map(lambda x: x % 2 == 0, my_set) 
print(list(result))         ##  [True, False, True, False, True, False, True, False, True, False]                                                       
```

2. map on list:
```python
my_list = ["name1", "name2", "name3", "name4", "name5"]                                         
res = map(len, my_list)                                 
print(list(res))       ##   [5, 5, 5, 5, 5]                                
```

3. map and a user defined function.

```python
                                                             
my_list = ["name1", "name2", "name3", "name4", "name5"]      
                                                             
def upper(i):                                                
    return i.upper()                                         
res = map(upper, my_list)                                    
print(list(res))         ## ['NAME1', 'NAME2', 'NAME3', 'NAME4', 'NAME5']                                    
```

> That's the basics about the map function