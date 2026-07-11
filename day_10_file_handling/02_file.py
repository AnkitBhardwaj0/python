def count(str1):
    dic={
        'a':0,
        'e':0,
        'i':0,
        'o':0,
        'u':0
    }
    for line in str1:
        for ch in line:
            ch=ch.lower()
            if ch in dic:
                dic[ch] += 1
    print(dic)

f=open("day_10_file_handling/f2.txt",'r')
str1=f.readlines()
count(str1)
f.close()


    



