var lines = File.ReadAllLines("./input/1.txt").Select(l => int.Parse(l)).ToList();


int CountIncreases(IEnumerable<int> l)
{

    var prev = int.MaxValue;
    var count = 0;

    foreach (var line in l)
    {
        if (line > prev)
        {
            count++;
        }
        prev = line;
    }

    return count;
}

int[] groups = new int[lines.Count() - 2];


for (int i = 0; i < lines.Count(); i++)
{
    if (i < lines.Count() - 2) groups[i] += lines[i];
    if (i - 1 >= 0 && i - 1 < lines.Count() - 2) groups[i - 1] += lines[i];
    if (i - 2 >= 0 && i < lines.Count()) groups[i - 2] += lines[i];
}
Console.WriteLine(CountIncreases(lines));
Console.WriteLine(CountIncreases(groups));

