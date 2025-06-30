#include<stdio.h>
#include<string.h>
int isAnagram(char s1[],char s2[],int n)
{
	int cnt1[26] = {0},cnt2[26]={0};
	int i,pos=0,temp;
	for(i=0;i<n;i++){
		pos = int(s1[i])-65;
		cnt1[pos]+=1;
	}
	for(i=0;i<n;i++){
		pos = int(s2[i])-65;
		cnt2[pos]+=1;
	}
	for(i=0;i<26;i++)
	{
		if(cnt1[i]==cnt2[i] && cnt1[i]!=0 && cntt2!=0 )
		temp++;
	}
	if(temp==n)
	return 1;
	return -1;
}
void main()
{
	int n;
	printf("Enter the size of the string: ");
	scanf("%d",&n);
	char a1[n],a2[n];
	printf("Enter the first string: ");
	scanf("%s",a1);
	printf("Enter the second string: ");
	scanf("%s",a2);
	int res= isAnagram(a1,a2,n);
	if(res == 1)
	printf("TRUE");
	else
	printf("FALSE");
}
