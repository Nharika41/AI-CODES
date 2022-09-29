# AI-CODES
#These are the AI Lab experiments
'''Vacuum cleaner problem is a well-known search problem for an agent which works on Artificial Intelligence. In this problem, our vacuum cleaner is our agent. It is a goal based agent, and the goal of this agent, which is the vacuum cleaner, is to clean up the whole area. So, in the classical vacuum cleaner problem, we have two rooms and one vacuum cleaner. There is dirt in both the rooms and it is to be cleaned. The vacuum cleaner is present in any one of these rooms. So, we have to reach a state in which both the rooms are clean and are dust free. So, there are eight possible states possible in our vacuum cleaner problem. These can be well illustrated with the help of the following diagrams:

Here, states 1 and 2 are our initial states and state 7 and state 8 are our final states (goal states). This means that, initially, both the rooms are full of dirt and the vacuum cleaner can reside in any room. And to reach the final goal state, both the rooms should be clean and the vacuum cleaner again can reside in any of the two rooms. The vacuum cleaner can perform the following functions: move left, move right, move forward, move backward and to suck dust. But as there are only two rooms in our problem, the vacuum cleaner performs only the following functions here: move left, move right and suck. Here the performance of our agent (vacuum cleaner) depends upon many factors such as time taken in cleaning, the path followed in cleaning, the number of moves the agent takes in total, etc. But we consider two main factors for estimating the performance of the agent. They are:

Search Cost: How long the agent takes to come up with the solution.
Path cost: How expensive each action in the solution are. By considering the above factors, the agent can also be classifies as a utility based agent.'''
n=int(input("Enter the number of rooms:")) for i in range(n): a=str(input("Enter where the location is:")) print("The vaccum cleaner is in location-"+a) if(a==a): b=input("Enter d if the location is dirt- Enter c if the location cleaned:") if(b=='d'): print("The location-"+a+" is dirty") print("Suck the dirt") print("The dirt is cleaned") print("Now move to right")

if(b=='c'):
    print("The vaccum cleaner is in location"+a)
    print("The location "+a+ " is cleaned")
    print("Move to left")

else:
  print("The location is cleaned")
else: print("Give the correct location")

''' Output:

Test cases: Enter Location of Vacuum A Enter status of a0 Enter status of other room0 Initial Location Condition{'A': '0', 'B': '0'} Vacuum is placed in location B 0 Location B is already clean. No action 0 Location A is already clean. GOAL STATE: {'A': '0', 'B': '0'} Performance Measurement: 0

Result: The Vacuum cleaner agent has been successfully implemented. '''
