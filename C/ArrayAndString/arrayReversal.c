#include <stdio.h>
#include <stdlib.h>

/* Given an array, of size  n, reverse it.
Example: If array, arr = [1,2,3,4,5] , after reversing it, the array should be, arr=[5,4,3,2,1]. */ 

int main(){
    int n, tmp,i; 
    scanf("%d",&n);
    // functions 
    int  arr[n];
    void printArray(int arr[], int len);
    for(i = 0; i < n; i++)
        scanf("%d", &arr[i]);
    for(i = 0; i < n/2; i++){
        tmp = arr[i]; 
        arr[i] = arr[n-i-1]; 
        arr[n-i-1] = tmp; 
    }
    printArray(arr, n);
}
void printArray(int arr[], int len){
    for(int i = 0; i < len; i++)
        printf("%d ", arr[i]);
}
