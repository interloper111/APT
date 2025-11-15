import matplotlib.pyplot as plt
import numpy as np

g= 9.81

def graph_plotter(apt1_start_time, apt2_start_time, apt1_final_time, apt2_final_time, apt1_vertical_velocity, apt2_vertical_velocity):

    t1 = np.linspace(apt1_start_time, apt1_final_time, 1000)
    t2 = np.linspace(apt2_start_time, apt2_final_time, 1000)

    s1 = (apt1_vertical_velocity * (t1 - apt1_start_time)) + (-g/2)*((t1 - apt1_start_time))**2 + 1.2
    s2 = (apt2_vertical_velocity * (t2 - apt2_start_time)) + (-g/2)*((t2 - apt2_start_time))**2 + 1.2

    plt.axhline(y=0, color='grey', linestyle='--', linewidth=1)
    plt.axhline(y=1.2, color='grey', linestyle='--', linewidth=1)

    plt.xlabel("Time / s")
    plt.ylabel("Vertical displacement / m")
    plt.plot(t1,s1, label="Apt 1")
    plt.plot(t2,s2, label="Apt 2")
    plt.legend()
    # plt.savefig('AptPlot.png', dpi=600)
    plt.show()


