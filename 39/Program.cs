// Вычисли периметр треугольника по координатам в 2D плоскости.
// Координаты вводит пользователь

Console.Write("Введите точку XA: ");
int xa = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите точку YA: ");
int ya = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите точку XB: ");
int xb = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите точку YB: ");
int yb = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите точку XA: ");
int xc = Convert.ToInt32(Console.ReadLine());
Console.Write("Введите точку YA: ");
int yc = Convert.ToInt32(Console.ReadLine());

double Perimetor(double xa, double ya, double xb, double yb, double xc, double yc)
{
    double a = (xa - xb) * (xa - xb);
    double b = (ya - yb) * (ya - yb);
    double c = (xb - xc) * (xb - xc);
    double d = (yb - xc) * (yb - xc);
    double e = (xc - xa) * (xc - xa);
    double f = (yc - ya) * (yc - ya);
    double piece1 = Math.Sqrt(a + b);
    double piece2 = Math.Sqrt(c + d);
    double piece3 = Math.Sqrt(e + f);
    double perimetor = piece1 + piece2 + piece3;
    return perimetor;
}

double result = Perimetor(xa, ya, xb, yb, xc, yc);
double finalResult = Math.Round(result, 2, MidpointRounding.ToZero); 
Console.WriteLine($"Периметр треугольника = > {finalResult}");
