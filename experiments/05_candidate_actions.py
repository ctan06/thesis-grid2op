#Candidate Action Library

#Objective: This small library contains a set of candidate actions that can be used in various experiments.
#Each action is defined as a function that performs a specific task or operation.

import grid2op
import time

#Define candidate actions
candidate_actions = {
    "no_action": {},
    "increase_generator_0": {
        "redispatch": [(0, 5.0)]
    },
    "reconnect_line_17": {
        "set_line_status": [(17, 1)]
    },
}

#Function to create a environment and disconnect line 17
def create_post_outage_environment():

    #Create a new Grid2Op environment
    env = grid2op.make("l2rpn_case14_sandbox")
    env.reset()

    print("Generator ramp-up limits:", env.gen_max_ramp_up)
    print("Generator ramp-down limits:", env.gen_max_ramp_down)
    print("Generator maximum outputs:", env.gen_pmax)
    print("Generator minimum outputs:", env.gen_pmin)

    print("\n===== INITIAL GRID CONDITION =====")

    print("Current timestep:", env.get_obs().current_step)

    print("Generator outputs:", env.get_obs().gen_p)

    print("Load demands:", env.get_obs().load_p)

    print("Line statuses:", env.get_obs().line_status)

    print("Grid topology:", env.get_obs().topo_vect)

    print("Line loadings:", env.get_obs().rho)

    print("==================================\n")

    #Disconnect line 17 to simulate a line outage
    outage_action = env.action_space({"set_line_status": [(17, -1)]})
    obs_after_outage, reward, done, info = env.step(outage_action)

    print("\n===== GRID CONDITION AFTER OUTAGE =====")

    print("Current timestep:", obs_after_outage.current_step)
    print("Generator outputs:", obs_after_outage.gen_p)
    print("Load demands:", obs_after_outage.load_p)
    print("Line statuses:", obs_after_outage.line_status)
    print("Grid topology:", obs_after_outage.topo_vect)
    print("Line loadings:", obs_after_outage.rho)

    print("=======================================\n")

    return env

#Apply and evaluate candidate actions
for name, action_dict in candidate_actions.items():

    #Create a new environment for each candidate action to ensure independence of simulations.
    env = create_post_outage_environment()

    #Convert the candidate dictionary into a Grid2Op action.
    action = env.action_space(action_dict)

    #Record the time taken to create the environment and apply the outage action
    start_time = time.perf_counter()

    #Apply the candidate action.
    obs, reward, done, info = env.step(action)
    #Display the timestep after applying the candidate action.
    print("Timestep after candidate action:", obs.current_step)
    print("Exception details:", info.get("exception"))
    #Record the time taken to apply the action and receive the resulting observation.
    execution_time = time.perf_counter() - start_time


    #Measure the resulting grid state.
    maximum_loading = obs.rho.max()

    #Total load disconnected from the grid.
    disconnected_load = obs.load_p[obs.load_p == 0].sum()

    overloaded_lines = (obs.rho > 1.0).sum()

    #Display the results.
    print()
    print("Action:", name)
    print("Maximum line loading:", maximum_loading)
    print("Number of overloaded lines:", overloaded_lines)
    print("Solver status:", "Failed" if info["exception"] else "Successful")
    print("Disconnected load:", disconnected_load)
    print("Execution time:", execution_time, "seconds")
    print("Reward:", reward)
    print("Done:", done)

    env.close()