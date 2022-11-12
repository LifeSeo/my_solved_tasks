// Заполнить массив рандомно целыми числами, вывести номер индекса и значения каждого элемента.

int[] array = new int[9];
Random rand = new Random();

for (int x = 0; x < array.Length; x++)
{
    array[x] = rand.Next(99);
    Array.Sort(array);

    Console.WriteLine("Индекс элемента массива " + x + " Число в массиве = " + array[x]);
}