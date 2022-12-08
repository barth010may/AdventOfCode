using System.Reflection.PortableExecutable;
using System.Security.Cryptography.X509Certificates;

namespace Day_2 {
    public enum points {
        A = 1,
        B = 2,
        C = 3,
        X = 1,
        Y = 2,
        Z = 3,
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
                        sum += (int)points.X + 3;
                        break;
                    case "A Y":
                        sum += (int)points.Y + 6;
                        break;
                    case "A Z":
                        sum += (int)points.Z;
                        break;
                    case "B X":
                        sum += (int)points.X;
                        break;
                    case "B Y":
                        sum += (int)points.Y + 3;
                        break;
                    case "B Z":
                        sum += (int)points.Z + 6;
                        break;
                    case "C X":
                        sum += (int)points.X + 6;
                        break;
                    case "C Y":
                        sum += (int)points.Y;
                        break;
                    case "C Z":
                        sum += (int)points.Z + 3;
                        break;
                    default:
                        break;
                }
            }

            Console.WriteLine("Answer is: " + sum);


        }
    }
}