# AI-CODES
#VACCUM CLEANER AGENT
n=int(input("Enter the number of rooms:"))
for i in range(n):
  a=str(input("Enter where the location is:"))
  print("The vaccum cleaner is in location-"+a)
  if(a==a):
    b=input("Enter d if the location is dirt- Enter c if the location cleaned:")
    if(b=='d'):
      print("The location-"+a+" is dirty")
      print("Suck the dirt")
      print("The dirt is cleaned")
      print("Now move to right")
    
    if(b=='c'):
        print("The vaccum cleaner is in location"+a)
        print("The location "+a+ " is cleaned")
        print("Move to left")

    else:
      print("The location is cleaned")
  else:
    print("Give the correct location")


