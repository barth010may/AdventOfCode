

using System.Diagnostics.CodeAnalysis;
using System.Runtime.ExceptionServices;

class program 
{
    static void Main(string[] args) 
    {
        // DAY 3, PART 1
        // Find the sum of the item type that appears in both compartments of each rucksack.

        Dictionary<char, int> dictionary = new Dictionary<char, int>()
        {
            {'a', 1}, {'b', 2}, {'c', 3},  
            {'d', 4}, {'e', 5}, {'f', 6},  
            {'g', 7}, {'h', 8}, {'i', 9}, 
            {'j', 10}, {'k', 11}, {'l', 12}, 
            {'m', 13}, {'n', 14}, {'o', 15}, 
            {'p', 16}, {'q', 17}, {'r', 18}, 
            {'s', 19}, {'t', 20}, {'u', 21},  
            {'v', 22}, {'w', 23}, {'x', 24}, 
            {'y', 25}, {'z', 26}, {'A', 27}, 
            {'B', 28}, {'C', 29}, {'D', 30}, 
            {'E', 31}, {'F', 32}, {'G', 33}, 
            {'H', 34}, {'I', 35}, {'J', 36}, 
            {'K', 37}, {'L', 38}, {'M', 39}, 
            {'N', 40}, {'O', 41}, {'P', 42},   
            {'Q', 43}, {'R', 44}, {'S', 45}, 
            {'T', 46}, {'U', 47}, {'V', 48},  
            {'W', 49}, {'X', 50}, {'Y', 51}, 
            {'Z', 52}
        };

        string text = File.ReadAllText(@"C:\Users\Borup\AdventOfCode\AdventofCode\Day 3\puzzleinput.txt");

        string[] lines = text.Split("\r\n");

        int sum = 0;
        bool keepLooping = true;

        foreach (string line in lines) {
            for (int i = 0; i < line.Length / 2 && keepLooping; i++) {

                for (int j = line.Length / 2; j < line.Length; j++) {
                    if (line[i] == line[j]) {
                        sum += dictionary[line[i]];
                        keepLooping = false;
                        break;
                    }
                }
            }
            keepLooping = true;
        }
        Console.WriteLine("The Answer to PART 1: " + sum);

        // DAY 3, PART 2
        // Find the sum of the item type that corresponds to the badges of each three-Elf group.

        keepLooping = true;
        sum = 0;

        for (int k = 0; k < lines.Length; k += 3) {
            for (int i = 0; i < lines[k].Length && keepLooping; i++) {
                for (int j = 0; j < lines[k+1].Length && keepLooping; j++) {
                    if (lines[k][i] == lines[k+1][j]) {
                        for (int x = 0; x < lines[k+2].Length; x++) {
                            if (lines[k][i] == lines[k+2][x]) {
                                sum += dictionary[lines[k][i]];
                                keepLooping = false;
                                break;
                            }
                        }
                    }
                }
            }
            keepLooping = true;
        }

        Console.WriteLine("The Answer to PART 2: " + sum);
    }
}