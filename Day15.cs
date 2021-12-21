namespace aoc
{
    public class Day15 : IDay
    {

        public (string, string) Compute(string[] input)
        {
            var map = input.Select(x => x.Select(y => Convert.ToInt32(y.ToString())).ToArray()).ToArray();

            var map2 = new int[map.Length * 5][];
            for (var y = 0; y < map.Length * 5; y++)
            {
                map2[y] = new int[map[0].Length * 5];
                for (int x = 0; x < map.Length * 5; x++)
                {
                    var value = map[y % map.Length][x % map[0].Length] + x / map[0].Length + y / map.Length;
                    if (value > 9)
                    {
                        value %= 9;
                    }
                    map2[y][x] = value;
                }
            }
            int c = ComputeMap(map);
            int c2 = Djikstra(map2);

            return ($"{c}", $"{c2}");
        }

        private int ComputeMap(int[][] map)
        {
            int[][] pathValues = new int[map.Length][];

            for (int y = map.Length - 1; y >= 0; y--)
            {
                pathValues[y] = new int[map[0].Length];
                for (int x = map[0].Length - 1; x >= 0; x--)
                {
                    pathValues[y][x] = FindShortestPath(x, y, map, pathValues);
                }
            }
            var c = pathValues[0][0] - map[0][0];


            return c;
        }

        private int FindShortestPath(int xStart, int yStart, int[][] map, int[][] weights)
        {
            if (xStart == map[0].Length - 1 && yStart == map.Length - 1)
            {
                return map[yStart][xStart];
            }
            else if (xStart == map[0].Length - 1)
            {
                return map[yStart][xStart] + weights[yStart + 1][xStart];
            }
            else if (yStart == map[0].Length - 1)
            {
                return map[yStart][xStart] + weights[yStart][xStart + 1];
            }
            else
            {
                var path1 = weights[yStart + 1][xStart];
                var path2 = weights[yStart][xStart + 1];
                return map[yStart][xStart] + Math.Min(path2, path1);
            }
        }

        private int Djikstra(int[][] map)
        {

            Dictionary<(int, int), int> distance = new();
            var q = new HashSet<(int, int)>();
            bool[] shortestPathTreeSet = new bool[map.Length * map[0].Length];

            for (var y = 0; y < map.Length; y++)
            {
                for (int x = 0; x < map.Length; x++)
                {
                    distance[(x, y)] = int.MaxValue;
                }
            }

            q.Add((0, 0));
            distance[(0, 0)] = 0;
            while (q.Count > 0)
            {
                var (x, y) = MinimumDistance(distance, q);

                q.Remove((x, y));

                if ((x, y) == (map.Length - 1, map[0].Length - 1))
                {
                    break;
                }
                var neightbours = GetNeighbours(x, y, map[0].Length, map.Length);

                foreach (var (vx, vy) in neightbours)
                {
                    var alt = distance[(x, y)] + map[vy][vx];
                    if (alt < distance[(vx, vy)])
                    {
                        distance[(vx, vy)] = alt;
                        q.Add((vx, vy));
                    }
                }
            }

            return distance[(map.Length - 1, map[0].Length - 1)];

            //for (int count = 0; count < verticesCount - 1; ++count)
            //{
            //    int u = MinimumDistance(distance, shortestPathTreeSet, verticesCount);
            //    shortestPathTreeSet[u] = true;

            //    for (int v = 0; v < verticesCount; ++v)
            //    {
            //        if (!shortestPathTreeSet[v] && Convert.ToBoolean(graph[u, v]) && distance[u] != int.MaxValue && distance[u] + graph[u, v] < distance[v])
            //        {
            //            distance[v] = distance[u] + graph[u, v];
            //        }
            //    }
            //}
        }

        private static (int, int) MinimumDistance(Dictionary<(int, int), int> distance, HashSet<(int, int)> q)
        {

            var min = q.MinBy(p => distance[p]);

            return min;
        }

        private IEnumerable<(int x, int y)> GetNeighbours(int x, int y, int xMax, int yMax)
        {
            if (x > 0) yield return (x - 1, y);
            if (y > 0) yield return (x, y - 1);
            if (x < xMax - 1) yield return (x + 1, y);
            if (y < yMax - 1) yield return (x, y + 1);
        }

    }
}