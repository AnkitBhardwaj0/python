"""
Create line wise reverse of a file
Write a function which takes two arguments: the names of the input file (to be read from) and the output file (which will be created).
"""
file1="day_10_file_handling/q_04.txt"
file2="day_10_file_handling/s_04.txt"
with open(file1,'w') as f:
    text="""
Python is one of the most popular programming languages.
Practice every day to improve your coding skills.
Reading files is an important part of Python programming.
Lists, dictionaries, and tuples are basic data structures.
Exception handling makes programs more reliable.
JSON files are human-readable and easy to share.
Pickle stores Python objects in binary format.
Functions help organize code into reusable blocks.
Debugging is an essential skill for every programmer.
Consistency is more important than studying for long hours.
"""
    f.write(text)

def reverse(f1,f2):
    rev_text=[]
    with open (f1,'r')as f:
        for line in f:
            line = line.rstrip("\n")
            line = line[::-1]
            line += "\n"
            rev_text.append(line)
    with open (f2,'w')as f:
        reverse_text = "".join(rev_text)
        f.write(reverse_text)
    with open (f2,'r')as f:
        print(f.read())
reverse(file1,file2)