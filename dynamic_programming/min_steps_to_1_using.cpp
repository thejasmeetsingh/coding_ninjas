int countStepsToOneHelper(int n, int *arr)
{
	if (n == 1)
       return 0;
    
    if (arr[n] != -1)
       return arr[n];
 
    int res = countStepsToOneHelper(n-1, arr);
 
    if (n % 2 == 0) {
        res = min(res, countStepsToOneHelper(n / 2, arr));
    }
    
    if (n % 3 == 0) {
        res = min(res, countStepsToOneHelper(n / 3, arr));
    }
 
    arr[n] = 1 + res;
    return arr[n];
}

int countStepsToOne(int n) {
    int arr[n+1];
 
    for (int i=0; i<=n; i++)
        arr[i] = -1;
 
    return countStepsToOneHelper(n, arr);
}
