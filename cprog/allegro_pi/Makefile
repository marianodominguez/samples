############
MACHINE= $(shell uname -s)

# object files have corresponding source files
OBJS= main.o
CXX=g++
COMPILER_FLAGS= -g
INCLUDE= -I/usr/include/aarch64-linux-gnu 
LIBS= -lallegro_font -lallegro

EXEC= bin/cube

$(EXEC): $(OBJS)
	$(CXX) $(COMPILER_FLAGS) -o $(EXEC) $(OBJS) $(LIBS)

main.o: cube.c
	$(CXX) -c $(COMPILER_FLAGS) -o $@ $< $(INCLUDE)

clean:
	rm -f $(EXEC) $(OBJS)
