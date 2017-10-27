default types

-----
Variables

int 
x_64 word size matches address size

int=int64

in 32-bit arch or AMD_64_p-32
int=int32

____

all inits as zero

rules
var - zero
:= for initialize not zero


string 2-word struct
pointer dev nil, len =0 -> empty

Types and values

Casting -> extra memory, integrity

go has conversion

-----
struct
extra byte
padding byte alignment

group by size highest to smallest

____

no implicit conversion. assign different types

anonymous types can be converted implicit.

----



