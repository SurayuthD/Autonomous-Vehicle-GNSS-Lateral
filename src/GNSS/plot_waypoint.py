import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#...................................................................Curve 1.........................................................................#

x1=  [661473.31,     661478.44,     661483.47,      661487.12,      661489.88]      #661489.88,      661489.88         
y1=  [1509700.25,    1509700.25,    1509699.74,     1509697.06,     1509688.065]    #1509583.749,    1509522.50         

x2=  [661473.31,     661478.35,  661482.28,  661484.90,  661486.81]      #661486.945,     661487.67                 
y2=  [1509698.39,    1509698.39, 1509697.56, 1509695.23, 1509688.065]    #1509583.749,    1509522.50                 

x3=  [661473.31,     661478.35,  661480.90,  661482.46,  661484.17]      #661484.17,      661484.17                 
y3=  [1509696.56,    1509696.56, 1509695.50, 1509693.59, 1509688.065]    #1509583.749,    1509522.50 

#...................................................................Curve 2.........................................................................#

x4= [661376.99,     661377.31,      661385.10,      661395.11,      661403.27,      661417.88,      661433.35]
y4= [1509653.56,    1509667.16,     1509679.03,     1509689.91,     1509696.00,     1509701.28,     1509703.9]

x5= [661379.26,     661380.71,      661386.43,      661396.73,      661405.27,      661418.32,      661433.35]
y5= [1509653.56,    1509665.727,    1509676.19,     1509688.05,     1509694.04,     1509698.81,     1509700.99]

x6= [661382.42,     661384.11,      661387.89,      661398.362,      661407.30,      661418.53,      661433.35]
y6= [1509653.56,    1509664.41,     1509672.70,     1509685.75,     1509691.86,     1509696.31,     1509698.11]

#...................................................................Curve 3.........................................................................#

x7= [661376.99,     661378.29,      661381.376,     661392.48,      661405.57,      661416.61,      661423.02,      661430.17,      661436.79]
y7= [1509560.13,    1509549.73,     1509537.60,     1509525.89,     1509515.60,     1509510.45,     1509507.83,     1509506.53,     1509506.78]

x8= [661379.84,     661380.82,      661383.736,     661394.25,      661407.30,      661417.61,      661423.72,      661430.28,      661436.79]
y8= [1509560.13,    1509550.53,     1509540.62,     1509528.60,     1509518.09,     1509512.45,     1509510.08,     1509508.93,     1509509.04]

x9= [661382.42,     661383.356,     661386.00,      661396.00,      661408.78,      661418.68,      661424.49,      661430.37,      661436.79]
y9= [1509560.13,    1509551.340,    1509543.17,     1509531.21,     1509519.95,     1509514.66,     1509512.5,      1509511.22,     1509511.65]

#...................................................................Curve 4.........................................................................#

x10= [661466.07,    661472.01,      661477.68,      661481.07,      661482.94,      661484.3,      661484.17]
y10= [1509511.90,   1509512.44,     1509513.18,     1509514.50,     1509515.67,     1509517.50,     1509522.5]

x11= [661466.07,    661472.01,      661478.05,      661482.31,      661484.94,      661486.86,      661487.10]
y11= [1509509.82,   1509510.22,     1509510.94,     1509512.36,     1509513.8,      1509517.50,     1509522.5]

x12= [661466.07,    661472.01,      661478.40,      661483.45,      661487.10,      661489.37,      661489.88]
y12= [1509507.78,   1509508.27,     1509508.79,     1509510.07,     1509512.09,      1509517.5,      1509522.5]


#...................................................................Linear SN.........................................................................#

x13= [661484.17,    661484.17,      661484.17]#,      661478.35,      661473.31]
y13= [1509522.50,   1509583.749,    1509688.065]#,    1509696.56,     1509696.56]

x14= [661487.12,    661486.945,     661486.81]#,      661478.35,      661473.31]
y14= [1509522.50,   1509583.749,    1509688.065]#,    1509698.39,     1509698.39]

x15= [661489.88,    661489.88,      661489.88]#,      661478.44,      661473.31]
y15= [1509522.50,   1509583.749,    1509688.065]#,    1509700.25,     1509700.25]

#...................................................................Linear EW.........................................................................#

# x16= [661433.35,      661478.44]
# y16= [1509703.9,      1509700.25]

# x17= [661433.35,      661473.31]
# y17= [1509701.39,     1509698.39]

# x18= [661433.35,      661473.31]
# y18= [1509699.09,     1509696.56]

x16= [661433.35,      661473.31]
y16= [1509703.9,      1509703.25]

x17= [661433.35,      661473.31]
y17= [1509701.39,     1509700.39]

x18= [661433.35,      661473.31]
y18= [1509699.09,     1509698.56]


#...................................................................Linear NS.........................................................................#

x19= [661382.42,      661382.42]
y19= [1509653.56,     1509560.13]

x20= [661379.26,      661379.26]
y20= [1509653.56,     1509560.13]

x21= [661376.99,      661376.99]
y21= [1509653.56,     1509560.13]

#...................................................................Linear WE.........................................................................#

x22= [661436.79,      661466.07]
y22= [1509511.65,     1509511.70]

x23= [661436.79,      661466.07]
y23= [1509509.44,     1509509.82]

x24= [661436.79,      661466.07]
y24= [1509507.42,     1509507.78]

#-----------------------------------------------------------------------------------------------------------------------------------------------------#
# fig1 = plt.figure()
# fig2 = plt.figure()
# fig3 = plt.figure()
# fig4 = plt.figure()
# fig5 = plt.figure()
fig6 = plt.figure()
# fig7 = plt.figure()
# fig8 = plt.figure()

# ax = fig1.gca()
# bx = fig2.gca()
# cx = fig3.gca()
# dx = fig4.gca()
# ex = fig5.gca()
fx = fig6.gca()
# gx = fig7.gca()
# hx = fig8.gca()

# ax.plot(x1,y1,'-ro')
# ax.plot(x2,y2,'-ko')
# ax.plot(x3,y3,'-ro')
# ax.set_title('Reference Path: Curve 1')

# bx.plot(x4,y4,'-ro')
# bx.plot(x5,y5,'-ko')
# bx.plot(x6,y6,'-ro')
# bx.set_title('Reference Path: Curve 2')
# bx.grid(linestyle = "dashed")

# cx.plot(x7,y7,'-ro')
# cx.plot(x8,y8,'-ko')
# cx.plot(x9,y9,'-ro')
# cx.set_title('Reference Path: Curve 3')
# # cx.grid(linestyle = "dashed")

# dx.plot(x10,y10,'-ro')
# dx.plot(x11,y11,'-ko')
# dx.plot(x12,y12,'-ro')
# dx.set_title('Reference Path: Curve 4')
# # dx.grid(linestyle = "dashed")

# ex.plot(x13,y13,'-ro')
# ex.plot(x14,y14,'-ko')
# ex.plot(x15,y15,'-ro')
# ex.set_title('Reference Path: Linear South to North')
# # ex.grid(linestyle = "dashed")

fx.plot(x16,y16,'-ro')
fx.plot(x17,y17,'-ko')
fx.plot(x18,y18,'-ro')
fx.set_title('Reference Path: Linear East to West')
# fx.grid(linestyle = "dashed")

# gx.plot(x19,y19,'-ro')
# gx.plot(x20,y20,'-ko')
# gx.plot(x21,y21,'-ro')
# gx.set_title('Reference Path: Linear North to South')
# # gx.grid(linestyle = "dashed")

# hx.plot(x22,y22,'-ro')
# hx.plot(x23,y23,'-ko')
# hx.plot(x24,y24,'-ro')
# hx.set_title('Reference Path: Linear West to East')
# hx.grid(linestyle = "dashed")

# plt.legend()
plt.show() 