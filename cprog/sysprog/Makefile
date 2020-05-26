ALL := hello hello_dbg getreg_rcx getreg_cr0

CC=gcc
CFLAGS_DBG=-g -ggdb -gdwarf-4 -O0 -Wall -Wextra
CFLAGS=-Wall -Wextra
BIN=bin
all: ${ALL}
CB_FILES := *.[ch]

hello: hello.c
	${CC} ${CFLAGS} hello.c -o ${BIN}/hello
hello_dbg: hello.c
	${CC} ${CFLAGS_DBG} hello.c -o ${BIN}/hello_dbg
	objdump --source ${BIN}/hello_dbg > ${BIN}/hello_dbg_objdump.txt

getreg_rcx: getreg_rcx.c
	${CC} ${CFLAGS} getreg_rcx.c -o ${BIN}/getreg_rcx
getreg_cr0: getreg_cr0.c
	${CC} ${CFLAGS_DBG} getreg_cr0.c -o ${BIN}/getreg_cr0

# indent- "beautifies" C code into the "Linux kernel style".
# (cb = C Beautifier :) )
# Note! original source file(s) is overwritten, so we back it up.
cb: ${CB_FILES}
	mkdir bkp 2> /dev/null; cp -f ${CB_FILES} bkp/
	indent -linux ${CB_FILES}

clean:
	rm -vf ${ALL} ${BIN}/core* ${BIN}/*.o *~