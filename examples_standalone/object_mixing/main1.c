#include <stdio.h> // for printf(3)
#include "add.h"

int main(int argc,char** argv,char** envp) {
	printf("did you know that 2+2=%d\n", add(2,2));
}
