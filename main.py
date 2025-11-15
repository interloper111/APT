import math
from apt_class import Apt
from graph import graph_plotter
 
# y = 0 is defined at the ground.
# All APTs (alien pop-up toy) start from a 1.2m high bench.
# Since we are only measureing total time and vertical velocity, horizontal velocity is not used.
# Only allows for 2 APTs (for now).
    
apt1 = Apt(math.sqrt(10.791))
apt2 = Apt(0)
apt2.find_perfect_start_time(apt1.final_time)


graph_plotter(apt1.start_time, apt2.start_time, apt1.final_time, apt2.final_time, apt1.velocity, apt2.velocity)

