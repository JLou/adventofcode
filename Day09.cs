namespace aoc;

public class Day09 : IDay
{
    public (string, string) Compute(string[] input)
    {
        var map = input.Select(line => line.Select(x => int.Parse(x.ToString())).ToArray()).ToArray();

        int xMax = map[0].Length;
        int yMax = map.Length;

        var lowPoints = new List<int>();
        var lowPointsCoord = new List<(int x, int y)>();
        for (int y = 0; y < yMax; y++)
        {
            for (int x = 0; x < xMax; x++)
            {
                if (GetNeighbours(x, y, xMax, yMax).All(coord => map[coord.y][coord.x] > map[y][x]))
                {
                    lowPoints.Add(map[y][x]);
                    lowPointsCoord.Add((x, y));
                }
            }
        }

        var basins = new List<int>();

        foreach (var (x, y) in lowPointsCoord)
        {
            var basin = new HashSet<(int, int)> { (x, y) };
            (int x, int y)[] higherNeighbours = new (int x, int y)[] { (x, y) };
            do
            {
                higherNeighbours = higherNeighbours
                    .SelectMany(coord => GetNeighbours(coord.x, coord.y, xMax, yMax).Where(neighCoord =>
                           map[neighCoord.y][neighCoord.x] > map[coord.y][coord.x]
                        && map[neighCoord.y][neighCoord.x] < 9))
                    .ToArray();
                ;
                basin = new(basin.Union(higherNeighbours));

            } while (higherNeighbours.Length > 0);
            basins.Add(basin.Count);
        }

        var risk1 = lowPoints.Select(x => x + 1).Sum();
        var risk2 = basins.OrderByDescending(x => x).Take(3).Aggregate(1, (acc, next) => acc * next);
        return ($"{risk1}", $"{risk2}");
    }
    private IEnumerable<(int x, int y)> GetNeighbours(int x, int y, int xMax, int yMax)
    {
        if (x > 0) yield return (x - 1, y);
        if (y > 0) yield return (x, y - 1);
        if (x < xMax - 1) yield return (x + 1, y);
        if (y < yMax - 1) yield return (x, y + 1);
    }
}
