#include <stdio.h>

int cpu_intensive(int i) {
	double j = 0.0;
	for(int x=1;x<i;x++){
		j += i;
		j *= 1.0000001;
		j /= 1.0000001;
	}
	return j;
}

