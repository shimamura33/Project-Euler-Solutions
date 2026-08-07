# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 11:10:28 2026

@author: phoeb
"""

'''
暴力求解1 AI版
'''
import math

def solve_euler_91(limit=50):
    count = 0
    
    # Case 1: Right angle is at the origin O(0,0)
    # P must be on the positive x-axis and Q on the positive y-axis
    count += limit * limit
    
    # Case 2: Right angle is on the x-axis or y-axis (but not at the origin)
    # For a fixed point on an axis, there are exactly 'limit' options for the third vertex
    count += 2 * (limit * limit)
    
    # Case 3: Right angle is at a point P(x, y) inside the grid (x > 0, y > 0)
    for x in range(1, limit + 1):
        for y in range(1, limit + 1):
            # Find the simplified perpendicular vector component
            g = math.gcd(x, y)
            dx = y // g
            dy = x // g
            
            # Count valid integer steps Q can make in both perpendicular directions
            # Moving down and right: P + k*(dx, -dy)
            k_down_right = min((limit - x) // dx, y // dy)
            
            # Moving up and left: P + k*(-dx, dy)
            k_up_left = min(x // dx, (limit - y) // dy)
            
            count += k_down_right + k_up_left
            
    return count

if __name__ == "__main__":
    print(f"Total right triangles: {solve_euler_91(50)}")


'''
暴力求解2 更短
'''
# https://www.nayuki.io/page/project-euler-solutions
# https://github.com/nayuki/Project-Euler-solutions
# 

def compute():
	LIMIT = 51
	ans = sum(1
		for x1 in range(LIMIT)
		for y1 in range(LIMIT)
		for x2 in range(LIMIT)
		for y2 in range(LIMIT)
		# For uniqueness, ensure that (x1,y1) has a larger angle than (x2,y2)
		if y2 * x1 < y1 * x2 and is_right_triangle(x1, y1, x2, y2))
	return str(ans)


# Tests whether the three points {(0,0), (x1,y1), (x2,y2)} form a right triangle.
def is_right_triangle(x1, y1, x2, y2):
	a = x1**2 + y1**2
	b = x2**2 + y2**2
	c = (x2 - x1)**2 + (y2 - y1)**2
	return (a + b == c) or (b + c == a) or (c + a == b)


if __name__ == "__main__":
	print(compute())