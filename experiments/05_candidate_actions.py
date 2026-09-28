#Candidate Action Library

#Objective: This small library contains a set of candidate actions that can be used in various experiments.
#Each action is defined as a function that performs a specific task or operation.

import grid2op
import time

#Define candidate actions
candidate_actions = {
    "no_action": {},
    "increase_generator_0": {
        "redispatch": [(0, 10.0)]
    },
    "increase_generator_1": {
        "redispatch": [(1, 10.0)]
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

    #Disconnect line 17 to simulate a line outage
    outage_action = env.action_space({"set_line_status": [(17, -1)]})
    env.step(outage_action)

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