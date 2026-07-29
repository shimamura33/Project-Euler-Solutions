# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 14:38:31 2026

@author: phoeb
"""

#!/usr/bin/env python
#和p71差不多 引用分数相关的gcd方程
import math 

print(sum(1 for d in range(2, 12001) 
          for n in range(1, d) 
          if (n*3 > d) and (n*2 < d) and math.gcd(n, d) == 1))

