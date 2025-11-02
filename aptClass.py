from quadraticFormula import quadraticFormula

# Made class for the APTs, only input is initial vertical velocity
# (since initial horizontal velocity is not required for any of the calculations I have not inlcuded it)


# Gravitaional constant for earth to 3sf

g= 9.81


class Apt:
    
    def __init__(self, initialVerticalVelocity):
        
        self.startTime = 0
        self.velocity = initialVerticalVelocity
        self.finalTime = quadraticFormula((-g/2), self.velocity, 1.2)[1] + self.startTime
        
    def findPerfectStartTime(self, otherFinalTime):
        # Finds the perfect start time to hit the ground at the same time as apt1
        self.startTime = otherFinalTime - self.finalTime
        self.finalTime = quadraticFormula((-g/2), self.velocity, 1.2)[1] + self.startTime

                        
            
            