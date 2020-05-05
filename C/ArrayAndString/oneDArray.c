#include <stdio.h>
#include <stdlib.h>

#define MAXLEN 100

int main() {
    int i, n, *arr = (int *)malloc(sizeof(int) * n); 
    long int sum = 0; 
    scanf("%d", &n); 
    for(i = 0; i < n; i++){
        scanf("%d", (arr+i));
        sum += *(arr + i); 
    } 
    printf("%ld", sum);
    return 0;
}


