import math
from aptClass import Apt
from graph import graphPlotter
 
# y = 0 is defined at the ground.
# All APTs (alien pop-up toy) start from a 1.2m high bench.
# Since we are only measureing total time and vertical velocity, horizontal velocity is not used.
# Only allows for 2 APTs (for now).
    
apt1 = Apt(math.sqrt(10.791))
apt2 = Apt(0)
apt2.findPerfectStartTime(apt1.finalTime)

graphPlotter(apt1.startTime, apt2.startTime, apt1.finalTime, apt2.finalTime, apt1.velocity, apt2.velocity)