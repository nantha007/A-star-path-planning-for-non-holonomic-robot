import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

def plot(ax):
#     plt.hold()
#     plt.axis([0, 11.1, 0, 10.1])
#     plt.hold()
    # circle 1
    circle1 = plt.Circle((3.9, 9.65), 0.405, color='g', clip_on=False)
    # circle 2
    circle3 = plt.Circle((4.38, 7.36), 0.405, color='g', clip_on=False)
    # rect 4
    ax.add_patch(Rectangle((4.38,3.15), 0.91, 1.83,color='g',alpha=1))
    # circle 5
    circle5 = plt.Circle((4.38, 2.74), 0.405, color='g', clip_on=False)
    # rect 5
    ax.add_patch(Rectangle((5.29,2.65), 1.83, 0.76, color='g',alpha=1))
    # rect 6
    ax.add_patch(Rectangle((4.74,0.35), 2.74, 1.52, color='g',alpha=1))
    # table 1
    circle21 = plt.Circle((3.1,8.3), 0.7995, color='g', clip_on=False)
    circle22 = plt.Circle((1.5,8.3), 0.7995, color='g', clip_on=False)
    ax.add_patch(Rectangle((1.5, 7.501), 1.5978, 1.599, color='g',alpha=1))

    # circle 7
    circle7 = plt.Circle((3.9,0.45), 0.405, color='g', clip_on=False)

    # rect 9
    ax.add_patch(Rectangle((8.32, 8.3), 0.86,1.83, color='g',alpha=1))
    # rect 10
    ax.add_patch(Rectangle((10.26, 9.19), 0.84,0.91, color='g',alpha=1))
    # rect 11
    ax.add_patch(Rectangle((7.44, 6.21), 3.66,0.76, color='g',alpha=1))
    # rect 12
    ax.add_patch(Rectangle((10.19, 3.625), 0.91,0.86, color='g',alpha=1))
    # rect 13
    ax.add_patch(Rectangle((10.52, 4.485), 0.58,1.17, color='g',alpha=1))
    # rect 14
    ax.add_patch(Rectangle((10.52, 1.7825), 0.84,1.17, color='g',alpha=1))
    # rect 15
    ax.add_patch(Rectangle((9.27, 0.35), 1.83, 0.76, color='g',alpha=1))
    # rect 16
    ax.add_patch(Rectangle((7.79, 0.35), 1.17, 0.58, color='g',alpha=1))
    # rect 17
    ax.add_patch(Rectangle((7.84, 2.67), 1.52, 1.17, color='g',alpha=1))

#     plt.hold()
    ax.add_artist(circle1)
    ax.add_artist(circle3)
    ax.add_artist(circle5)
    ax.add_artist(circle21)
    ax.add_artist(circle22)
    ax.add_artist(circle7)

    # plt.show()
    return ax

def isInsideCircle(x,y,x_center,y_center, radius):
    rad = 0.230/2
    cl = 0.2
    return (( ((x-x_center)**2+(y-y_center)**2) - (radius+cl+rad)**2 ) < 0)

def isInsideRect(x,y,x_min, y_min, x_max, y_max):
    cl = 0.2
    rad = 0.230/2
    return (x>x_min-cl-rad and x<x_max+cl+rad and y>y_min-cl-rad and y<y_max+cl+rad)

def obstacleCheck(x, y):
    cl = 0.2
    rad = 0.230/2
    dist = cl + rad
    # circle 1
    circle1 = isInsideCircle(x,y,3.9,9.65,0.405)
    # print('1',circle1)
    # table 2
    circle21 = isInsideCircle(x,y,3.1,8.3,0.7995)
    # print('2',circle21)
    circle22 = isInsideCircle(x,y,1.5,8.3,.7995)
    # print('3',circle22)
    rect2 = isInsideRect(x,y,1.5,7.501,3.1,9.1)
    # print('4', rect2)
    # circle 3
    circle3 = isInsideCircle(x,y,4.38,7.36,0.405)
    # print('5',circle3)
    # rect 4
    rect4 = isInsideRect(x,y,4.38,3.15,5.29,4.98)
    # print('6',rect4)
    # circle 5
    circle5 = isInsideCircle(x,y,4.38,2.74,0.405)
    # print('7',circle5)
    # rect 5
    rect5 = isInsideRect(x,y,5.29,2.65,3.41,7.12)
    # print('8', rect5)
    # rect 6
    rect6 = isInsideRect(x,y,4.74,0.35,7.48,1.87)
    # print('9', rect6)
    # circle 7
    circle7 = isInsideCircle(x,y,3.9,0.45,0.405)
    # print('10',circle7)
    # rect 9
    rect9 = isInsideRect(x,y,8.32,8.3,9.18,10.1)
    # print('11', rect9)
    # rect 10
    rect10 = isInsideRect(x,y,10.26,9.19,11.1,10.1)
    # print('12', rect10)
    #rect 11
    rect11 = isInsideRect(x,y,7.44,6.21,11.1,6.97)
    # print('13', rect11)
    # rect 12
    rect12 = isInsideRect(x,y,10.19,3.625,11.1,4.485)
    # print('rect12', rect12)
    # rect 13
    rect13 = isInsideRect(x,y,10.52,4.485,11.1,5.655)
    # print('14',rect13)
    # rect 14
    rect14 = isInsideRect(x,y,10.52,1.7825,11.1,2.9525)
    # print('15',rect14)
    #rect 15
    rect15 = isInsideRect(x,y,9.27,0.35,11.1,1.11)
    # print('16', rect15)
    # rect 16
    rect16 = isInsideRect(x,y,7.79,0.35,8.96,0.93)
    # print('17',rect16)
    # rect 17
    rect17 = isInsideRect(x,y,7.84,2.67,9.015,3.84)
    # print('18', rect17)
    # is outside
    outside = not (x> dist and y> dist and x< 10.1 - dist and y<11.1 - dist )

    isObs = (circle1 or circle3 or circle5 or circle7 or circle21 or circle22 or \
        rect2 or rect4 or rect5 or rect6 or rect9 or rect10 or rect11 or rect12 or\
        rect13 or rect14 or rect15 or rect15 or rect16 or rect17 or outside)

    return isObs

if __name__ == '__main__':
    #fig, ax = plt.subplots()
    #ax = plot(ax)
    # ax.plot()
#    plt.hold()
#     plt.plot(6,6,'bo')
#     plt.show()
    print(obstacleCheck(8,8))
