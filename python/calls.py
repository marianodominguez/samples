'''
Calls is a recursive call stack analysis algorithm that returns the number of times each function is called.
'''

# List of calls
calls  = [
    "->a",
    "->b",
    "->c",
    "<-c",
    "->c",
    "<-c",
    "->c",
    "<-c",
    "<-b",
    "<-a",
]

# Stack of calls
stack=[]
# Counters of calls
counters = {}
# Path of calls
path=[]

# Process the calls
for call in calls:
    # Call to a function
    if call.startswith("->"):
        stack.append(call)
        path.append(call[2:])
    # Return from a function
    elif call.startswith("<-"):
        if stack:
            last_call = stack.pop()
            spath = "->".join(path)
            path.pop()
            # Increment the counter
            if spath in counters:
                counters[spath] += 1
            else:
                counters[spath] = 1
        else:
            print(f"Error: Unmatched return {call}")
    # Unknown call
    else:
        print(f"Unknown call: {call}")

# Print the call counts
print(f"Call counts: {counters}")