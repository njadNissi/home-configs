#include<stdio.h>

int val(int x){
	printf("Integer: ");
	return x;
}

int val(char x){
	printf("Chars: ");
	return x;
}
int main(){
	printf("%d\n ", val(5));
	printf("%d\n ", val('5'));
}
