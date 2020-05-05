#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    
    int n;
    int sumOfFiveDig(int); 
    scanf("%d", &n);
    printf("%d\n", sumOfFiveDig(n));
    //Complete the code to calculate the sum of the five digits on n.
    return 0;
}

int sumOfFiveDig(int n){
    int sum = 0; 
    while(n > 0){
        sum += n%10; 
        n /= 10; 
    }
    return sum; 
}
