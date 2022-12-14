using System.ComponentModel.Design;
using System.Diagnostics.Metrics;
using System.Security;

namespace Day_7
{
    internal class Program
    {

        static void Main(string[] args)
        {

            string text = File.ReadAllText(@"C:\Users\Borup\AdventOfCode\AdventofCode\Day 7\puzzleinput.txt");

            string[] lines = text.Split("\r\n");

            // DAY 7, PART 1
            // Find the sum of all the directories that contain up to 100.000 bytes

            int counter = 0;

            CreateFileSystem();

            //FindSumOfDirs();

            // DAY 7, PART 2
            // Find the total memory of the smallest directory that would free up enough space for a 3 mil update

            FindSmallestPossibleDirectory();

            void FindSmallestPossibleDirectory()
            {
                Directory.SetCurrentDirectory(@"C:\Users\Borup\AdventOfCode\AdventofCode\Day 7\main");

                string[] directories = Directory.GetDirectories(Directory.GetCurrentDirectory());

                List<string> directoryList = new List<string>();

                int sum = 0;
                int totalsum = 0;

                // find all the directories which contain 100000 bytes 
                foreach (string directory in directories)
                {
                    totalsum = WalkDirectoryTree(directory, directoryList);
                }
            }

            void FindSumOfDirs()
            {
                Directory.SetCurrentDirectory(@"C:\Users\Borup\AdventOfCode\AdventofCode\Day 7\main");

                string[] directories = Directory.GetDirectories(Directory.GetCurrentDirectory());

                List<string> directoryList = new List<string>();

                int sum = 0;
                int totalsum = 0;

                // find all the directories which contain 100000 bytes 
                foreach (string directory in directories)
                {
                    totalsum = WalkDirectoryTree(directory, directoryList);  
                }
                foreach (string dir in directoryList)
                {
                    Console.WriteLine(dir);
                    string[] files = Directory.GetFiles(dir,"*", SearchOption.AllDirectories);
                    foreach (string file in files)
                    {
                        string fileName = Path.GetFileName(file);
                        string[] substrings = fileName.Split(' ');
                        int number = int.Parse(substrings[0]);

                        sum += number;
                    }

                }
                Console.WriteLine("Total Sum : " + sum);

            }

            int WalkDirectoryTree(string dir, List<string> directoryList)
            {

                Directory.SetCurrentDirectory(dir);

                string[] files = Directory.GetFiles(Directory.GetCurrentDirectory());
                    
                int localsum = 0;

                // iterate through files in working directory
                foreach (string file in files)
                {
                    string fileName = Path.GetFileName(file);
                    if (fileName.Split(' ') != null)
                    {
                        string[] substrings = fileName.Split(' ');
                        int number = int.Parse(substrings[0]);

                        localsum += number;
                    }
                }

                // check for subdirectories and iterate process on them
                string[] subdirs = Directory.GetDirectories(Directory.GetCurrentDirectory());
                
                if (subdirs != null)
                {
                    foreach (string subdir in subdirs)
                    {
                        localsum += WalkDirectoryTree(subdir, directoryList);
                    }
                }

                if (localsum <= 100000)
                {
                    directoryList.Add(Directory.GetCurrentDirectory());
                }

                return localsum;
            }


            void CreateFileSystem()
            {
                Directory.SetCurrentDirectory(@"C:\Users\Borup\AdventOfCode\AdventofCode\Day 7");
                foreach (string line in lines)
                {
                    if (line.StartsWith("$"))
                    {
                        // command found
                        if (line.Contains("cd .."))
                        {
                            Directory.SetCurrentDirectory(Directory.GetParent(Directory.GetCurrentDirectory()).FullName);
                        }
                        else if (line.Contains("cd"))
                        {
                            // Create new Directory if one doesnt exist
                            string[] substring = line.Split(" ");
                            var directory = Directory.CreateDirectory(Directory.GetCurrentDirectory() + $@"\{substring[2]}");

                            // change into new directory
                            Directory.SetCurrentDirectory(directory.FullName);
                        }
                        else
                        {
                            // list all files
                        }
                    }
                    else if (line.StartsWith("dir"))
                    {
                        // directory found
                        string[] substring = line.Split(" ");
                        Directory.CreateDirectory(Directory.GetCurrentDirectory() + $@"\{substring[1]}");
                    }
                    else
                    {
                        // file found
                        string pathString = Path.Combine(Directory.GetCurrentDirectory(), line);

                        File.Create(pathString);
                    }
                }
            }
        }
    }
}