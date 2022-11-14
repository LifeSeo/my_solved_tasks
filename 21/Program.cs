// Найти наибольшее число в массиве с помощью цикла FOR

int[] array = new int[] { 75, 7798, 2573, 76, 685, -570, 4762, 586, -6378, 26 };
int max = 0;

for (int i = 0; i < array.Length; i++)
{
    if (array[i] > max)
    {
        max = array[i];
    }

}
Console.WriteLine(max);
