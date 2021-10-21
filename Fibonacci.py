

from numpy import sqrt, isclose
import matplotlib.pyplot as plt

tau = (1 + sqrt(5))/2 # Golden ratio
W = 1
edgeList = [0, W]
long = W
short = long/tau

N = 4 # Change generation here
# Handles how many times the original will be dissected L -> LS
for x in range(0,N):
    pending=[]
    for i in range(0,len(edgeList)-1):
        # For all values of edgeList except final:
            if isclose(edgeList[i+1]-edgeList[i], long):
            # If the difference between one value and the next is
            # approx. equal to the current value of 'long':
                pending.append(edgeList[i]+short)
                # Adds new value inbetween according to L -> LS rule

    edgeList.extend(pending)
    edgeList.sort()
    # Sorts values of edgeList into size order (since above for loop returns
    # disorded edgeList)
    long = long/tau
    # Reduce the 'long' variable by golden ratio for the next generation
    short = short/tau
    # Reduce the 'short' variable by golden ratio for the next generation
    
    
# 1D
plt.figure(dpi=1200,figsize=(5,1))
plt.axis('off')
plt.axis('equal')

for i in range(0,len(edgeList)-1):
    if isclose(edgeList[i+1]-edgeList[i], long):
    # If the difference between one value and the next is
    # approx. equal to the current value of 'long':
        plt.plot( [edgeList[i], edgeList[i+1]] , [0,0], 'b', linewidth=2 )
        # Plots blue line between points
    if isclose(edgeList[i+1]-edgeList[i], short):
    # If the difference between one value and the next is
    # approx. equal to the current value of 'short':
        plt.plot( [edgeList[i], edgeList[i+1]] , [0,0], 'r', linewidth=2 )
        # Plots red line between points
    plt.plot( edgeList[i], 0 , 'ko', markersize=3 )
    plt.plot( edgeList[i+1], 0 , 'ko', markersize=3 )


# 2D
plt.figure(dpi=1200,figsize=(5,5))
plt.axis('off')
plt.axis('equal')

for i in range(0,len(edgeList)):
    plt.plot( [ edgeList[i], edgeList[i] ],
             [ edgeList[0], edgeList[-1] ], 'k', linewidth=1 )
    plt.plot( [ edgeList[0], edgeList[-1] ],
             [ edgeList[i], edgeList[i] ], 'k', linewidth=1 )


# 3D
fig3d = plt.figure(dpi=600)
ax = fig3d.add_subplot(111, projection='3d')
ax.set_axis_off()

for i in range( 0, len(edgeList) ):
    for j in range( 0, len(edgeList) ):
        ax.plot( [ edgeList[i], edgeList[i] ],
                [ edgeList[j], edgeList[j] ],
                [ edgeList[0], edgeList[-1] ], 'r', linewidth=1 )
        ax.plot( [ edgeList[j], edgeList[j] ],
                [ edgeList[i], edgeList[i] ],
                [ edgeList[0], edgeList[-1] ], 'r', linewidth=1 )
        ax.plot( [ edgeList[i], edgeList[i] ],
                [ edgeList[0], edgeList[-1] ],
                [ edgeList[j], edgeList[j] ], 'k', linewidth=1 )
        ax.plot( [ edgeList[j], edgeList[j] ],
                [ edgeList[0], edgeList[-1] ],
                [ edgeList[i], edgeList[i] ], 'k', linewidth=1 )
        ax.plot( [ edgeList[0], edgeList[-1] ],
                [ edgeList[i], edgeList[i] ],
                [ edgeList[j], edgeList[j] ], 'b', linewidth=1 )
        ax.plot( [ edgeList[0], edgeList[-1] ],
                [ edgeList[j], edgeList[j] ],
                [ edgeList[i], edgeList[i] ], 'b', linewidth=1 )
