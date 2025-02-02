#include<stdio.h>

int main(void){
    int n, m;
    scanf("%d %d", &n, &m);

    int a[n][m];
    int b[n][m];

    for(int i=0; i<n; i++){
        for(int j=0; i<m; j++){
            scanf("%d", &a[i][j]);
        }
    }

    for(int i=0; i<n; i++){
        for(int j=0; i<m; j++){
            scanf("%d", &b[i][j]);
        }
    }

    for(int i=0; i<n; i++){
        for(int j=0; i<m; j++){
            int sum = a[i][j] + b[i][j];
            printf("%d", sum);
        }
        printf("\n");
    }

}