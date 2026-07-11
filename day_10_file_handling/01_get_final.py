f=open("day_10_file_handling/get_final_line.txt",'r')
while True:
    line=f.readline()
    if line=="":
        break
    lastline=line
print(lastline)
f.close()