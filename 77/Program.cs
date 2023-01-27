// Задача 59: Задайте двумерный массив из целых чисел.
// Напишите программу, которая удалит строку и столбец, на
// пересечении которых расположен наименьший элемент
// массива

int[,] CreateMatrixRndInt(int rows, int columns, int min, int max)
{
    int[,] matrix = new int[rows, columns];
    Random rnd = new Random();

    for (int i = 0; i < matrix.GetLength(0); i++)
    {
        for (int j = 0; j < matrix.GetLength(1); j++)
        {
            matrix[i, j] = rnd.Next(min, max + 1);
            // TODO: вывести индексы массива.
            // matrix[i, j] = i * 10 + j;
        }
    }
    return matrix;
}

void PrintMatrix(int[,] matrix, string beginRow, string separatorElems, string endRow)
{
    for (int i = 0; i < matrix.GetLength(0); i++)
    {
        Console.Write(beginRow);
        for (int j = 0; j < matrix.GetLength(1); j++)
        {
            if (j < matrix.GetLength(1) - 1)
                Console.Write($"{matrix[i, j],4}{separatorElems}");
            else Console.Write($"{matrix[i, j],4}");
        }
        Console.WriteLine(endRow);
    }
}

void RowColumnIndexMinElem(int[,] matrix, out int indexRow, out int indexColumn)
{
    int rows = matrix.GetLength(0);
    int columns = matrix.GetLength(1);
    int min = matrix[0, 0];
    indexRow = 0;
    indexColumn = 0;
    for (int i = 0; i < rows; i++)
    {
        for (int j = 0; j < columns; j++)
        {
            if (matrix[i, j] < min)
            {
                min = matrix[i, j];
                indexRow = i;
                indexColumn = j;
            }
        }
    }
}

int[,] DeleteRowColumnsMatrix(int[,] matrix, int indexRow, int indexColumn)
{
    int rows = matrix.GetLength(0);
    int columns = matrix.GetLength(1);
    int[,] matrix2 = new int[rows - 1, columns - 1];
    for (int i = 0, m = 0; i < rows - 1; i++, m++)
    {
        if (m == indexRow) m++;
        for (int j = 0, n = 0; j < columns - 1; j++, n++)
        {
            if (n == indexColumn) n++;
            matrix2[i, j] = matrix[m, n];
        }
    }
    return matrix2;
}

int[,] matrix1 = CreateMatrixRndInt(4, 4, 1, 50);
PrintMatrix(matrix1, "", "", "");
Console.WriteLine();
int rowIndex1, columnIndex1;
RowColumnIndexMinElem(matrix1, out rowIndex1, out columnIndex1);
Console.WriteLine($"Минимальное число - {matrix1[rowIndex1,columnIndex1]}");
Console.WriteLine();
int[,] matrix3 = DeleteRowColumnsMatrix(matrix1, rowIndex1, columnIndex1);
PrintMatrix(matrix3, "", "", "");
