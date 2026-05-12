#Problem 86
#A spider, S, sits in one corner of a cuboid room, measuring 6 by 5 by 3, and a fly, F, sits in the opposite corner.
#By travelling on the surfaces of the room the shortest "straight line" distance from S to F is 10 and the path is shown on the diagram.


#However, there are up to three "shortest" path candidates for any given cuboid and the shortest route doesn't always have integer length.

#It can be shown that there are exactly 2060 distinct cuboids, ignoring rotations, with integer dimensions, up to a maximum size of
#M by M by M, for which the shortest route has integer length when  M = 100.
#This is the least value of M for which the number of solutions first exceeds two thousand; the number of solutions when M = 99 is 1975.

#Find the least value of M such that the number of solutions first exceeds one million.

#If M >= a >= b >= c >= 1, then S_2 = sqrt((b+c)^2 + a^2) is the shortest path

import math

def first_M_where_it_exceeds(LIMIT = 1_000_000):

    M = 1
    num_sols = 0
    m_sq = 1
    
    while num_sols < LIMIT:
        new_sols = 0
        for b_plus_c in range(2, 2*M + 1):
            path_sq = b_plus_c * b_plus_c + m_sq
            if math.isqrt(path_sq)**2 == path_sq:
                #partitions of b_plus_c to b and c such that c <= b <= M
                if b_plus_c <= M:
                    new_sols += b_plus_c // 2
                else:
                    new_sols += M - (b_plus_c - 1) // 2
                        
        num_sols += new_sols
        M += 1
        m_sq = M*M
        
    return M - 1

print(first_M_where_it_exceeds())
