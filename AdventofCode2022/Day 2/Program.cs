using System.Reflection.PortableExecutable;
using System.Security.Cryptography.X509Certificates;

namespace Day_2 {
    public enum points {
        A = 1,
        B = 2,
        C = 3,
        Rock = 1,
        Paper = 2,
        Scissor = 3,
    };
    internal class Program {
        static void Main(string[] args) {

            // Day 2, Part 1
            // Final the total score of the given strategy guide

            string text = File.ReadAllText(@"C:\Users\Borup\AdventOfCode\AdventofCode\Day 2\puzzleinput.txt");

            string[] subs = text.Split("\r\n");

            int sum = 0;

            foreach (string sub in subs) {
                switch (sub) {
                    case "A X":
                        sum += (int)points.Rock + 3;
                        break;
                    case "A Y":
                        sum += (int)points.Paper + 6;
                        break;
                    case "A Z":
                        sum += (int)points.Scissor;
                        break;
                    case "B X":
                        sum += (int)points.Rock;
                        break;
                    case "B Y":
                        sum += (int)points.Paper + 3;
                        break;
                    case "B Z":
                        sum += (int)points.Scissor + 6;
                        break;
                    case "C X":
                        sum += (int)points.Rock + 6;
                        break;
                    case "C Y":
                        sum += (int)points.Paper;
                        break;
                    case "C Z":
                        sum += (int)points.Scissor + 3;
                        break;
                    default:
                        break;
                }
            }

            Console.WriteLine("Answer is: " + sum);

            // DAY 2, PART 2
            // Find the total score of the given strategy guide, but with a different scoring system

            sum = 0;

            foreach (string sub in subs) {
                switch (sub) {
                    case "A X":
                        sum += (int)points.Scissor;
                        break;
                    case "A Y":
                        sum += (int)points.Rock + 3;
                        break;
                    case "A Z":
                        sum += (int)points.Paper + 6;
                        break;
                    case "B X":
                        sum += (int)points.Rock;
                        break;
                    case "B Y":
                        sum += (int)points.Paper + 3;
                        break;
                    case "B Z":
                        sum += (int)points.Scissor + 6;
                        break;
                    case "C X":
                        sum += (int)points.Paper;
                        break;
                    case "C Y":
                        sum += (int)points.Scissor + 3;
                        break;
                    case "C Z":
                        sum += (int)points.Rock + 6;
                        break;
                    default:
                        break;
                }
            }

            Console.WriteLine("Answer to Part 2: " + sum);



        }
    }
}