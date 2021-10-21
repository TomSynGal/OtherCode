import matplotlib.pyplot as plt
from math import ceil,floor,sin,cos,atan,sqrt


plt.figure(dpi=1200,figsize=(5,1))
# Constructs the matplotlib figure as a high definition, square plot
plt.axis('off') # Disables axis plots on image
plt.axis('equal')


tau = (1 + sqrt(5))/2 # Golden ratio


gradient = (1/tau) # gradient of shaded region in green
theta = atan(gradient) # Angle formed between shaded region and x-axis (in radians)
thickness = ( cos(theta) + sin(theta) )*tau
# Distance between upper limit and lower limit of region
verticalHeight = thickness * sqrt(gradient**2 + 1)
# Distance between two parallel lines inverse
regionWidth = 5 # How many x values are considered


def maxAccepted(x):
    return gradient*x + verticalHeight/2


def minAccepted(x):
    return gradient*x - verticalHeight/2


def isWithinRegion(x,y,z):
    if z > minAccepted(x) and z < maxAccepted(x):
        if z > minAccepted(y) and z < maxAccepted(y):
            return True
        
        
zMax = ceil(maxAccepted(regionWidth))
zMin = floor(minAccepted(0))


x_accepted, y_accepted, z_accepted = [ ], [ ], [ ]
for x in range(regionWidth):
    for y in range(regionWidth):
        for z in range(zMin,zMax):
            if isWithinRegion(x,y,z):
                x_accepted = x_accepted + [x]
                y_accepted = y_accepted + [y]
                z_accepted = z_accepted + [z]
                    

for i in range(len(x_accepted)):
    for j in range(len(y_accepted)):
        x_final = (x_accepted[i]+z_accepted[i]*gradient)/(1+gradient**2)
        y_final = (y_accepted[j]+z_accepted[j]*gradient)/(1+gradient**2)
        plt.plot(x_final, y_final, 'ko', markersize=4 )

