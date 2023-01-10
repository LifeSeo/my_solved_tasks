// Найдём элемент массива, совпадающий с некоторым значением,
// который определяет пользователь.

int[] array = { 45, 67, 12, 56, 456, 76, 99, 678, 9869 };
int n = array.Length;
int find = 99;
int index = 0;

while (index < n)
{
    if (array[index] == find)
    
    {
        Console.WriteLine(index);
        break;
    }
    else
    {
        index++;
    }
}
