# list comprehension

l=[1,2,34,5,6,2,8,2,9,80]

l2=[i for i in l]
print(l2)


l2=[i*4 for i in l]
print(l2)

l3 = [i for i in l if i%2==0]
print(l3)

l3 = [i for i in l if i>10 and i<=70]
print(l3)



'''

1. Take 5 number from user and add into list.
2. Take one list from user and print sum of all element.
3. Take one list from user and reverse that string and store that list in another list.
4. Take one list from user and find all even numbers into list.
5. Take two list from user and merge that two list into another list.

    l1 = [1,2,3,5]
    l2 =[6,2,3,4,5]
    l3 =[1,2,3,5,6,2,3,4,5]
6. Take one list from user and return list like this:

    l = [2,3,4,5]
    o/p: [4,9,16,25]

7. Take one list from user and print only lower case string element.

    list = ['java' , 'Python', 'JAVA','kiwi']

8. Take one list from user and after that take range from user and delete all elements that contains in list from range.

    l= [1,2,3,5,1,5,45,7,85,8,9,6,4,7,8,]
    start:3
    end:9

    o/p: [1,2,1,45,85]
    
9. Take one list from user and remove all duplicate elements.

    l = [ 1,2,3,4,1,5,6,2,4]
    o/p: [1,2,3,4,5,6]

10. print list in reverse ordered.

11. print sum of digit in list.

    l = [12345,234,675,123,67]

    o/p:[15,9,18,6,13]

12. find cumulative sum.

    l = [1,3,4,5,6,7]
    o/p: [1,4,8,13,19,26]

13. Take one list from user and interchange first and last element.

    l = [1,3,4,5,6,7]
    o/p:[7,3,4,5,6,1]

14. Take one list from user and after that take one element from user and check that element is present in list or not.

    l = [1,3,4,5,6,7]

    ele: 3 -> Found at index 1
    ele: 2 -> Not Found

15. Input comma separated string convert into list and after that print sum of all element.

string - 1,2,4,5,6

l = [1,2,4,5,6]
sum: 18





'''


