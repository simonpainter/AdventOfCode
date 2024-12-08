import re, itertools, math,os,sys
pathname = os.path.dirname(sys.argv[0])        
input = pathname + "/input.txt"

def parse_input(path):
    with open(path, "r") as inputfile:
        data = inputfile.read()
        lines = data.split('\n')
        
    # Sort entries chronologically
    lines = [line for line in lines if line]  # Remove empty lines
    lines.sort()
    
    # Process log entries
    current_guard = None
    sleep_start = 0
    guard_schedules = {}
    
    for line in lines:
        # Extract minute from timestamp
        minute = int(line[15:17])
        
        if "Guard" in line:
            current_guard = int(line.split("#")[1].split()[0])
            if current_guard not in guard_schedules:
                guard_schedules[current_guard] = [0] * 60
        elif "falls asleep" in line:
            sleep_start = minute
        elif "wakes up" in line:
            # Mark minutes as asleep
            for i in range(sleep_start, minute):
                guard_schedules[current_guard][i] += 1
    
    return guard_schedules  # Return the guard_schedules directly


def part1(guard_schedules):
    max_sleep = 0
    sleepiest_guard = None
    
    # Find guard with most total sleep
    for guard_id, schedule in guard_schedules.items():
        total_sleep = sum(schedule)
        if total_sleep > max_sleep:
            max_sleep = total_sleep
            sleepiest_guard = guard_id
    
    # Find minute most frequently asleep
    max_minute_freq = max(guard_schedules[sleepiest_guard])
    sleepiest_minute = guard_schedules[sleepiest_guard].index(max_minute_freq)
    
    return sleepiest_guard * sleepiest_minute

def part2(guard_schedules):
    max_freq = 0
    result = 0
    
    # Find guard and minute with highest frequency
    for guard_id, schedule in guard_schedules.items():
        minute_freq = max(schedule)
        if minute_freq > max_freq:
            max_freq = minute_freq
            sleepiest_minute = schedule.index(minute_freq)
            result = guard_id * sleepiest_minute
            
    return result



print(part1(parse_input(input)))
print(part2(parse_input(input)))