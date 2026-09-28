#Measurement Bias Attack

#Objective: This experiment demonstrates how to introduce a measurement bias into the observation of a power grid environment.
#The bias is applied to a specific measurement (in this case, the active power output of a generator) 
#without affecting the physical state of the environment.

import grid2op
import numpy as np

env = grid2op.make("l2rpn_case14_sandbox")
obs = env.reset()

#Select a specific measurement to introduce a bias. In this case, we choose the active power output of generator 0.
generator_id = 0
#Record the physical value of the selected measurement before introducing the bias.
physical_value = obs.gen_p[generator_id]


#Create a copy of the observation to simulate the reported observation that a controller would receive.
#Modifying this copy does not apply an action to the physical simulator.
reported_obs = obs.copy()

#The bias value to be added to the reported measurement.
bias = 20.0
#Apply the bias to the reported observation.
reported_obs.gen_p[generator_id] += bias


#Compare the physical observation and the reported observation to demonstrate that the physical state remains unchanged
# while the reported observation reflects the bias.
print("\nGenerator:", generator_id)
#Physical generator output.
print("Physical generator output:", physical_value, "MW")
#Before introducing the bias.
print("Reported generator output before bias:",obs.gen_p[generator_id], "MW")
#After introducing the bias.
print("Reported generator output after bias:", reported_obs.gen_p[generator_id], "MW")


env.close()