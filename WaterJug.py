'''A Water Jug Problem: You are given two jugs, a 4-litre one and a 3-litre one, a pump which has unlimited water which you can use to fill the jug, and the ground on which water may be poured. Neither jug has any measuring markings on it. How can you get exactly 2 litre of water in the 4-gallon jug? 
'''

print("A is a 4 Gallons jug")
print("B is a 3 Gallons jug")
A=[]
B=[]
print("\n")
print("CONDITIONS:")
print("There are no markings on the jug A and jug B")
print("Atlast we need to have 2 Gallons of water in jug A")
print("\n")
for i in range(9):
    a=int(input("Amount of Water you want to remove from A:"))
    a0=int(input("Amount of water you want to add to A:"))
    b=int(input("Amount of water you want to remove to B:"))
    b0=int(input("Amount of water you want to add to B:"))
    if(i==1):
        A.append(a0)#[4][0]
        print("\n")
        print("In jug-A we are having",A,"gallons of water","\n","In jug-B we are having",B,"gallons of water")
        print("\n")
    if(i==2):
        B.append(A[0]-a)#[4][3]
        A.pop(0)#[0][3]
        A.append(a)#[1][3]
        print("In jug-A we are having",A,"gallons of water","\n","In jug-B we are having",B,"gallons of water")
        print("\n")
    if(i==3):
        B.pop(0)#[1][0]
        print("In jug-A we are having",A,"gallons of water","\n","In jug-B we are having",B,"gallons of water")
        print("\n")
    if(i==4):
        B.append(A[0])#[1][1]
        A.pop(0)#[0][1]
        print("In jug-A we are having",A,"gallons of water","\n","In jug-B we are having",B,"gallons of water")
        print("\n")
    if(i==5):
        A.append(a0)#[4][1]
        print("In jug-A we are having",A,"gallons of water","\n","In jug-B we are having",B,"gallons of water")
        print("\n")
    if(i==6):
        B.append(B[0]+A[0]-a)#[4][1,3]
        A.append(A[0]-2)#[4,2][1,3]
        B.pop(0)#[4,2][3]
        A.pop(0)#[2][3]
        print("In jug-A we are having",A,"gallons of water","\n","In jug-B we are having",B,"gallons of water")
        print("\n")
    if(i==7):
        B.pop(0)#[2][0]
        print("In jug-A we are having",A,"gallons of water","\n","In jug-B we are having",B,"gallons of water")
        print("\n")
        
    '''A Water Jug Problem: You are given two jugs, a 8-litre one and a 6-litre one, a pump which has unlimited water which you can use to fill the jug, and the ground on which water may be poured. Neither jug has any measuring markings on it. How can you get exactly 4 litre of water in the 8-gallon jug? 
 '''  
print("A is a 8 Gallons jug")
print("B is a 6 Gallons jug")
A=[]
B=[]
print("\n")
print("CONDITIONS:")
print("There are no markings on the jug A and jug B")
print("Atlast we need to have 4 Gallons of water in jug A")
print("\n")
for i in range(9):
    a=int(input("Amount of Water you want to remove from A:"))
    a0=int(input("Amount of water you want to add to A:"))
    b=int(input("Amount of water you want to remove to B:"))
    b0=int(input("Amount of water you want to add to B:"))
    if(i==1):
        A.append(a0)
        print("\n")
        print("In jug-A we are having",A,"gallons of water","\n","In jug-B we are having",B,"gallons of water")
        print("\n")
    if(i==2):
        B.append(A[0]-a)
        A.pop(0)
        A.append(a)
        print("In jug-A we are having",A,"gallons of water","\n","In jug-B we are having",B,"gallons of water")
        print("\n")
    if(i==3):
        B.pop(0)
        print("In jug-A we are having",A,"gallons of water","\n","In jug-B we are having",B,"gallons of water")
        print("\n")
    if(i==4):
        B.append(A[0])
        A.pop(0)
        print("In jug-A we are having",A,"gallons of water","\n","In jug-B we are having",B,"gallons of water")
        print("\n")
    if(i==5):
        A.append(a0)
        print("In jug-A we are having",A,"gallons of water","\n","In jug-B we are having",B,"gallons of water")
        print("\n")
    if(i==6):
        B.append(B[0]+A[0]-a)
        A.append(A[0]-a)
        B.pop(0)
        A.pop(0)
        print("In jug-A we are having",A,"gallons of water","\n","In jug-B we are having",B,"gallons of water")
        print("\n")
    if(i==7):
        B.pop(0)
        print("In jug-A we are having",A,"gallons of water","\n","In jug-B we are having",B,"gallons of water")
        print("\n")

        
        
        
    


        
        
        
    
