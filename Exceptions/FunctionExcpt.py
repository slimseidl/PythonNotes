def steps_to_miles(steps):
    if steps > 0:
        miles = steps / 2000
        return miles
    else:
        raise ValueError('Exception: Negative step count entered.')
    

if __name__ == '__main__':
    try:
        step_count = int(input())
        print(f'{steps_to_miles(step_count):.2f}')
    except ValueError as e:
        print(e)