def intersection(arrays):
    #[1,2,3],
    #[1,4,5],
    #[1,6,7]
    
    count = {}  #store the elements of all arrays
    list=[]     #will serve as container to hold the repeated
    length = 0  #number of arrays in input
    
    for a in arrays:   #outer loop, iterate through array
        length += 1    #for each array I go through count to length
        for b in a:    #inner loop ,iterate through elem in each arr
            if b not in count:  #if that elem is not in cache
                count[b] = 1    #added it
            else:
                count[b] += 1   #else, increment it by one

    for key in count:           #for each key in count
        if count[key] >= length:#if the value of the key is greater then the number of arrays given
             list.append(key)    #append to the result list

    return list

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(10, 20)) + [1, 2, 3])
    arrays.append(list(range(2, 3)) + [1, 2, 3])
    arrays.append(list(range(3, 40)) + [1, 2, 3])

    print(intersection(arrays))
