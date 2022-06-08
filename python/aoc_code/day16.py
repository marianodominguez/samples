
def decode(msg, nbits,offset):
    group=[]
    allbits=""
    totalbits=sum(nbits)
    end=totalbits//4+1
    start=offset//4
    ignorebits=offset % 4
    for d in msg[start:end]:
        v=int(d,16)
        allbits+='{:04b}'.format(v)
    allbits=allbits[ignorebits:]
    
    j=0
    for n in nbits:
       val=int(allbits[j:j+n],2)
       group.append(val)
       j+=n
    return group

#msg='38006F45291200'
msg='D2FE28'

d=decode(msg, [3,3,5,5] ,0)
version=d[0]
type=d[1]

if type==4:
    offset=7
    end=0
    val=''
    while not end:
        pack=decode(msg,[1,3],offset)
        end=1-pack[0]
        val+='{:04b}'.format(pack[1])
        offset+=4
    pack=decode(msg,[3],offset)
    val+='{:04b}'.format(pack[1])
    print(val)
    print('{:d}'.format(val))
        
