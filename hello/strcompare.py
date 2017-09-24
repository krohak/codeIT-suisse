import re

def string_third(str):

    dict_size = 1
    wcount = 0
    w_dictionary = {}
    non_w_dict = {}
    #print (dictionary)
    sum = 0

    s = re.split('[^a-zA-Z]', str)
    delim = re.split("[a-zA-Z]", str)
    delim = list(filter(None, delim))
    merge = [0]*(len(s) + len(delim) )

    print(merge)
    print(delim)
    k=0
    if(str[0].isalpha()):
        print("yes")
        for i in range(len(s)):
            merge[k] = s[i];
            if i < len(delim):
                merge[k+1] = delim[i]
                k+=2
            else:
                k+=1
        print(merge)

    for( i,item in enumerate(merge)):
        if item[0].isaplha()
            if not item in w_dictionary:
                w_dictionary[item] = dict_size
                dict_size+=1
            else:
                if(i+1 < len(merge)):
                    if not item+ merge[i+1] in w_dictionary:

    '''
    for i in range
    for i,word in enumerate(s):
        if not word in w_dictionary:
            w_dictionary[word] = dict_size
            dict_size+=1
        else:
            if( i < len(delim)):
                if(word+delim)


    #print(dictionary)
    result = len(s)*12 + sum + len(delim)*12
    print(result)
    '''
string_third("HOW MUCH WOOD COULD A WOOD CHUCK CHUCK IF A WOOD CHUCK COULD CHUCK WOOD")
