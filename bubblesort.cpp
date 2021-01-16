#include <iostream>
#include <cstdlib>

int* bubble_sort(int array[], int n)
{
  int i, j, temp;
  for(i = 1; i < n; i++)
    for(j = 0; j < n-i; j++)
      if(array[j] > array[j+1])
      {
        temp = array[j]; 
        array[j] = array[j+1]; 
        array[j+1] = temp; 
      }
  return array;
}

void print_array(int* array, int n)
{
  int i;
  for (i = 0; i < n; i++)
    std::cout << array[i] << " - " ;
  std::cout << std::endl;
}

int main() 
{
  int array[5] = {5, 4, 3, 2, 1};

  print_array(array, 5);
  bubble_sort(array, 5);
  print_array(array, 5);
}
