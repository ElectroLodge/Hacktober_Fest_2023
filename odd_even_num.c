#include<stdio.h>
int main(){
  int num;
  printf("enter any num :");
  scanf("%d",&num);
  if(num%2==0){
    printf("Entered num is even number.");
  }
  else{
    printf("entered num is odd number.");
  }
  return 0;
}
