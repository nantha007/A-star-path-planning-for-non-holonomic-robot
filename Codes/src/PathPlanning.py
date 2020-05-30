#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy as np
from map import obstacleCheck, plot
import timeit

def ddConstraints( ur, ul, theta, minTime):
    radius = 38.0/1000
    L = .23
    del_x = float((radius/2) *(ul + ur)*np.cos(theta)*minTime)
    del_y = float((radius/2) *(ul + ur)*np.sin(theta)*minTime)
    del_theta = float((radius/L) *(ur - ul)*minTime)
    return [del_x,del_y,del_theta, ur,ul]

def findNeighbour(motionModel, step, minTime,x,y,theta):
    neighbours = []
    neighbourTheta = theta
    for i in motionModel:
        obsflag = False
        for t in np.arange(step,minTime,step):
            point = ddConstraints(i[0], i[1], neighbourTheta, t)
            neighbourX = x + point[0]
            neighbourY = y + point[1]
            neighbourTheta = theta + point[2]
            if obstacleCheck(neighbourX,neighbourY):
                obsflag = True
                break
        if not obsflag:
            neighbours.append([round(neighbourX,2), round(neighbourY,2), round(neighbourTheta,2),
            round(point[3],2),round(point[4],2)])
    return neighbours

def a_star(start, goal):
    fig, ax = plt.subplots()
    ax = plot(ax)

    RPM2 = 100*2*3.14/60
    RPM1 = 50*2*3.14/60
    motionModel = [[0,RPM1],[RPM1,0],[RPM1,RPM1],[0,RPM2],[RPM2,0],[RPM2,RPM2],[RPM1,RPM2],[RPM2,RPM1]]
    theta = 0.0
    NodesList = []
    x = start[0]
    y = start[1]
    cost = 0
    openList = dict()
    openList[(x,y,theta)] = [cost, x, y, theta, 0,0,-1]
    closedList = dict()
    found = False
    minTime = 1.0        # 8 /20
    step = minTime/10
    plt.axis([0, 11.1, 0, 10.1])
    plt.grid(True)
    plt.plot(start[0], start[1], 'go')
    plt.plot(goal[0], goal[1], 'ro')
    count = 0

    while not found:
        count = count + 1
        print(count)
        if len(openList) == 0:
            break
        currentId = min(
            openList, key=lambda i: openList[i][0] + calHeuristic(goal[0], goal[1], openList[i][1], openList[i][2]))
        currentNode = openList[currentId]
        # print(openList)
        closedList[currentId] = currentNode
        del openList[currentId]

        # print('currentNode:',currentNode)
        x = currentNode[1]
        y = currentNode[2]
        theta = currentNode[3]
        cost = currentNode[0]
        print('x:',x,'y:',y)
        if np.sqrt((y- goal[1])**2+ (x- goal[0])**2) < .5:
            print('goal reached')
            found = True
            break
        neighbours = findNeighbour(motionModel, step, minTime, x,y,theta)

        for i in range(len(neighbours)):
            neighbourX = neighbours[i][0]
            neighbourY = neighbours[i][1]
            neighbourTheta = neighbours[i][2]
            ur, ul = neighbours[i][3], neighbours[i][4]
            if ((neighbourX,neighbourY,neighbourTheta) in closedList) or obstacleCheck(neighbourX,neighbourY):
                continue

            h_value = round(abs(np.sqrt((neighbourX - goal[0])**2 + (neighbourY - goal[1])**2 )) *10,2)
            new_cost = cost + round(abs(np.sqrt((neighbourX - x)**2 + (neighbourY - y)**2 )) *10,2)
            f = new_cost + h_value

            if (neighbourX, neighbourY, neighbourTheta) in openList:
                if openList[(neighbourX,neighbourY,neighbourTheta)][0] + h_value > f:
                    del openList[(neighbourX,neighbourY,neighbourTheta)]
                    openList[(neighbourX,neighbourY,neighbourTheta)] = ((new_cost, neighbourX, neighbourY, neighbourTheta, ur, ul,currentId))
                    NodesList.append((neighbourX,neighbourY))
            else:
                openList[(neighbourX, neighbourY, neighbourTheta)] = ((new_cost, neighbourX, neighbourY, neighbourTheta, ur, ul,currentId))
                NodesList.append((neighbourX,neighbourY))

    for key in NodesList:
        plt.plot(key[0], key[1], 'xc')
        plt.pause(.0001)

    return closedList, currentId, found

def calHeuristic(x,y,x0,y0):
    return (np.sqrt((x0 - x)**2 + (y0 - y)**2)*20)

def findPath(closedList, currentId, found):

    if found:
        path = []
        child = closedList[currentId]
        plt.plot(child[1], child[2], 'go')
        path.append(child[3:6])
        while 1:
            id = child[-1]
            if not id == -1:
                child = closedList[id]
                path.append(child[3:6])
                plt.plot(child[1], child[2], 'go')
                plt.pause(0.00001)
            else:
                break
    else:
        print('Path cannot be reached with the initial RPM')
    path.reverse()
    plt.show()
    return path

def fileWrite(path):
    with open("path.txt", 'w') as file:
        file.writelines('\t'.join(str(j) for j in i) + '\n' for i in path)
        print('out')

if __name__ == '__main__':
    while 1:
        x_start = float(input('Enter the row grid coordinate of start point:'))
        y_start = float(input('Enter the col grid coordinate of start point:'))
        if obstacleCheck(x_start,y_start):
            print("The Value entered is in obstacle space")
            print('**************************************\n\n')
        else:
            break

    while 1:
        x_end = float(input('Enter the row grid coordinate of end point'))
        y_end = float(input('Enter the col grid coordinate of end point'))
        if obstacleCheck(x_end,y_end):
            print("The Value entered is in obstacle space")
            print('**************************************\n\n')
        else:
            break
    start = timeit.timeit()
    closedList, currentId, found = a_star([x_start, y_start], [x_end,y_end])
    path = findPath(closedList, currentId, found)
    fileWrite(path)
    end = timeit.timeit()
    print('Time taken to find path:', end - start)
