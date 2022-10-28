#include<stdio.h>
#include<stdlib.h>
int main()
{
    int lb,ub,i,sum=0,t;
    printf("Enter the lower bound : ");
    scanf("%d",&lb);
    printf("\nEnter the upper bound : ");
    scanf("%d",&ub);
    for(i=lb;i<=ub;i++)
    {
        if(i%2==1)
        sum+=i;
    }
    printf("\nThe Sum of ODD numbers from %d to %d is : %d",lb,ub,sum);
    printf("\nTo terminate the code ENTER '0' \n");
    scanf("%d",&t);
    if(t==0)
    {
        exit(0);
    }
    else
    main();
    return 0;
}
