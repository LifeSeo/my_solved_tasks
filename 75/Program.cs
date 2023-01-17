// Создайте метод для обмена определенных столбцов матрицы
// размера 3 х 4 (порядковые номера столбцов вводятся).

int[,] matrix = new int[3, 4] { { 5, 2, 9, 4 }, { 7, 5, 8, 9 }, { 1, 0, 3, 9 } };

Console.WriteLine("Введите первый столбец для обмена: ");
int firstColumn = Convert.ToInt32(Console.ReadLine());
Console.WriteLine("Введите второй столбец для обмена: ");
int secondColumn = Convert.ToInt32(Console.ReadLine());

void PrintMatrix(int[,] matrix)
{
    for (int i = 0; i < matrix.GetLength(0); i++)
    {
        Console.Write("[");
        for (int j = 0; j < matrix.GetLength(1); j++)
        {
            if (j < matrix.GetLength(1) - 1)
                Console.Write($"{matrix[i, j],4}, ");
            else Console.Write($"{matrix[i, j],4}");
        }
        Console.WriteLine("]");
    }
}

int[,] ChangeMatrix(int[,] matrix, int firstColumn, int secondColumn)
{
    int result = 0;
    int[,] matrixChange = new int[3, 4];
    for (int i = 0; i < matrix.GetLength(0); i++)
    {
        for (int j = 0; j < matrix.GetLength(1) - 1; j++)
        {
            (matrix[i, firstColumn], matrix[i, secondColumn]) = (matrix[i, secondColumn], matrix[i, firstColumn]);
            result = matrix[i, j];
            matrixChange[i, j] = result;
        }
    }
    return matrixChange;
}

PrintMatrix(matrix);
Console.WriteLine();
ChangeMatrix(matrix, firstColumn, secondColumn);
PrintMatrix(matrix);
