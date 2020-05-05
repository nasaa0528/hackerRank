i#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#define MAXLEN 100 
int main() 
{
    char ch; 
    char s[MAXLEN]; 
    char sen[MAXLEN]; 
    scanf("%c", &ch); 
    scanf("%s", &s); 
    scanf("\n"); 
    scanf("%[^\n]%*c", &sen);
    printf("%c\n", ch);
    printf("%s\n", s); 
    printf("%s\n", sen);
    return 0;
}
