namespace aoc
{
    public class Day11 : IDay
    {
        public (string, string) Compute(string[] input)
        {
            var grid = input.Select(line => line.Select(c => Convert.ToInt32(c.ToString())).ToArray()).ToArray();

            var flashes = 0;
            var syncStep = 0;
            for (int i = 0; i < 1000; i++)
            {
                for (int y = 0; y < grid.Length; y++)
                {
                    for (int x = 0; x < grid[y].Length; x++)
                    {
                        grid[y][x]++;
                    }
                }

                var flashPoints = new HashSet<(int, int)>();
                for (int y = 0; y < grid.Length; y++)
                {
                    for (int x = 0; x < grid[y].Length; x++)
                    {
                        if (grid[y][x] > 9)
                        {
                            Illuminate(grid, y, x, flashPoints);
                        }
                    }
                }

                for (int y = 0; y < grid.Length; y++)
                {
                    for (int x = 0; x < grid[y].Length; x++)
                    {
                        if (grid[y][x] > 9)
                        {
                            grid[y][x] = 0;
                        }
                    }
                }


                flashes += flashPoints.Count;

                if (flashPoints.Count == grid.Length * grid[0].Length)
                {
                    syncStep = i + 1;
                    break;
                }
            }

            return ($"{flashes}", $"{syncStep}");
        }

        private void Illuminate(int[][] grid, int y, int x, HashSet<(int, int)> flashPoints)
        {
            if (!flashPoints.Contains((x, y)))
            {
                flashPoints.Add((x, y));
                foreach (var (nx, ny) in GetNeighbours(x, y, grid[0].Length, grid.Length))
                {
                    grid[ny][nx]++;
                    if (grid[ny][nx] > 9)
                    {
                        Illuminate(grid, ny, nx, flashPoints);
                    }
                }
            }

        }

        private IEnumerable<(int, int)> GetNeighbours(int x, int y, int xMax, int yMax)
        {

            var potentials = new[]
            {
                (x - 1, y - 1),
                (x, y - 1),
                (x + 1, y- 1),
                (x - 1, y),
                (x + 1, y),
                (x - 1, y + 1),
                (x, y + 1),
                (x + 1, y + 1),
            };

            return potentials.Where(coord => coord.Item1 >= 0 && coord.Item2 >= 0 && coord.Item1 < xMax && coord.Item2 < yMax);
        }

        private void PrintGrid(int[][] grid)
        {
            Console.WriteLine();
            foreach (var row in grid)
            {
                Console.WriteLine(string.Join("", row));
            }
            Console.WriteLine();
            Console.WriteLine();

        }
    }
}