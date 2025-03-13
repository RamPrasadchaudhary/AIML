name=input("Enter name")
age=int (input("Age"))
flag="False"
if age >=18:
    flag="True"
else:
    flag="False"
counter=0
for  i in name:
    if (i=="a"):
        counter+=1
if (flag=="True"):
    if(counter>=2):
        print("YOu are lucky")
    else:
        print("You are not lucky")                    
