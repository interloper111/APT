import matplotlib.pyplot as plt
import numpy as np

g= 9.81

def graph_plotter(apt1StartTime, apt2StartTime, apt1FinalTime, apt2FinalTime, apt1VerticalVelocity, apt2VerticalVelocity):

    t1 = np.linspace(apt1StartTime, apt1FinalTime, 1000)
    t2 = np.linspace(apt2StartTime, apt2FinalTime, 1000)

    s1 = (apt1VerticalVelocity * (t1 - apt1StartTime)) + (-g/2)*((t1 - apt1StartTime))**2 + 1.2
    s2 = (apt2VerticalVelocity * (t2 - apt2StartTime)) + (-g/2)*((t2 - apt2StartTime))**2 + 1.2

    plt.axhline(y=0, color='grey', linestyle='--', linewidth=1)
    plt.axhline(y=1.2, color='grey', linestyle='--', linewidth=1)

    plt.xlabel("Time / s")
    plt.ylabel("Vertical displacement / m")
    plt.plot(t1,s1, label="Apt 1")
    plt.plot(t2,s2, label="Apt 2")
    plt.legend()
    # plt.savefig('AptPlot.png', dpi=600)
    plt.show()

