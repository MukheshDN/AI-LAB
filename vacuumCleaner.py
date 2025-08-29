def vacuum_world():
    # initializing goal_state
    # '0' indicates Clean and '1' indicates Dirty
    goal_state = {'A': '0', 'B': '0'}
    cost = 0

    # Input from user
    location_input = input("Enter Location of Vacuum (A or B): ").upper()
    status_input = input("Enter status of " + location_input + " (0 for Clean, 1 for Dirty): ")
    status_input_complement = input("Enter status of the other room (0 for Clean, 1 for Dirty): ")

    print("\nInitial Location Conditions:", goal_state)

    if location_input == 'A':
        print("Vacuum is placed in Location A")

        if status_input == '1':
            print("Location A is Dirty.")
            goal_state['A'] = '0'  # Clean it
            cost += 1
            print("CLEANED A. Cost:", cost)
        else:
            print("Location A is already clean.")

        if status_input_complement == '1':
            print("Location B is Dirty.")
            print("Moving RIGHT to Location B.")
            cost += 1  # Moving cost
            print("Moved RIGHT. Cost:", cost)
            goal_state['B'] = '0'  # Clean it
            cost += 1
            print("CLEANED B. Cost:", cost)
        else:
            print("Location B is already clean. No action needed.")

    elif location_input == 'B':
        print("Vacuum is placed in Location B")

        if status_input == '1':
            print("Location B is Dirty.")
            goal_state['B'] = '0'  # Clean it
            cost += 1
            print("CLEANED B. Cost:", cost)
        else:
            print("Location B is already clean.")

        if status_input_complement == '1':
            print("Location A is Dirty.")
            print("Moving LEFT to Location A.")
            cost += 1  # Moving cost
            print("Moved LEFT. Cost:", cost)
            goal_state['A'] = '0'  # Clean it
            cost += 1
            print("CLEANED A. Cost:", cost)
        else:
            print("Location A is already clean. No action needed.")

    else:
        print("Invalid input for location. Please enter 'A' or 'B'.")
        return

    print("\nGOAL STATE:", goal_state)
    print("Performance Measurement (Total Cost):", cost)
