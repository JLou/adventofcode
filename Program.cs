using aoc;


var days = new IDay[24]
{
new Day01(),
new Day02(),
new Day03(),
new Day04(),
new Day05(),
new Day06(),
new Day07(),
new Day08(),
new Day09(),
new Day10(),
new Day11(),
new Day12(),
new Day13(),
new Day14(),
new Day15(),
new Day16(),
new Day17(),
new Day18(),
new Day19(),
new Day20(),
new Day21(),
new Day22(),
new Day23(),
new Day24()
};

int dayWanted = 1;
if (args.Length == 0 || !int.TryParse(args[0], out dayWanted) || dayWanted < 1 || dayWanted > 24)
{
    Console.WriteLine("Invalid day, fallback to 1");
    dayWanted = 1;
}

var lines = File.ReadAllLines("./input/" + dayWanted.ToString().PadLeft(2, '0') + ".txt");
var sampleLines = File.ReadAllLines("./samples/" + dayWanted.ToString().PadLeft(2, '0') + ".txt");

var d = days[dayWanted - 1];
var (part1S, part2S) = d.Compute(sampleLines);
var (part1, part2) = d.Compute(lines);
Console.WriteLine();
Console.WriteLine();

Console.WriteLine("-------------- SAMPLE ------------------");
Console.WriteLine("part1 = " + part1S);
Console.WriteLine("part2 = " + part2S);
Console.WriteLine("-------------- END SAMPLE --------------");
Console.WriteLine();
Console.WriteLine();

Console.WriteLine("---------- PERSONAL RESULT -------------");
Console.WriteLine("part1 = " + part1);
Console.WriteLine("part2 = " + part2);
Console.WriteLine("-------- END PERSONAL RESULT -----------");

Console.WriteLine();
Console.WriteLine();
