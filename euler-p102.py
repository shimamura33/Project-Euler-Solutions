# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 15:10:07 2026

@author: phoeb
"""

import numpy as np

file_directory = 'E:\\Downloads\\0102_triangles.txt'

"""
https://medium.com/@ev.zafeiratos/check-whether-0-lies-inside-a-triangle-or-not-2-axis-57edd570e5b3

If we take any point and connect that point to each vertex of the triangle, the result is three subtriangles with areas A1, A2 and A3, as shown below. For a triangle with a total area of A, we call the subset (A1/A, A2/A, A3/A) the barycentric coordinates of point P.
To solve the problem, we will make use of the vector status of area, which means there is a direction associated with it. For each area, not only triangles, there is an entity defined as vector normal which is calculated by the cross product of the corresponding vectors.


Vector normals are vector measures as well, but since we operate on a
2–D plane the direction of these cross products is going to be z-axis itself.
We expect each of the subtriangle vector normals to have same direction with the direction of the original triangle vector normal.
Therefore, the condition to be met so that (0,0) resides within the triangle area is that each of the cross products calculated for sub-areas has the same sign as the cross product of the area A.

STEP 1 : Read each line from the file
STEP 2 : Initiate the vectors for main triangle & subtriangles and calculate the vector normal for each.
STEP 3 : Check whether the condition described above is met and increase the corresponding counter if this is the case.
"""


with open(file_directory) as reader:
    line = reader.readline()
    counter=0
    while line!= '':
        numbers=[int(number) for number in line.split(',')]

    #Calculate ab&ac vectors
        ab=[numbers[2]-numbers[0],numbers[3]-numbers[1]]
        ac=[numbers[4]-numbers[0],numbers[5]-numbers[1]]
        abxac=int(np.cross(ab,ac))
    
    #Calculate bc&ba vectors,where pis the（0，0）point
        bc=[numbers[4]-numbers[2],numbers[5]-numbers[3]]
        bp=[0-numbers[2],0-numbers[3]]
        bcxbp =int(np.cross(bc,bp))
    
    #Calculate ca&cb vectors，where pis the（0，0）point
        ca=[numbers[0]-numbers[4],numbers[1]-numbers[5]]
        cp=[0-numbers[4],0-numbers[5]]
        caxcp=int(np.cross(ca,cp))
    
    #calculate ab&ap vectors where pis the（0，0）point
        ab=[numbers[2]-numbers[0],numbers[3]-numbers[1]]
        ap=[0-numbers[0],0-numbers[1]]
        abxap=int(np.cross(ab,ap))

#Set　the　flag to false　in case
#there is at least one negative product
        flag=True
    
        if(abxac*bcxbp<0):
            flag =False
        elif(abxac *caxcp<0):
            flag=False
        elif(abxac*abxap<0):
            flag =False
        if flag:
            counter+=1
    
        line=reader.readline()

print('The number of points inside trianges is:',counter)