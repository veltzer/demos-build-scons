#include "add.h"

int mul(int a,int b) {
	int i, sum;
	sum=0;
	for(i=0;i<a;i++) {
		sum=add(sum, b);
	}
	return sum;
}
