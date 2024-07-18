# Given a set of activities with start and end times, select the maximum number 
# of activities that can be performed by a single person, assuming that a person 
# can only work on a single activity at a time.

def max_activities(start, end):
    n = len(start)  # Number of activities
    activities = list(zip(start, end))  # Combine start and end times
    # Sort activities by end times
    activities.sort(key=lambda x: x[1])

    selected_activities = []  # List to store the selected activities
    last_end_time = 0  # Initialize the end time of the last selected activity

    for i in range(n):
        # If the start time of the current activity is greater than or equal to the end time of the last selected activity
        if activities[i][0] >= last_end_time:
            selected_activities.append(activities[i])  # Select the current activity
            last_end_time = activities[i][1]  # Update the end time of the last selected activity

    return selected_activities

# Test Maximum Activities
start_times = [1, 3, 0, 5, 8, 5]
end_times = [2, 4, 6, 7, 9, 9]
print("Selected activities:", max_activities(start_times, end_times))  
# Output: [(1, 2), (3, 4), (5, 7), (8, 9)]
