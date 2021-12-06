namespace aoc
{
    public class Day04 : IDay
    {
        public record Cell(int Value, bool Checked = false);
        public (string, string) Compute(string[] input)
        {
            var tirage = input[0].Split(",").Select(i => Convert.ToInt32(i));

            var grids = new List<Cell[,]>();
            Cell[,]? currentGrid = null;
            int rowIndex = 0;

            foreach (var row in input.Skip(1))
            {
                if (row == "")
                {
                    if (currentGrid != null)
                    {
                        grids.Add(currentGrid);
                    }
                    currentGrid = new Cell[5, 5];

                    rowIndex = 0;

                }
                else
                {
                    var numbers = row
                        .Split(" ")
                        .Where(e => !string.IsNullOrWhiteSpace(e))
                        .Select((e, index) => (Convert.ToInt32(e), index));
                    foreach (var (number, i) in numbers)
                    {
                        currentGrid![rowIndex, i] = new Cell(number, false);
                    }
                    rowIndex++;
                }
            }
            grids.Add(currentGrid);

            var ((winner, num), (loser, losernum)) = RunTirage(tirage, grids);

            var sum = ComputeGridScore(winner);
            var loserSum = ComputeGridScore(loser);

            return ((sum * num).ToString(), (loserSum * losernum).ToString());


            bool CheckRow(Cell[,] grid, int rowIndex)
            {
                return Enumerable.Range(0, 5).All(i => grid[rowIndex, i].Checked);
            }
            bool CheckColumn(Cell[,] grid, int columnIndex)
            {
                return Enumerable.Range(0, 5).All(i => grid[i, columnIndex].Checked);
            }


            ((Cell[,], int), (Cell[,], int)) RunTirage(IEnumerable<int> tirage, List<Cell[,]> grids)
            {
                var activeBoards = new HashSet<Cell[,]>(grids);
                var winners = new List<(Cell[,], int)>();
                foreach (var item in tirage)
                {
                    foreach (var (toRemove, _) in winners)
                    {
                        activeBoards.Remove(toRemove);
                    }

                    foreach (var grid in activeBoards)
                    {
                        for (int i = 0; i < 5; i++)
                        {
                            for (int j = 0; j < 5; j++)
                            {
                                if (grid[i, j].Value == item)
                                {
                                    grid[i, j] = grid[i, j] with { Checked = true };

                                    if (CheckRow(grid, i) || CheckColumn(grid, j))
                                    {
                                        winners.Add((grid, item));
                                    }
                                }
                            }
                        }
                    }
                }

                return (winners[0], winners.Last());
            }

            static int ComputeGridScore(Cell[,]? grid)
            {
                int sum = 0;
                foreach (var cell in grid)
                {
                    if (!cell.Checked)
                    {
                        sum += cell.Value;
                    }
                }

                return sum;
            }
        }

    }
}
