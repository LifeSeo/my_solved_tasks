// Составить программу вывода на экран числа, вводимого с клавиатуры. Выводимому числу должно предшествовать сообщение «Вы ввели число».

Console.WriteLine("Введите число: ");
int number = Convert.ToInt16(Console.ReadLine());

Console.Write("Вы ввели число: ");
Console.WriteLine(number);
