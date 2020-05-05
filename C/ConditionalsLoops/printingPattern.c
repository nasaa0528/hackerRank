#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#define min(a,b) ((a < b) ? (a) : (b))
int main() 
{

    int n,i,j,len;
    scanf("%d", &n);
    int tmp; 
    len = 2 * n - 1; 
    for(i = 0; i < len; i++){
        for(j = 0; j < len; j++){
            // printf("%d ", n);
            tmp = min(i,j);
            tmp = min(tmp, len - i - 1); 
            tmp = min(tmp, len - j - 1); 
            printf("%d ", n - tmp);
        }
        printf("\n");
    }
    return 0;
}


