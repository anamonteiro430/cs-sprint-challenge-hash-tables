#UPER
#I'm given a list of item's weights, the length of the list and the limit
#I want to check if the sum of any 2 item's weight is equal to the limit number.

#create hash table 
#store as keys the weights of the items if it's not already there


def get_indices_of_item_weights(weights, length, limit):  #O(n) n being the number of items in weights list
    cache={}  #hold the weights as keys and the indexes in the list of weights as values
    #because values are going to be needed to return
    list = []   #structure to hold the two numbers that summed are equal to the limit that we'll find later

    #Special Case - if there one or less element in weights return None because we can't sum it
    if len(weights) <= 1:
        return None

    #Special Case - only two weights
    if len(weights) == 2:
        if (weights[0] + weights[1]) == limit:  #if their sum is equal to the limit
            return (1,0)  #return a tuple with the highest index as the first element
            

    for index in range(length): #iterate through the list of weights
        if weights[index] not in cache: #if the element in the index is not on the cache map
            cache[weights[index]] = index  #put it in there
    
    for key in cache: #then iterate through the keys in the cache
        result = limit - key #the result that I want to know would be the other number that when added to this key is equal to the limit
        if result in cache:  #if the result(other number is in cache)
            list.append(cache.get(result))  #append is to my list
        
    return tuple(list)   #convert list to tuple
