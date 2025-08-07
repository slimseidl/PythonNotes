def feet_to_steps(user_feet):
    steps = int(user_feet / 2.5)
    return steps


print(f'Enter number of feet walked:')
feet = float(input())
print(f'Number of steps walked: {feet_to_steps(feet)}')