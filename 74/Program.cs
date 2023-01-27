// Дан двумерный массив. Определить какие элементы повторяются в строке
// и вывести их в виде массива

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

int[] DifferentElementsMatrixRows(int[,] matrix)
{
    int[] ResultDifferentElementsMatrix = new int[matrix.GetLength(0)];

    for (int i = 0; i < matrix.GetLength(0); i++) // каждая строка
    {
        int elements = 0;
        for (int j = 0; j < matrix.GetLength(1); j++) // каждый элемент
        {
            for (int k = j+1; k < matrix.GetLength(0); k++) // каждый элемент, что правее
            {
                if (matrix[i, j] == matrix[i, k])
                    elements = matrix[i, j];
            }
        }
        ResultDifferentElementsMatrix[i] = elements;
    }
    return ResultDifferentElementsMatrix;
}

void PrintArray(int[] arr)
{
    Console.Write("[");
    for (int i = 0; i < arr.Length; i++)
    {
        if (i < arr.Length - 1) Console.Write($"{arr[i]}, ");
        else Console.Write($"{arr[i]}");
    }
    Console.WriteLine("]");
}

int[,] matrix = NewRndMatrix(5, 5, 1, 10);
PrintMatrix(matrix);
int[] array = DifferentElementsMatrixRows(matrix);
PrintArray(array);
