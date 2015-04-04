#include "mul.h" // for mul(U)
#include <stdio.h> // for printf(3)
#include <stdlib.h> // for EXIT_SUCCESS, atoi(3)

int main(int argc, char** argv, char** envp) {
	int a=atoi(argv[1]);
	int b=atoi(argv[2]);
	printf("did you know that %d * %d is %d ?\n", a, b, mul(a,b)); 
	return EXIT_SUCCESS;
}
