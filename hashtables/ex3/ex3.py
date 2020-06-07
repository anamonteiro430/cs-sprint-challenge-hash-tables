def intersection(arrays):
    #[1,2,3],
    #[1,4,5],
    #[1,6,7]
    
    count = {}
    list=[]
    for i in arrays[0]:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
    
    for i in arrays[1]:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
        
    print(count)

    for key in count:
        if count[key] >= 2:
             list.append(key)    

    return list

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(10, 20)) + [1, 2, 3])
    arrays.append(list(range(2, 3)) + [1, 2, 3])
    arrays.append(list(range(3, 40)) + [1, 2, 3])

    print(intersection(arrays))
