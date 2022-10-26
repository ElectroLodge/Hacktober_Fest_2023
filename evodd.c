#include<stdio.h>
#include<stdlib.h>
int main()
{
    int n,t;
    printf("Enter a number of your choice : ");
    scanf("%d",&n);
    if(n%2==0)
    printf("The entered number id EVEN.\n");
    else
    printf("The entered number id ODD.\n");
    printf("To terminate the code ENTER '0' \n");
    scanf("%d",&t);
    if(t==0)
    exit(0);
    else
    main();
}
