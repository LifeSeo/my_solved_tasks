// Сделать реверс элементов главной и дополнительной диагонали в 2-х мерной матрице

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

int[,] DiagonalReverse(int[,] matrix)
{
    for (int i = 0; i < matrix.GetLength(0); i++)
    {
        for (int j = 0; j < matrix.GetLength(1)/2; j++)
        {
            int temp = matrix[i, j];
            matrix[i, j] = matrix[matrix.GetLength(0)-1-i,matrix.GetLength(1)-1-j];
            matrix[matrix.GetLength(0)-1-i,matrix.GetLength(1)-1-j] = temp;
        }
            
    }
    return matrix;
}
int[,] matrix = CreateMatrixRndInt(5, 5, 1, 21);
PrintMatrix(matrix);
Console.WriteLine();
int[,] diagonalReverse = DiagonalReverse(matrix);
PrintMatrix(diagonalReverse);
