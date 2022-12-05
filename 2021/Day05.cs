using System.Text.RegularExpressions;

namespace aoc
{
    public class Day05 : IDay
    {
        public record Line(int x1, int y1, int x2, int y2);

        public (string, string) Compute(string[] input)
        {
            var regex = new Regex(@"(\d+),(\d+) -> (\d+),(\d+)");

            var lines = input
                .Select(l => regex.Match(l).Groups.Values.Skip(1).Select(v => Convert.ToInt32(v.Value)).ToArray())
                .Select(m => new Line(m[0], m[1], m[2], m[3]))
                .ToList();

            return (ComputePart(lines, false).ToString(), ComputePart(lines, true).ToString());
        }

        private int ComputePart(List<Line> lines, bool withDiagonals)
        {
            Dictionary<(int, int), int> intersections = new Dictionary<(int, int), int>();

            foreach (var line in lines)
            {
                DrawLine(line, intersections, withDiagonals);
            }

            return intersections.Count(kvp => kvp.Value > 1);
        }

        private void DrawLine(Line line, Dictionary<(int, int), int> intersections, bool withDiagonals = false)
        {
            var (x1, y1, x2, y2) = line;
            if (x1 == x2)
            {
                MarkVertical(y1, y2, x1, intersections);
            }
            else if (y1 == y2)
            {
                MarkHorizontal(x1, x2, y1, intersections);
            }
            else if (withDiagonals)
            {
                MarkDiagonal(line, intersections);
            }
        }

        private void MarkDiagonal(Line line, Dictionary<(int, int), int> intersections)
        {
            var (x1, y1, x2, y2) = line;
            var (dx, dy) = (x1 < x2 ? 1 : -1, y1 < y2 ? 1 : -1);
            Mark(x1, y1, Math.Abs(x1 - x2), dx, dy, intersections);
        }

        private void MarkVertical(int y1, int y2, int x, Dictionary<(int, int), int> intersections)
        {
            var dy = y1 < y2 ? 1 : -1;
            Mark(x, y1, Math.Abs(y1 - y2), 0, dy, intersections);
        }

        private void MarkHorizontal(int x1, int x2, int y, Dictionary<(int, int), int> intersections)
        {
            var dx = x1 < x2 ? 1 : -1;
            Mark(x1, y, Math.Abs(x1 - x2), dx, 0, intersections);
        }

        private void Mark(int x1, int y1, int length, int dx, int dy, Dictionary<(int, int), int> intersections)
        {
            for (var (x, y, i) = (x1, y1, 0); i <= length; x += dx, y += dy, i++)
            {
                if (!intersections.ContainsKey((x, y)))
                {
                    intersections.Add((x, y), 1);
                }
                else
                {
                    intersections[(x, y)]++;
                }
            }
        }
    }
}