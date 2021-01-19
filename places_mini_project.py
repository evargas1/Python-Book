where_was_paul = ['jersuelm', 'rome', 'ceasera', 'italy', 'macedonia', 'troas', 'neapolis']


# indexing and captializing
print("Paul needed to make it to " + where_was_paul[1].title() + " to fullfill Jehovahs will but first he went to " + str(len(where_was_paul)) + " places." )
# replace an item in the list
where_was_paul[3] = 'shipwreck'
print(where_was_paul)
# adds item to the end of the list
where_was_paul.append('withfestus')
print(where_was_paul)
# adds item to front of the list
where_was_paul.insert(0, 'jail')
print(where_was_paul)
# remove last item in the list
del where_was_paul[-1]
print(where_was_paul)
print(len(where_was_paul))

# poped method
last_item = where_was_paul.pop()
middle_item = where_was_paul.pop(4)
print(where_was_paul, len(where_was_paul))
print(last_item)
print(middle_item)


print("Pual experinced " + str(middle_item) + " many times and Jehovah always protected him.")
print("\nMany of Puals friends went with him to " + str(last_item))


# .sort is perm and sorted is temp which can be seen becasue it does not have a "." 

print("orignal list: ")
print(where_was_paul)
print("Sorted list: ")
print(sorted(where_was_paul))
print("Sorted list backwards: ")
print(sorted(where_was_paul, reverse=True))
print("Orignal list: ")
print(where_was_paul, len(where_was_paul))
