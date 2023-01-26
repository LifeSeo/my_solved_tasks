// Задать координаты 3-х точек (a, b, c). Создать цикл со смещением в 1 для каждой точки с увеличением. Вывести на консоль рисунок всех заданых координат (a, b, c), каждый массив точек разного цвета

using System;
class Program{
    static void Main()
{
Console.Clear();
int xa = 5, ya = 1, xb = 10, yb = 1, xc = 15, yc = 1;
int count = 0;

while(count < 10)
{
xa = xa + 1;
ya = ya + 1;
xb = xb + 1;
yb = yb + 1;
xc = xc + 1;
yc = yc + 1;
count++;
Console.ForegroundColor = ConsoleColor.White;
Console.SetCursorPosition(xa,ya);
Console.WriteLine("+");
Console.ForegroundColor = ConsoleColor.Blue;
Console.SetCursorPosition(xb,yb);
Console.WriteLine("+");
Console.ForegroundColor = ConsoleColor.Red;
Console.SetCursorPosition(xc,yc);
Console.WriteLine("+");
} 
    }
  }
    
