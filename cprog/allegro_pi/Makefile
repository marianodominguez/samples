############
MACHINE= $(shell uname -s)

# object files have corresponding source files
OBJS= main.o
CXX=gcc
COMPILER_FLAGS= -g
INCLUDE= -I/usr/include/aarch64-linux-gnu 
LIBS= -lallegro_font -lallegro -lm

EXEC= bin/cube

$(EXEC): $(OBJS)
	$(CXX) $(COMPILER_FLAGS) -o $(EXEC) $(OBJS) $(LIBS)

main.o: src/cube.c
	$(CXX) -c $(COMPILER_FLAGS) -o $@ $< $(INCLUDE)

clean:
	rm -f $(EXEC) $(OBJS)
