// Заполнить массив рандомно целыми числами, вывести номер индекса,
// значения каждого элемента

int[] array = new int[10];
Random num = new Random();

for(int i = 0; i < array.Length; i++)
{
    array[i] = num.Next(55);
    Console.WriteLine("Индекс элемента массива: " + i + " Значение элемента массива: "  + array[i]);
}
