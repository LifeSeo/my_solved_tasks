// Отсортировать массив по возрастанию.

void PrintArray(int[] array)
{
    Console.Write("[");
    for (int i = 0; i < array.Length; i++)
    {
        if (i < array.Length - 1) Console.Write($"{array[i]}, ");
        else Console.Write($"{array[i]}");
    }
    Console.WriteLine("]");
}

int[] CreateArrayRndInt(int size, int min, int max)
{
    int[] arr = new int[size];
    Random rnd = new Random();

    for (int i = 0; i < arr.Length; i++)
    {
        arr[i] = rnd.Next(min, max + 1);
    }
    return arr;
}

int[] SortingArray(int[] array)
{
    for (int i = 0; i < array.Length; i++)
    {
        for (int j = 0; j < array.Length-1; j++)

        {
            
            if (array[j] > array[j+1])
            {
            int temp = array[j];
            array[j] = array[j+1];
            array[j+1] = temp;
            }
        }
    }
    return array;
}
int[] array = CreateArrayRndInt(10, 1, 25);
PrintArray(array);
int[] sortingArray = SortingArray(array);
PrintArray(sortingArray);
