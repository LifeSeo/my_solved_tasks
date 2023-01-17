// Дан двумерный массив. Найти:
// число пар одинаковых соседних элементов в каждой строке;
// int[,] matrix = new int[4, 2] { { 5, 2 }, { 7, 9 }, { 3, 9 }, { 4, 9 } };

void PrintMatrix(int[,] matrix)

{
    for (int i = 0; i < matrix.GetLength(0); i++)
    {
        Console.Write("[");
        for (int j = 0; j < matrix.GetLength(1); j++)
        {
            if (j < matrix.GetLength(1) - 1) Console.Write($"{matrix[i, j],4}, ");
            else Console.Write($"{matrix[i, j],4} ");
        }
        Console.WriteLine("]");
    }
}
int[,] CreateMatrixRndInt(int rows, int columns, int min, int max)
{
    int[,] matrix = new int[rows, columns];
    Random rnd = new Random();

    for (int i = 0; i < matrix.GetLength(0); i++)
    {
        for (int j = 0; j < matrix.GetLength(1); j++)
        {
            matrix[i, j] = rnd.Next(min, max + 1);
        }
    }
    return matrix;
}

int SummaParMatrix(int[,] matrix)
{
    int count = 0;
    for (int i = 0; i < matrix.GetLength(0); i++)
    {
        for (int j = 0; j < matrix.GetLength(1) - 1; j++)
        {

            if (matrix[i, j] == matrix[i, j + 1])
                count++;
        }
    }
    return count;
}

int[,] matrix = CreateMatrixRndInt(25, 25, 1, 10);
PrintMatrix(matrix);
int result = SummaParMatrix(matrix);
Console.WriteLine(result);
