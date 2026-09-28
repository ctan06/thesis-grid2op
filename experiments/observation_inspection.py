#loads the Grid2Op so Python can use it
import grid2op

#creates the simulated 14-substation power grid 
env = grid2op.make("l2rpn_case14_sandbox")
obs = env.reset()           #starts the simulation and gives us the current state/observation

print("Environment created successfully.")
print("Number of lines:", env.n_line)
print("Number of generators:", env.n_gen)
print("Number of loads:", env.n_load)
print("Maximum line loading:", obs.rho.max())