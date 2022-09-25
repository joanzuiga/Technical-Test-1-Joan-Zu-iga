from cgi import print_environ



# array to validate
strArr = ["baseball", "a,all,b,ball,bas,base,cat,code,d,e,quit,z"]

def WordSplit(strArr):

    response = "the string not possible"

    word = strArr[0]
    #an auxiliary word so as not to divide the original word
    wordDivided=word
    dictionary = strArr[1]

    cont = (len(word))

    #array of dictionary words
    cadena = dictionary.split(",")


    for z in range(cont):
        first = wordDivided[0:z]
        second = wordDivided[z:cont]
        if(cadena.__contains__(first) and cadena.__contains__(second) and len(first)>1):
            response=first+","+second  
                
    return response

print(WordSplit(strArr))
