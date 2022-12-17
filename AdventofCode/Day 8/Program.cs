using System.Globalization;

namespace Day_8
{
    // Could also use Lists to make dynamic
    public class MatrixIndex
    {
        public int X { get; set; }
        public int Y { get; set; }
        public int Value { get; set; }
        public MatrixIndex(int x, int y, int value)
        {
            X = x;
            Y = y;
            Value = value;
        }
    }

    internal class Program
    {
        static void Main(string[] args)
        {
            // DAY 8, PART 1
            // How many trees are visible from the edge

            string text = File.ReadAllText(@"C:\Users\Borup\AdventOfCode\AdventofCode\Day 8\puzzleinput.txt");

            string[] lines = text.Split("\r\n");

            const int MATRIX_ROWS = 99;
            const int MATRIX_COLOUMNS = 99;

            int[,] array = new int[MATRIX_ROWS, MATRIX_COLOUMNS];

            for (int i = 0; i < MATRIX_ROWS; i++) {
                for (int j = 0; j < MATRIX_COLOUMNS; j++) {
                    array[i,j] = int.Parse(lines[i][j].ToString());
                }
            }



        }
    }
}