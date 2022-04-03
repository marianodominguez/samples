# Enter your code here. Read input from STDIN. Print output to STDOUT
l = [ -1, 2, 3, -4, -5, 6, 10, -10]

max_val = l[0]
max_pos = l[0]
initial=0
final=0

for index in range(1,len(l)):
    max_val = max(l[index], max_val+l[index])
    if max_val > max_pos:
        final = index
        max_pos = max_val
    else: 
	    initial=index
print("idx=", initial, final)

print(max_pos)
