import matplotlib.pyplot as plt
from math import ceil,floor,sin,cos,atan,sqrt

plt.figure(dpi=1200,figsize=(5,1))
# Constructs the matplotlib figure as a high definition, square plot
plt.axis('off') # Disables axis plots on image
plt.axis('equal')


tau = (1 + sqrt(5))/2 # Golden ratio


gradient = (1/tau) # Gradient of shaded region in green
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


def isWithinRegion(x,y):
    if y > minAccepted(x) and y < maxAccepted(x):
        return True
    

yMax = ceil(maxAccepted(regionWidth))
yMin = floor(minAccepted(0))


x_accepted, y_accepted = [ ], [ ]


for x in range(regionWidth):
    for y in range(yMin,yMax):
        if isWithinRegion(x,y):
            x_accepted = x_accepted + [x]
            y_accepted = y_accepted + [y]
            
for i in range(len(x_accepted)):
    x_final = (x_accepted[i]+y_accepted[i]*gradient)/(1+gradient**2)
    plt.plot(x_final, 0, 'ko', markersize=4 )
