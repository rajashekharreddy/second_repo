# initializing string  
test_str = "GeeksforGeeks"
  
# using naive method to get count  
# of each element in string  
all_freq = {} 
  
for i in test_str: 
    if i in all_freq: 
        all_freq[i] += 1
    else: 
        all_freq[i] = 1
  
# printing result  
print ("Count of all characters in GeeksforGeeks is :\n "
                                        +  str(all_freq))

print(sorted(all_freq.items(), key = lambda kv:(kv[1], kv[0])))

"""from collections import OrderedDict

ord_dict = OrderedDict(all_freq)
print(ord_dict)
"""
