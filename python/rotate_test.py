def rotate(l):
    print(l)
    for i in range(1,len( l )):
        print( 'copy {a} to {b}'.format(a=l[i], b=l[i-1]) )
    print("echo ''> {f}".format(f=l[-1]))
f=[]

f.extend([f"test.{n}.log" for n in range(9,0, -1)])
f.append("test.log")
rotate(f)

