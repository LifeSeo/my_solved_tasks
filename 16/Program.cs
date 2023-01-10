// Указать порядковый номер в массиве и вывести соответствующее ему целое число
// Порядковый номер вводит пользователь

int[] array = {46, 89, 98, 3425, 809, 870};
Console.WriteLine("Номер индекса из массива: ");
int x = Convert.ToInt32(Console.ReadLine());
Console.Write("Это число: ");
Console.WriteLine(array[x]);
