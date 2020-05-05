#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct triangle
{
	int a;
	int b;
	int c;
};

typedef struct triangle triangle;
double *volume_triangle(triangle * tr, int n){
    double *tmp_vols = malloc(n*sizeof(double)); 
    for(int i = 0; i < n; i++){
        double p = (double)((tr[i].a) + (tr[i].b) + (tr[i].c)) / 2;
        tmp_vols[i] = sqrt(p * (p - tr[i].a) * (p - tr[i].b) * (p - tr[i].c)); 
    }
    return tmp_vols;
}


void sort_by_area(triangle* tr, int n) {
    double *vols = malloc(n * sizeof(double));
    vols = volume_triangle(tr,n); 
    int i, k; 
    double tmpVol; 
    triangle tmp; 
    for(i = 0; i < n; i++){
        for(k = i + 1; k < n; k++){
            if(vols[k] < vols[i]){
                tmpVol = vols[i]; 
                vols[i] = vols[k]; 
                vols[k] = tmpVol; 
                tmp = tr[i]; 
                tr[i] = tr[k]; 
                tr[k] = tmp; 
            }
        }
    }
}

int main()
{
	int n;
	scanf("%d", &n);
	triangle *tr = malloc(n * sizeof(triangle));
	for (int i = 0; i < n; i++) {
		scanf("%d%d%d", &tr[i].a, &tr[i].b, &tr[i].c);
	}
	sort_by_area(tr, n);
	for (int i = 0; i < n; i++) {
		printf("%d %d %d\n", tr[i].a, tr[i].b, tr[i].c);
	}
	return 0;
}
