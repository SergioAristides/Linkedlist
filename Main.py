from node import Linkedlist


if __name__ == '__main__':
    myList=Linkedlist()
    myList.append(1)
    myList.append(2)
    myList.append(6)
    myList.remove_position(2)
    myList.append(55)
    myList.append_first(23)
    myList.append_first(16)
    myList.append_first(5)
    myList.remove_begin()
    myList.insert_position(5,2)
    myList.remove_end()
    myList.append(31)
    myList.append(12)
    myList.remove_value(1)
    print(myList)
    myList.reverse()
    print(myList)

    
    
    #myList.remove(10)
    #print(myList)
    