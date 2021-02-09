import sys

def bus_schedule():
    # Read the two lines and find the running buses
    departure_time, schedule = sys.stdin.read().splitlines()
    departure_time = int(departure_time)
    buses = [int(bus) for bus in schedule.split(',') if bus != 'x']

    current_time = departure_time
    solution = None
    while solution is None:
        
        # Check each bus
        for bus in buses:
            # If the current time is a multiple of the bus number, 
            # then it will arrive at this time
            if current_time % bus == 0:
                solution = bus * (current_time - departure_time)
        
        current_time += 1

    print(f'The solution is {solution}.')

def shuttle_contest():
    # Read the two lines and find the running buses
    _, schedule = sys.stdin.read().splitlines()
    buses = []
    for i, bus in enumerate(schedule.split(',')):
        if bus != 'x':
            # The time delay needs to be negative so it reflects the buses
            # arriving after, not before the multiple of the first bus
            buses.append((int(bus), i*-1))

    # This problem requires solving a series of modular equations
    # t = 0 % <bus_1>
    # t = 1 % <bus_2>
    # t = 4 % <bus_3>
    # ...
    #
    # We can do this using the chinese remainder theorem assuming the moduli 
    # are all coprime (in the case of the input file here, they are all prime)
    # Chinese Remainder Theorem Refresher: 
    # https://crypto.stanford.edu/pbc/notes/numbertheory/crt.html

    # M is simply the moduli multiplied together
    M = 1
    for bus, time_delay in buses:
        M *= bus

    # Solve according to the formula in the above link
    result = 0
    for bus, time_delay in buses:
        a_i = time_delay
        b_i = M // bus
        b_i_inv = pow(b_i, -1, bus)
        result += (a_i * b_i * b_i_inv)
    
    print(result % M)


if __name__ == '__main__':
    #bus_schedule()
    shuttle_contest()
