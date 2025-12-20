'''
Rotate a list of files

Rotate a list of files by copying each file to the previous one and deleting the last file
'''

def rotate(l):
    print(l)
    for i in range(1,len( l )):
        # Copy the file
        print( 'copy {a} to {b}'.format(a=l[i], b=l[i-1]) )
    # Delete the last file
    print("echo ''> {f}".format(f=l[-1]))
f=[]

# Add files to the list
f.extend([f"test.{n}.log" for n in range(9,0, -1)])

f.append("test.log")
rotate(f)

