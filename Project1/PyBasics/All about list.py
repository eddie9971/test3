nlist1 = [[]]
nlist2 = [[1,2],[3,4,5]]
# create a list with list comprehension
nlist_comp1 = [[i for i in range(5)], [i for i in range(7)], [i for i in range(3)]]
nlist_comp2 = [[i for i in range(n)] for n in range(3)]
print(nlist_comp1)
print(nlist_comp2)
# append a list
list1 = [8, 7, 6]
nlist_comp1.append(list1)
print(nlist_comp1)
# concat nested lists
concat_nlist = nlist_comp1 + nlist_comp2
print(concat_nlist)
concat_nlist.reverse()
print(concat_nlist)
# reverse sub elements of nested list
for _list in concat_nlist:
   _list.reverse()
print(concat_nlist)
# reverse sub elements + elements of a nested list
for _list in concat_nlist:
   _list.reverse()
concat_nlist.reverse()
print(concat_nlist)
# flatten list
flat_list = [ele for sublist in concat_nlist for ele in sublist]
print(flat_list)

# 排序
list = [11,22,44,1,6,8,3,28,53,45]
list.sort() #从小到大
list.sort(reverse=True) #从大到小

print(list)

# 相加
list2 = [1,2,3]
list3 = list+list2

# if in a list 敏感词替换
forbidden_list = ['fuck','shit']
text = 'fuck this shit'
for item in forbidden_list:
   text = text.replace(item,'***')
print(text)