from quadratic_formula import quadratic_solve

# Made class for the APTs, only input is initial vertical velocity
# (since initial horizontal velocity is not required for any of the calculations I have not inlcuded it)


# Gravitaional constant for earth to 3sf

g= 9.81


class Apt:
    
    def __init__(self, initial_vertical_velocity):
        
        self.start_time = 0
        self.velocity = initial_vertical_velocity
        self.final_time = quadratic_solve((-g/2), self.velocity, 1.2)[1] + self.start_time
        
    def find_perfect_start_time(self, other_final_time):
        # Finds the perfect start time to hit the ground at the same time as apt1
        self.start_time = other_final_time - self.final_time
        self.final_time = quadratic_solve((-g/2), self.velocity, 1.2)[1] + self.start_time

                        
            

            
