
#Thomas Gallagher
#09/03/2022
#Conventional Magnets for Accelerators
#Question 4

###############################################################################

import numpy as np
import matplotlib.pyplot as plt

###############################################################################

def CombinedFunc(x, B0, Bgrad, h):
    
    y = (B0*h)/(B0+(Bgrad*x))
    
    return y

figRes = 1001

B0 = 1.2 #T
Bgrad = 4.1 #T/m
h = 0.01 #m
magWidth = 0.025 #m
magCentre = B0/Bgrad
print('The centre of the magnet is ',magCentre,' mm')
magLeft = magCentre - (magWidth/2)
print('The left edge of the vaccum chamber is at position ',magLeft,' m')
magRight = magCentre + (magWidth/2)
print('The left edge of the vaccum chamber is at position ',magRight,' m')
magLeftOverhang = magLeft+0.035
magRightOverhang = magRight-0.035

xvals = np.linspace(-0.29,0.58,figRes)
yvals = np.zeros(len(xvals))

xvalsPOLE = np.linspace(magLeft,magRight,figRes)
yvalsPOLE = np.zeros(len(xvalsPOLE))

xvalsPOLEoverhang = np.linspace(magLeftOverhang,magRightOverhang,figRes)
yvalsPOLEoverhang = np.zeros(len(xvalsPOLEoverhang))

for i in range (figRes):
    
    yvals[i]=CombinedFunc(xvals[i], B0, Bgrad, h)
    yvalsPOLE[i]=CombinedFunc(xvalsPOLE[i], B0, Bgrad, h)
    yvalsPOLEoverhang[i]=CombinedFunc(xvalsPOLEoverhang[i], B0, Bgrad, h)

magLeftX = np.full(101, magLeft)
magRightX = np.full(101, magRight)
magCentreX = np.full(101, magCentre)
magYvals = np.linspace(0.0046,0.0054,101)

mm = 1E3

plt.clf()
plt.plot(xvals*mm, yvals*mm, 'g')
plt.grid()
plt.title('Hyperbolic Combined-Function Plot', fontsize = 10)
plt.xlabel(r'$x$ $(mm)$')
plt.ylabel(r'$y$ $(mm)$')
plt.savefig('Fig1.png', dpi=300, bbox_inches = "tight")
plt.show()

plt.clf()
plt.plot(xvalsPOLE*mm, yvalsPOLE*mm, 'g')
plt.grid()
plt.title('Hyperbolic Combined-Function Plot for the Pole Face Region in the Bounds of the Vaccum Chamber', fontsize = 8)
plt.xlabel(r'$x$ $(mm)$')
plt.ylabel(r'$y$ $(mm)$')
plt.savefig('Fig2.png', dpi=300, bbox_inches = "tight")
plt.show()

plt.clf()
plt.plot(xvalsPOLEoverhang*mm, yvalsPOLEoverhang*mm, 'g', label = 'Pole Contour')
plt.plot(magLeftX*mm, magYvals*mm, 'r', linestyle = 'dotted', label='Vaccum Chamber Edge')
plt.plot(magRightX*mm, magYvals*mm, 'r', linestyle = 'dotted', label = 'Vaccum Chamber Edge')
plt.plot(magCentreX*mm, magYvals*mm, 'k', linestyle = 'dotted', label = 'Magnet Centre')
plt.grid()
plt.title('Hyperbolic Combined-Function Plot for the Pole Face Region in the Bounds of the Vaccum Chamber', fontsize = 8)
plt.xlabel(r'$x$ $(mm)$')
plt.ylabel(r'$y$ $(mm)$')
plt.legend(prop={'size': 8})
plt.savefig('Fig3.png', dpi=300, bbox_inches = "tight")
plt.show()


