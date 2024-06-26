#include<stdio.h>
struct students{
    int id;
    float percentile;
    char name[50];
};
int main(){
    int i;
    struct students e1,e2,e3;
    e1.id = 43;
    e2.id = 44;
    e1.percentile = 56.67;
    e2.percentile = 89.99;
    strcpy(e1.name, "Tirth");
    // e2.name = "Harry";
    printf("the id of the first student = %d\n", e1.id);
    // printf("the name of the student = %s\n");
    printf("the name of the student = %s\n", e1.name);
    



    return 0;
}