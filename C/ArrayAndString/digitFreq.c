#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    char ch, i; 
    int *freq = (int *)calloc(11,sizeof(int));
    while((ch = getchar()) != '\n'){
        if(ch >= '0' && ch <= '9'){
            *(freq + ch - '0') += 1;
            } 
    }
    for(i = 0; i < 10; i++)
        printf("%d ", *(freq + i));
    return 0;
}

