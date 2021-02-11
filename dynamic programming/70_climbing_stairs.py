def climbStairs(n: int) -> int:
    cur_res, m2, m1 = 0, 1, 2
    if n == 1:
        return m2
    if n == 2:
        return m1
    
    for i in range(2, n):
        cur_res = m1 + m2
        m2, m1 = m1, cur_res
    
    return cur_res