import os
print(" !!! \n Please Note if you want to \n Start file number frome Speci number so \n so please Enter number Carefully \n !!!!")
print("\n\n")
name1 = input("Enter File Name : ")
file1 = int(input("Enter File Quntity: "))
k = int(input("Enter Number File Sart From : "))
# This is for extenion
extention1 = input("Ender Extention")

for i in range(file1):

    os.system(f"echo > {name1}{k}{extention1}")
    k += 1
