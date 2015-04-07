#include <unistd.h>	// for execl(3)
#include <stdlib.h>	// for EXIT_SUCCESS, EXIT_FAILURE

int main(int argc, char** argv, char** envp) {
	execl("./generate.py", "./generate.py", NULL);
	//return EXIT_FAILURE;
	return EXIT_SUCCESS;
}
