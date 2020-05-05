#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
//Complete the following function.


void calculate_the_maximum(int n, int k) {
    int andMax, orMax, xOrMax; 
    andMax = orMax = xOrMax = 0;
    int i, j;  
    for(i = 1; i <= n; i++){
        for(j = i + 1; j<=n; j++){ 
            if((i & j) < k && andMax < (i & j))
                andMax = i & j; 
            if((i | j) < k && orMax < (i | j))
                orMax = i | j; 
            if((i ^ j) < k && xOrMax < (i ^ j))
                xOrMax = i ^ j; 
        }
    }
    printf("%d\n", andMax);
    printf("%d\n", orMax);
    printf("%d\n", xOrMax);
}

int main() {
    int n, k;
  
    scanf("%d %d", &n, &k);
    calculate_the_maximum(n, k);
 
    return 0;
}

