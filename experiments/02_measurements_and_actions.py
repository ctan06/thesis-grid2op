#Measurements and actions

#Objective: Identify the measurements and actions available in the Grid2Op environment.

import grid2op

env = grid2op.make("l2rpn_case14_sandbox")
obs = env.reset()

#The measurements available in the environment are stored in the observation object.
#The observation object contains various attributes that represent the state of the power grid.
print()
print("Measurements available in the environment:")
for observation in obs.attr_list_vect:
    print(observation)
print()

print("Certain observation values:")
print("Generator active power:", obs.gen_p)
print()
print("Load active power:", obs.load_p)
print()
print("Line status:", obs.line_status)
print()
print("Current line loadings:", obs.rho)
print()
print("Topology vector:", obs.topo_vect)
print()

#The actions available in the environment are defined by the action space of the environment.
print("Actions available in the environment:")
for action in env.action_space.attr_list_vect:
    print(action)
print()

env.close()