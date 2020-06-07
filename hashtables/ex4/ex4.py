def has_negatives(a):
    count={}
    result=[]
    a = [abs(i) for i in a]
    print(a)
    
    for i in a:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    print(count)

    for key in count:
        if count[key] == 2:
            result.append(key)
    return result


        

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
