
#TEXT REVERSAL  PROGRAM

print("TEXT REVERSAL \n")

n=str(input("Enter the Text: "))

stack=[]
r_stack=[]


def listToStr(r_stack): 
    
    string = "" 
       
    for ele in r_stack: 
        string += ele  
    return string


for i in n:
    stack.append(i)
    

for i in range(len(stack)):
    r_stack.append(stack.pop(-1))


print("\nReverse Text: ",listToStr(r_stack))    
                   