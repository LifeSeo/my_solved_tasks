// Составить программу вывода на экран в одну строку четырех любых чисел с тремя пробелами между ними.

int a = new Random().Next(1,123);
int b = new Random().Next(4,667);
int c = new Random().Next(12,90);
int d = new Random().Next(56,99);
Console.WriteLine($"{a}   {b}   {c}   {d}");