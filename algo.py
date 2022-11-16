# shuffle: Creates a random array


"insertion sort:"

# from random import shuffle
# import time


# start = time.time()

# def insertion_sort(arr):
#     length = len(arr)
#     for i in range(1, length):
#         j = i - 1
#         key = arr[i]
#         while j >= 0 and arr[j] > key:
#             arr[j + 1] = arr[j]
#             j -= 1
#         else:
#             arr[j + 1] = key
    
#     return arr

# len_ = 10
# lst = [item for item in range(len_)]
# shuffle(lst)
# print(lst)
# ins = insertion_sort(lst)
# print(ins)
# print(time.time() - start,"s")

"-----------------------------------------------------------"

"insertion sort with show graph:"


# plt.clf: Deletes the previous mode

# from random import shuffle
# import matplotlib.pyplot as plt



# def insertion_sort(arr):
#     length = len(arr)
#     for i in range(1, length):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and arr[j] > key:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key

#         plt.bar(range(length), lst)
#         plt.pause(1)
#         plt.clf()

#     return arr

# len_ = 10
# lst = [item for item in range(len_)]
# shuffle(lst)
# b = insertion_sort(lst)
# print(b)
# plt.bar(range(len_), lst)
# plt.show()

"--------------------------------------------------------------"

"selection sort:"

# from random import shuffle


# def selection_sort(arr):
#     length = len(arr)
#     for i in range(length - 1):
# 	    minIndex = i
# 	    for j in range(i+1, length):
# 		    if arr[j] < arr[minIndex]:
# 			    minIndex = j
# 	    else:
# 		    arr[i], arr[minIndex] = arr[minIndex], arr[i]

#     return arr

# len_ = 20
# lst = [item for item in range(len_)]
# shuffle(lst)
# print(lst)
# print(selection_sort(lst))

"----------------------------------------------------------------"

"selection sort with show graph:"

# plt.clf: Deletes the previous mode

# from random import shuffle
# import matplotlib.pyplot as plt



# def selection_sort(arr):
#     length = len(arr)
#     for i in range(length - 1):
#         minIndx = i
#         for j in range(i + 1, length):
#             if arr[j] < arr[minIndx]:
#                 minIndx = j
        
#         arr[i] , arr[minIndx] = arr[minIndx] , arr[i]
#         plt.bar(range(length), lst)
#         plt.pause(1)
#         plt.clf()
#     return arr
	
# len_ = 20
# lst = [item for item in range(len_)]
# shuffle(lst)
# plt.bar(range(len_), lst)
# plt.show()
# print(selection_sort(lst))

"-----------------------------------------------------------------"

"bubble sort:"

# from random import shuffle



# len_ = 20
# lst = [item for item in range(len_)]
# shuffle(lst)

# def bubble_sort(arr):
#     length = len(arr)
#     for i in range(length - 1):
#         for j in range(length - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1] , arr[j]

#     return arr

# bub = bubble_sort(lst)
# print(bub)

"--------------------------------------------------------------"

"bubble sort with graph:"

# import matplotlib.pyplot as plt
# from random import shuffle



# def bubble_sort(arr):
#     length = len(arr)
#     for i in range(length - 1):
#         for j in range(length - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] =  arr[j + 1] , arr[j]

#             plt.bar(range(len_), lst)
#             plt.pause(0.005)
#             plt.clf()

#     return arr

# len_ = 5
# lst = [item for item in range(len_)]
# shuffle(lst)
# bub = bubble_sort(lst)
# print(bub)
# plt.bar(range(len_), lst)
# plt.show()

"merge sort:"
# from random import shuffle
# from matplotlib import pyplot as plt



# def merge_sort(lst):
#     _len = len(lst)
#     if len(lst) > 1:
#         mid = len(lst) // 2
#         left = lst[:mid]
#         right = lst[mid:]
#         merge_sort(left)
#         merge_sort(right)
#         i = 0
#         j = 0
        
#         k = 0
        
#         while i < len(left) and j < len(right):
#             if left[i] <= right[j]:
#               lst[k] = left[i]
#               i += 1
#             else:
#                 lst[k] = right[j]
#                 j += 1
           
#             k += 1
            
#         while i < len(left):
#             lst[k] = left[i]
#             i += 1
#             k += 1

#         while j < len(right):
#             lst[k]=right[j]
#             j += 1
#             k += 1
#         plt.bar(range(_len), lst)
#         plt.pause(0.5)
#         plt.clf()


# len_ = 10
# lst_ = [item for item in range(len_)]
# shuffle(lst_)
# plt.bar(range(len_), lst_)
# plt.show()
# print(lst_)
# mrg = merge_sort(lst_)
# print(lst_)


"linked list / sll: "
"یکسری گره که توی حافظه زنجیروار بهم وصله"
"اولین ند میگن first or start or head."

"class node:"
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None

"class linked list:"
# class Sll:
#     def __init__(self, head):
#         self.head = head

#     def __repr__(self):
#         str_ = ""
#         temp = self.head
#         while temp.next:
#             str_ += str(temp.value) + " -> "
#             temp = temp.next
#         else:
#             str_ += str(temp.value)
#         return str_

#     def add_first(self, value):
#         new_node = Node(value)
#         new_node.next = self.head
#         self.head = new_node

#     def add_last(self, value):
#         new_node = Node(value)
#         temp = self.head
#         while temp.next:
#             temp = temp.next
#         else:
#             temp.next = new_node

#     def delete(self, value):
#         temp = self.head
#         if temp.value == value:
#             if temp.next == None:
#                 self.head = None
#         while temp.next:
#             if temp.next.value == value:
#                 temp.next = temp.next.next
#                 break

# head = Node(15)
# mi = Sll(head)
# mi.add_first(9)
# mi.add_first("hasan")
# mi.add_last("ali")
# print(mi)
# mi.delete("hasan")
# print(mi)


"--------------------------------------------------------------"
"Circular Linked List:"

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

#     def __repr__(self):
#         return f"{self.data}"


# class Cll:
#     def __init__(self):
#         self.head = None
#         self.tail = None
    
#     def insert_first(self, data):
#         new_node = Node(data)
#         if self.head == None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             new_node.next = self.head
#             self.head = new_node
#             self.tail.next = self.head
            
#     def insert_last(self, data):
#         new_node = Node(data)
#         if self.head == None:
#             self.head = new_node
#             self.tail = new_node
#         else:
#             self.tail.next = new_node
#         self.tail = new_node
#         self.tail.next = self.head
    
#     def insert_index(self, data, index):
#         new_node = Node(data)
#         temp = self.head
#         count = 1
#         while temp.next != None and count < index:
#             temp = temp.next
#             count += 1
#         new_node.next = temp.next
#         temp.next = new_node
    
#     def delete_first(self):
#         if self.head == None:
#             print("NO nodes")
#         else:
#             self.head = self.head.next
#             self.tail.next = self.head
    
#     def delete_last(self):
#         if self.head == None:
#             print("NO nodes")
#         elif self.head.next == None:
#             self.head = None
#         else:
#             temp = self.head
#             while temp.next != self.tail:
#                 temp = temp.next
#             self.tail = temp
#             temp.next = self.head
    
#     def delete_index(self, index):
#         if self.head == None:
#             print("NO nodes")
#         else:
#             temp = self.head
#             count = 1
#             while temp.next != None and count < index:
#                 temp = temp.next

#                 count += 1
#             temp.next = temp.next.next
    
#     def display(self):
#         temp = self.head
#         if self.head == None:
#             print("NO nodes")
#         while temp != None:
#             print(temp.data, "-->", end=" ")
#             temp = temp.next
#             if temp == self.head:
#                 break
    
#     def search(self, data):
#         if self.head == None:
#             print("NO nodes")
#         else:
#             temp = self.head
#             count = 0
#             while temp:
#                 count += 1
#                 if temp.data == data:
#                     print(data, " found at Position-->", count)
#                     return
#                 temp = temp.next
#                 if temp == self.head:
#                     break
#             print("Element not found")

# cll = Cll()
# cll.insert_first("a")
# cll.insert_first("b")
# cll.insert_first("v")
# cll.insert_first("d")
# cll.insert_first("f")
# cll.insert_last("7")
# print(cll.tail)
# print(cll.head)
# cll.display()
# cll.search("v")