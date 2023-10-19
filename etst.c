// write binary search in c

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 100

int binary_search(int *arr, int size, int key)
{
    int low = 0;
    int high = size - 1;
    int mid = 0;

    while (low <= high)
    {
        mid = (low + high) / 2;
        if (arr[mid] == key)
            return mid;
        else if (arr[mid] > key)
            high = mid - 1;
        else
            low = mid + 1;
    }
    return -1;
}