f=open('access.log',"r")

def rate(lines):
    num_200=0;
    sl = [ x for x in lines if x['status'].startswith('2') ]
    #print(sl)
    num_200=len(sl)
    return num_200/len(lines)

def unique_clients_hour(lines):
    clients={}
    for record in lines:
        hour=record['date'][:-6]
        clients[record['ip']+"_"+hour] = record
    return len(clients.keys())

lines = []
for line in f:
    if line.strip()=='':
        continue
    fields=line.split(' ')
    record= {
        "ip": fields[0],
        "status": fields[8],
        "date": fields[3][1:]
        }
    #print(record)
    lines.append(record)

print(rate(lines))
print(unique_clients_hour(lines))