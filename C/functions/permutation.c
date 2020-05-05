#include <stdio.h>
#include <stdlib.h>
#include <string.h>
void swap(char **s, int n , int m){
    char *tmp; 
    tmp = s[n]; 
    s[n] = s[m]; 
    s[m] = tmp;
}

int next_permutation(int n, char **s)
{
    int k, l; 
    k = n - 1; 
    while(k > 0){
        if(strcmp(s[k-1],s[k]) < 0) 
            break;
        else if(strcmp(s[k-1], s[k]) == 0){
            k--; 
            continue; 
        }
        k--; 
    }
    if(k == 0)
        return 0;
    l = n - 1; 
    while( l > (k - 1)){
        if(strcmp(s[k-1], s[l]) < 0)
            break; 
        l--; 
    }
    swap(s, k-1 , l);
    for(k; k < n; k++, n--){
        swap(s,k,n-1);
    }
    return 1; 
}

