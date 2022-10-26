#include<stdio.h>
int main()
{
  int num;
  printf("Enter any number:");
  scanf("%d",&num);
  if(num%2==0){
    printf("Entered number is an even number.");
  }
  else{
    printf("Entered number is a odd number.");
  }
  return 0;
}
