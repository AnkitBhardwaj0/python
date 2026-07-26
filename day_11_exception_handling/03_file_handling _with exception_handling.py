"""
File Handling with Exception handling
Write a program that opens a text file and write data to it as "Hello, Good Morning!!!". Handle exceptions that can be generated during the I/O operations. Do not show the success message on the main exception handling block (write inside the else block).
"""
file_name="day_11_exception_handling/03_f.txt" 
try:
    with open(file_name,'w') as f:
        strings="Hello, Good Morning!!!"
        f.write(strings)
except OSError as e:
    print(e,"\n")
except Exception as e:
    print(e,"/n")

else:
    print(" success")

try:
    with open(file_name,'r') as f:
        strings=f.read()
except FileNotFoundError as e:
    print(e,"\n")
except OSError as e:
    print(e)
except Exception as e:
    print(e,"/n")

else:
    print(strings)
    print(" success")