'''
Read access log

Read an access log file and calculate the rate of 2xx responses and the number of unique clients per hour.
Access log format: ip - - [date] "method url protocol" status size

'''
# Open the file
f=open('access.log',"r")

def rate(lines):
    # Number of 2xx responses
    num_200=0;
    # List of 2xx responses
    sl = [ x for x in lines if x['status'].startswith('2') ]
    #print(sl)
    num_200=len(sl)
    return num_200/len(lines)

def unique_clients_hour(lines):
    # Dictionary of clients
    clients={}
    # For each line
    for record in lines:
        # Hour
        hour=record['date'][:-6]
        # Client
        clients[record['ip']+"_"+hour] = record
    # Return the number of unique clients
    return len(clients.keys())

lines = []
# For each line
for line in f:
    # Skip empty lines
    if line.strip()=='':
        continue
    # Split the line
    fields=line.split(' ')
    # Record
    record= {
        "ip": fields[0],
        "status": fields[8],
        "date": fields[3][1:]
        }
    # Add the record
    lines.append(record)

# Print the rate
print(rate(lines))
# Print the number of unique clients
print(unique_clients_hour(lines))