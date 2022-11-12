// Заполнить массив рандомно целыми числами, вывести номер индекса,
// значения каждого элемента

int[] array = new int[9];
Random num = new Random();

for (int index = 0; index < array.Length; index++)
{
    array[index] = num.Next(99);
    Console.WriteLine("Индекс элемента массива " + index + " Число в массиве = " + array[index]);
    
}