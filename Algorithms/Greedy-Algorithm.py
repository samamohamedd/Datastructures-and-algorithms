states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

stations = {}  # The keys are station names, and the values are the states they cover.
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = set()
best_station = None  # keep track of the station that covers the maximum number of states in each iteration
states_covered = set()  # keeps track of the states covered by the best_station

while states_needed:
    best_station = None
    states_covered = set()
    for station, states in stations.items():
        #  For each station, the code calculates the intersection between the states_needed set
        #  and the states covered by the current station using the & operator.
        # This intersection is stored in the covered variable.
        covered = states_needed & states
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    states_needed -= states_covered
    final_stations.add(best_station)

print(final_stations)
