using System.Diagnostics.CodeAnalysis;
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

            string text = File.ReadAllText(@"C:\Users\Borup\C#\AdventOfCode\AdventofCode\Day 8\puzzleinput.txt");

            string[] lines = text.Split("\r\n");

            const int MATRIX_ROWS = 99;
            const int MATRIX_COLOUMNS = 99;

            int[,] array = new int[MATRIX_ROWS, MATRIX_COLOUMNS];

            int answer = MATRIX_ROWS * 2 + MATRIX_COLOUMNS * 2 - 4;

            // convert puzzleinput into a accessible matrix
            for (int i = 0; i < MATRIX_ROWS; i++) {
                for (int j = 0; j < MATRIX_COLOUMNS; j++) {
                    array[i,j] = int.Parse(lines[i][j].ToString());
                }
            }

            bool flag = true;

            // check every instance if it is visible
            for (int i = 1; i < MATRIX_ROWS - 1; i++) { 
                for (int j = 1; j < MATRIX_COLOUMNS - 1; j++) {

                    int counter = 0;
                    flag = true;
                    // check down 
                    for (int k = i + 1; k < MATRIX_ROWS && flag; k++) {
                        if (array[i, j] <= array[k, j]) {
                            flag = false;
                        }
                    }
                    if (flag) {
                        counter++;
                    }
                    else {
                        flag = true;
                    }
                    

                    // problem: if loop fails, then the next loops will never check
                    // problem: 

                    //check up
                    for (int k = 0; k < i && flag; k++) {
                        if (array[i, j] <= array[k, j]) {
                            flag = false;
                        }
                    }
                    if (flag) {
                        counter++;
                    }
                    else {
                        flag = true;
                    }


                    //check right
                    for (int k = j + 1; k < MATRIX_COLOUMNS && flag; k++) {
                        if (array[i, j] <= array[i, k]) {
                            flag = false;
                        }
                    }
                    if (flag) {
                        counter++;
                    }
                    else {
                        flag = true;
                    }
                    

                    //check left
                    for (int k = 0; k < j && flag; k++) {
                        if (array[i, j] <= array[i, k]) {
                            flag = false;
                        }
                    }
                    if (flag) {
                        counter++;
                    }

                    if (counter > 0) {
                        answer++;
                    }

                }
            }

            Console.WriteLine("Answer to part 1: " + answer);

            // DAY 8, PART 2
            // Find the highest possible scenic score

            int biggestScore = 0;

            // iterate through matrix
            for (int i = 1; i < MATRIX_ROWS - 1; i++) {
                for (int j = 1; j < MATRIX_COLOUMNS - 1; j++) {

                    // problem: k is used as counter, but its doesnt start at 0

                    int right = 0, left = 0, up = 0, down = 0;
                    flag = true;
                    int counter = 0;
                    // Look down
                    for (int k = i + 1; k < MATRIX_ROWS && flag; k++) {
                        if (array[i, j] <= array[k, j]) {
                            flag = false;
                            counter++;
                        }
                        else {
                            counter++;
                        }
                    }
                    down = counter;

                    counter = 0;
                    flag = true;
                    // Look up
                    for (int k = i - 1; k >= 0 && flag; k--) {
                        if (array[i, j] <= array[k, j]) {
                            flag = false;
                            counter++;
                        }
                        else {
                            counter++;
                        }
                    }
                    up = counter;

                    flag = true;
                    counter = 0;
                    // Look right
                    for (int k = j + 1; k < MATRIX_COLOUMNS && flag; k++) {
                        if (array[i, j] <= array[i, k]) {
                            flag = false;
                            counter++;
                        }
                        else {
                            counter++;
                        }
                    }
                    right = counter;

                    flag = true;
                    counter = 0;
                    // Look left
                    for (int k = j - 1; k >= 0 && flag; k--) {
                        if (array[i, j] <= array[i, k]) {
                            flag = false;
                            counter++;
                        }
                        else {
                            counter++;
                        }
                    }
                    left = counter;

                    // calculate scenic score and update highest
                    int localScore = right * left * down * up;
                    
                    if (localScore >= biggestScore) {
                        biggestScore = localScore;
                    }

                }
            }

            Console.WriteLine("Answer to Part 2: " + biggestScore);

        }
    }
}