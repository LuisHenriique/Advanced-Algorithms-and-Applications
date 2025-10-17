all: main.o


main.o: main.cpp
	g++ main.cpp -o main

run: all
	./main < 1.in

clear:

	rm -rf *.o main
