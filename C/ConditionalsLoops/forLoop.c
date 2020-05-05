#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

#define DIGITLEN 11 
// For each integer  in the interval  (given as input) :

// If 1<=n<=9 , then print the English representation of it in lowercase. That is "one" for , "two" for , and so on.
// Else if n>9 and it is an even number, then print "even".
// Else if n>9  and it is an odd number, then print "odd".
const char *digits[DIGITLEN] = {"", 
                        "one", "two", "three",
                        "four", "five", "six",
                        "seven", "eight", "nine",
                        }; 
const char *oddEven[3] = {"odd", "even"};
int main() 
{
    int a, b;
    int for_loop(int, int);
    scanf("%d\n%d", &a, &b);
      for_loop(a,b);
    return 0;
}
int for_loop(int a, int b){
    int i; 
    for (i = a; i <= b; i++){
        if(i>=1 && i <= 9)
            printf("%s\n", digits[i]);
        else if(i > 9 && i % 2 != 0)
            printf("%s\n", oddEven[0]);
        else 
            printf("%s\n", oddEven[1]);
    }   
    return 1; 
}

