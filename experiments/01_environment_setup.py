#Grid2Op Environment Setup

#Objective: Verify that the Grid2Op environment is set up correctly and can be used to simulate power grid operations.

#Environment: l2rpn_case14_sandbox


#Loads the Grid2Op so Python can use it
import grid2op

#Creates the simulated 14-substation power grid in memory
env = grid2op.make("l2rpn_case14_sandbox")
#Starts the simulation and returns the current state/observation of the grid
obs = env.reset()
print()
print("Environment created successfully.")
print()

#Display basic information about the grid
print("Environment:", env.name)
print("Number of substations:", env.n_sub)
print("Number of lines:", env.n_line)
print("Number of generators:", env.n_gen)
print("Number of loads:", env.n_load)
print("Maximum line loading:", obs.rho.max())

#Close the environment to free up resources
env.close()