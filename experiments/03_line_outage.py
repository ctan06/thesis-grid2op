#Line Outage Experiment

#Objective: Simulate a line outage in the Grid2Op environment and observe the impact on the power grid.

import grid2op

env = grid2op.make("l2rpn_case14_sandbox")
obs = env.reset()

print("\n===== INITIAL GRID CONDITION =====")

print("Current timestep:", obs.current_step)

print("Generator outputs:", obs.gen_p)

print("Load demands:", obs.load_p)

print("Line statuses:", obs.line_status)

print("Grid topology:", obs.topo_vect)

print("Line loadings:", obs.rho)

print("==================================\n")

#Select the line to disconnect (e.g., line 17)
line_to_disconnect = 17

#Record the initial state of the grid before the line outage
max_line_loading_before = obs.rho.max()
print("Before line outage:")
print("Line to disconnect:", line_to_disconnect)
print("Line status:", obs.line_status[line_to_disconnect])
print("Line loading:", obs.rho[line_to_disconnect])
print("Maximum line loading:", max_line_loading_before)
print()

#Perform the line outage by disconnecting the selected line
action = env.action_space({"set_line_status": [(line_to_disconnect, -1)]})
obs_after, reward, done, info = env.step(action)

print("\n===== GRID CONDITION AFTER OUTAGE =====")

print("Current timestep:", obs_after.current_step)
print("Generator outputs:", obs_after.gen_p)
print("Load demands:", obs_after.load_p)
print("Line statuses:", obs_after.line_status)
print("Grid topology:", obs_after.topo_vect)
print("Line loadings:", obs_after.rho)

print("=======================================\n")

#Record the state of the grid after the line outage
max_line_loading_after = obs_after.rho.max()
print("After line outage:")
print("Disconnected line:", line_to_disconnect)
print("Line status:", obs_after.line_status[line_to_disconnect])
print("Line loading:", obs_after.rho[line_to_disconnect])
print("Maximum line loading:", max_line_loading_after)
print()
print("Reward received:", reward)
print("Done:", done)
print()

#Identify any overloaded lines after the outage and the most heavily loaded line
overloaded_lines = [i for i, loading in enumerate(obs_after.rho) if loading > 1.0]
print("Overloaded lines after outage:", overloaded_lines)
print("Most heavily loaded line after outage:", obs_after.rho.argmax())
print("Maximum line loading after outage:", max_line_loading_after)
print()

env.close()