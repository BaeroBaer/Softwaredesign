list1=[1,2,3,4,5]
list2=[11,12,13,14,15]
list_zipped=[]
list_odd=[]
list_zip_reversed=[]


## schleife fuer zipped
for i in range(len(list1)):
    list_zipped.append(list1[i])
    list_zipped.append(list2[i])
    
print(list_zipped)
## schleife fuer odd
for i in range(len(list1)):
    if list1[i]%2!=0:
        list_odd.append(list1[i])
    if list2[i]%2!=0:
        list_odd.append(list2[i])

print(list_odd)

## schleife fuer reversed zipped
for r in reversed(list1):
    list_zip_reversed.append(list1[i])
    list_zip_reversed.append(list2[i])

print(list_zip_reversed)  



