"""Generate the output like: A(5), B(3), C(1) with input like ABBAAACB"""

print("please input the number")
string = input("input your string")
new_string =[]
for i in range(len(string)):
    a=new_string[i]=string[i] + '('+str(i)+'),'

print(new_string)
