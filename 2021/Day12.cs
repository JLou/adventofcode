namespace aoc
{
    public class Day12 : IDay
    {
        public (string, string) Compute(string[] input)
        {
            var edges = new Dictionary<string, List<string>>();
            foreach (var edge in input)
            {
                var chunks = edge.Split('-');
                if (edges.ContainsKey(chunks[0]))
                {
                    edges[chunks[0]].Add(chunks[1]);
                }
                else
                {
                    edges[chunks[0]] = new List<string>() { chunks[1] };
                }

                if (edges.ContainsKey(chunks[1]))
                {
                    edges[chunks[1]].Add(chunks[0]);
                }
                else
                {
                    edges[chunks[1]] = new List<string>() { chunks[0] };
                }
            }

            var visitedNodeCounts = edges.Keys.ToDictionary(e => e, _ => 0);
            return (
                $"{ComputePaths("start", new HashSet<string> { "start" }, edges)}",
                $"{ComputePaths2("start", visitedNodeCounts, edges)}"
            );
        }

        public int ComputePaths(string nodeStart, HashSet<string> visitedNodes, Dictionary<string, List<string>> edges)
        {
            if (nodeStart == "end")
                return 1;
            var toVisit = edges[nodeStart].Where(e => !(IsSmallCave(e) && visitedNodes.Contains(e)));
            var s = 0;
            foreach (var node in toVisit)
            {
                var newVisitedNodes = new HashSet<string>(visitedNodes);
                newVisitedNodes.Add(node);
                s += ComputePaths(node!, newVisitedNodes, edges);
            }

            return s;
        }

        public int ComputePaths2(string nodeStart, Dictionary<string, int> visitedNodes, Dictionary<string, List<string>> edges)
        {
            if (nodeStart == "end")
                return 1;
            var toVisit = edges[nodeStart].Where(e =>
                !(IsSmallCave(e)
                    && visitedNodes.Any(kvp => IsSmallCave(kvp.Key) && kvp.Value >= 2)
                    && visitedNodes[e] >= 1)
                && e != "start");

            var s = 0;
            foreach (var node in toVisit)
            {
                var newVisitedNodes = new Dictionary<string, int>(visitedNodes);
                newVisitedNodes[node]++;
                s += ComputePaths2(node!, newVisitedNodes, edges);
            }

            return s;
        }

        private bool IsSmallCave(string nodeName) => nodeName == nodeName.ToLowerInvariant();
    }
}