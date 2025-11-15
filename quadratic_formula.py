import math

def quadratic_solve(a, b, c):
    
    # Returns real roots
    if (b**2 -(4 * a * c)) >= 0:
        
        x1 = (-b + math.sqrt(b**2 -(4 * a * c)))/ (2 * a)
        x2 = (-b - math.sqrt(b**2 -(4 * a * c)))/ (2 * a)
        
        return [x1, x2]
    
    # Returns complex roots
    else:
        
        x1 = (-b + (math.sqrt(-(b**2 -(4 * a * c)))) * 1j)/ (2 * a)
        x2 = (-b - (math.sqrt(-(b**2 -(4 * a * c)))) * 1j)/ (2 * a)
        
        return [x1, x2]

    

