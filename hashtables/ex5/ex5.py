# Your code here



def finder(files, queries):
    paths = {}
    result=[]
    for file in files:
        paths[file] = 0
    
    for key in paths:
        for q in queries:
            if q in key:
                result.append(key)
                

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
