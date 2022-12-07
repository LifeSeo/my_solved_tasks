// Задача 58: Задайте две матрицы. Напишите программу,
// которая будет находить произведение двух матриц.
// Например, даны 2 матрицы:
// 2 4 | 3 4
// 3 2 | 3 3
// Результирующая матрица будет:
// 18 20
// 15 18

int[,] NewRndMatrix(int rows, int columns, int minElement, int maxElement)
{
    int[,] matrix = new int[rows, columns];
    Random rnd = new Random();

    for (int i = 0; i < matrix.GetLength(0); i++)
    {
        for (int j = 0; j < matrix.GetLength(1); j++)
        {
            matrix[i, j] = rnd.Next(minElement, maxElement + 1);
        }
    }
    return matrix;
}

int[,] NewRndMatrix2(int rows, int columns, int minElement, int maxElement)
{
    int[,] matrix2 = new int[rows, columns];
    Random rnd = new Random();

    for (int i = 0; i < matrix2.GetLength(0); i++)
    {
        for (int j = 0; j < matrix2.GetLength(1); j++)
        {
            matrix2[i, j] = rnd.Next(minElement, maxElement + 1);
        }
    }
    return matrix2;
}

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

bool CheckMatrix(int[,] matrix, int[,] matrix2)
{
    return (matrix.GetLength(1) == matrix2.GetLength(0));
}

int[,] MultiplyTwoMatrix(int[,] matrix, int[,] matrix2)
{
    int[,] multiplyTwoMatrix = new int[matrix.GetLength(0), matrix2.GetLength(1)];
    if (CheckMatrix(matrix, matrix2) == true)
    {
        for (int i = 0; i < multiplyTwoMatrix.GetLength(0); i++)
        {
            for (int j = 0; j < multiplyTwoMatrix.GetLength(1); j++)
            {
                multiplyTwoMatrix[i, j] = 0;
                for (int k = 0; k < matrix.GetLength(1); k++)
                {
                    multiplyTwoMatrix[i, j] += matrix[i, k] * matrix2[k, j];
                }
            }
        }

    }
    return multiplyTwoMatrix;
}

Console.WriteLine("Первая матрица");
int[,] matrix = NewRndMatrix(3, 6, 1, 9);
PrintMatrix(matrix);
Console.WriteLine();
Console.WriteLine("Вторая матрица");
int[,] matrix2 = NewRndMatrix2(6, 3, 1, 9);
PrintMatrix(matrix2);
Console.WriteLine();
Console.WriteLine(@CheckMatrix(matrix, matrix2) ? "Результат перемножения матриц"
: "Условия не соблюдаются, умножение невозможно");
Console.WriteLine();
int[,] multiplyTwoMatrix = MultiplyTwoMatrix(matrix, matrix2);
PrintMatrix(multiplyTwoMatrix);





