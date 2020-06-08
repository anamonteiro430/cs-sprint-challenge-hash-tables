#a is a list of numbers both positive and negative
#assuming there are no repeated numbers(like in test and ex.)
#make each number in list be positive using abs()
#count them in cache
#those who have a count of 2 append to result list

def has_negatives(a):
    count={}
    result=[]
    a = [abs(i) for i in a]
    
    for i in a:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    for key in count:
        if count[key] == 2:
            result.append(key)
    return result


        

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
