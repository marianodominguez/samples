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

stack=[]
counters = {}
path=[]

for call in calls:
    if call.startswith("->"):
        stack.append(call)
        path.append(call[2:])
    elif call.startswith("<-"):
        if stack:
            last_call = stack.pop()
            spath = "->".join(path)
            path.pop()
            if spath in counters:
                counters[spath] += 1
            else:
                counters[spath] = 1
        else:
            print(f"Error: Unmatched return {call}")
    else:
        print(f"Unknown call: {call}")

print(f"Call counts: {counters}")