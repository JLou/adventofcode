namespace aoc
{
    public class Day18 : IDay
    {
        public (string, string) Compute(string[] input)
        {
            Node megaroot = null!;
            List<Node> nodes = new List<Node>();

            foreach (var line in input)
            {
                var root = BuildNodeRecurr(line);
                if (megaroot == null)
                {
                    megaroot = root;
                }
                else
                {
                    megaroot = new Node
                    {
                        Left = megaroot,
                        Right = root
                    };
                    megaroot.Left.Parent = megaroot;
                    megaroot.Right.Parent = megaroot;
                }

                Reduce(megaroot);
                Console.WriteLine(printNode(megaroot));
            }

            Reduce(megaroot);

            int max = 0;

            for (int i = 0; i < input.Length; i++)
            {
                for (int j = 0; j < input.Length; j++)
                {
                    if (i == j) continue;

                    var r = new Node
                    {
                        Left = BuildNodeRecurr(input[i]),
                        Right = BuildNodeRecurr(input[j]),
                    };
                    r.Left.Parent = r;
                    r.Right.Parent = r;

                    Reduce(r);
                    max = Math.Max(Magnitude(r), max);
                }
            }

            return (Magnitude(megaroot).ToString(), max.ToString());
        }

        private static void Reduce(Node megaroot)
        {
            var stack = new Stack<Node>();
            stack.Push(megaroot.Right);
            stack.Push(megaroot.Left);
            Node node;
            bool isStable = true;

            do
            {
                isStable = true;
                Node? toSplit = null;
                while (stack.TryPop(out node))
                {
                    node.Level = node.Parent.Level + 1;

                    //if (node.Value != -1) Console.Write(node.Value + ", ");

                    if (toSplit == null && node.Value >= 10)
                    {
                        toSplit = node;
                    }
                    else if (node.Value == -1 && node.Left.Value != -1 && node.Right.Value != -1)
                    {
                        var (a, b) = (node.Left.Value, node.Right.Value);

                        if (node.Level >= 4)
                        {
                            var parent = node.Parent;
                            var currNode = node;
                            while (parent != null && parent.Left == currNode)
                            {
                                currNode = parent;
                                parent = parent.Parent;
                            }
                            if (parent != null)
                            {
                                parent = parent.Left;
                            }
                            if (parent != null)
                            {
                                while (parent.Value == -1)
                                {
                                    parent = parent.Right;
                                }
                                parent.Value += a;
                            }


                            parent = node.Parent;
                            currNode = node;
                            while (parent != null && parent.Right == currNode)
                            {
                                currNode = parent;
                                parent = parent.Parent;
                            }
                            if (parent != null)
                            {
                                parent = parent.Right;
                            }
                            if (parent != null)
                            {
                                while (parent.Value == -1)
                                {
                                    parent = parent.Left;
                                }

                                parent.Value += b;
                            }

                            node.Value = 0;
                            node.Left = null;
                            node.Right = null;

                            isStable = false;
                            break;
                        }
                        else
                        {
                            if (node.Right != null)
                            {
                                stack.Push(node.Right);
                            }

                            if (node.Left != null)
                            {
                                stack.Push(node.Left);
                            }

                        }
                    }
                    else
                    {
                        if (node.Right != null)
                        {
                            stack.Push(node.Right);
                        }

                        if (node.Left != null)
                        {
                            stack.Push(node.Left);
                        }
                    }
                }

                if (isStable && toSplit != null)
                {
                    toSplit.Left = new Node()
                    {
                        Value = (int)Math.Floor(toSplit.Value / 2.0),
                        Level = toSplit.Level + 1,
                        Parent = toSplit
                    };
                    toSplit.Right = new Node()
                    {
                        Value = (int)Math.Ceiling(toSplit.Value / 2.0),
                        Level = toSplit.Level + 1,
                        Parent = toSplit
                    };
                    toSplit.Value = -1;
                    isStable = false;
                }
                stack.Clear();
                stack.Push(megaroot.Right);
                stack.Push(megaroot.Left);

            } while (!isStable);
        }

        private string printNode(Node node)
        {
            if (node.Value != -1)
            {
                return node.Value.ToString();
            }
            else
            {
                return $"[{printNode(node.Left)},{printNode(node.Right)}]";
            }
        }

        private int Magnitude(Node node)
        {
            if (node.Value != -1)
            {
                return node.Value;
            }
            else
            {
                return 3 * Magnitude(node.Left) + 2 * Magnitude(node.Right);
            }
        }


        private Node BuildNodeRecurr(string s)
        {
            if (int.TryParse(s, out var n))
            {
                return new Node() { Value = n };
            }

            int opened = 0;
            int splitIndex = 0;
            for (int i = 1; i < s.Length; i++)
            {
                var c = s[i];
                switch (c)
                {
                    case '[':
                        opened++;
                        break;
                    case ']':
                        opened--;
                        break;
                    case ',':
                        if (opened == 0)
                            splitIndex = i;
                        break;
                };
                if (splitIndex > 0) break;
            }

            Node left = BuildNodeRecurr(s.Substring(1, splitIndex - 1));
            Node right = BuildNodeRecurr(s.Substring(splitIndex + 1, s.Length - splitIndex - 2));

            var node = new Node()
            {
                Left = left,
                Right = right
            };

            left.Parent = node;
            right.Parent = node;
            return node;
        }

        class Node
        {
            public int Value { get; set; } = -1;
            public Node? Parent { get; set; }
            public Node Left { get; set; }
            public Node Right { get; set; }
            public int Level { get; set; } = 0;
        }
    }
}
