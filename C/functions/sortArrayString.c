#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int lexicographic_sort(const char* a, const char* b) {
    return -strcmp(a,b);
}
int lexicographic_sort_reverse(const char* a, const char* b) {
    return strcmp(a,b); 
}
int sort_by_number_of_distinct_characters(const char* a, const char* b) {
    char *tmp_a, *tmp_b; 
    int i, j; 
    tmp_a = (char *)calloc(1024, sizeof(char));
    tmp_b = (char *)calloc(1024, sizeof(char));
    for(i = 0, j=0; i < strlen(a); i++){
        if(strchr(tmp_a, a[i]) == '\0'){
            *(tmp_a + j) = a[i]; 
            j++;
        }
    }
    for(i = 0, j=0; i < strlen(b); i++){
        if(strchr(tmp_b, b[i]) == '\0'){
            *(tmp_b + j) = b[i]; 
            j++;
        }
    }
    if(strlen(tmp_a) < strlen(tmp_b))
        return 1; 
    else if(strlen(tmp_a) > strlen(tmp_b))
        return -1;
    else 
         return -strcmp(a,b);
}
int sort_by_length(const char* a, const char* b) {
    if(strlen(a) < strlen(b))
        return 1; 
    else if(strlen(a) > strlen(b))
        return -1; 
    else 
        return -strcmp(a,b);
}

void string_sort(char** arr, const int cnt,
                int ( *cmp_func)(const char* , const char* )); 
void string_sort(char **arr, const int cnt, int(*cmp_func)(const char*, const char*)){
    int i, j; 
    char *tmp = (char *)calloc(1024, sizeof(char));
    for(i = 0; i < cnt; i++){
        for(j = i+1; j < cnt; j++){
            if((*cmp_func)(arr[i], arr[j]) < 0){
                char *tmp = arr[i];
                arr[i] = arr[j];
                arr[j] = tmp;
            }
        }
    }
}



int main() 
{
    int n;
    scanf("%d", &n);
  
    char** arr;
	arr = (char**)malloc(n * sizeof(char*));
  
    for(int i = 0; i < n; i++){
        *(arr + i) = malloc(1024 * sizeof(char));
        scanf("%s", *(arr + i));
        *(arr + i) = realloc(*(arr + i), strlen(*(arr + i)) + 1);
    }
  
    string_sort(arr, n, lexicographic_sort);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]);
    printf("\n");

    string_sort(arr, n, lexicographic_sort_reverse);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]); 
    printf("\n");

    string_sort(arr, n, sort_by_length);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]);    
    printf("\n");

    string_sort(arr, n, sort_by_number_of_distinct_characters);
    for(int i = 0; i < n; i++)
        printf("%s\n", arr[i]); 
    printf("\n");
}
