from image_processing.Constants import board_size


class Trie:
    def __init__(self):
        self.root = {}

    def add_word(self, s):
        cur_dict = self.root
        for c in s:
            if c not in cur_dict.keys():
                cur_dict[c] = {}
            cur_dict = cur_dict[c]
        cur_dict['final'] = True

    def contains(self, s):
        cur_dict = self.root
        for c in s:
            if c not in cur_dict.keys():
                return False
            cur_dict = cur_dict[c]
        return 'final' in cur_dict.keys()


class Graph:
    def __init__(self, letters):
        self.letters = letters
        self.vertices = []
        self.edges = {}
        for i in range(len(letters)):
            self.vertices.append([])
            for j in range(len(letters[i])):
                self.edges[(i, j)] = []
                if i > 0:
                    self.edges[(i, j)].append((i - 1, j))
                    self.edges[(i - 1, j)].append((i, j))
                    if j > 0:
                        self.edges[(i, j)].append((i - 1, j - 1))
                        self.edges[(i - 1, j - 1)].append((i, j))
                    if j < board_size - 1:
                        self.edges[(i, j)].append((i - 1, j + 1))
                        self.edges[(i - 1, j + 1)].append((i, j))
                if j > 0:
                    self.edges[(i, j)].append((i, j - 1))
                    self.edges[(i, j - 1)].append((i, j))

    def dfs(self, i, j, used, length, paths, cur_path):
        used[i][j] = True
        cur_path.append((i, j))
        if len(cur_path) == length:
            paths.append(cur_path.copy())
            cur_path.pop()
            used[i][j] = False
            return
        for y, x in self.edges[(i, j)]:
            if not used[y][x]:
                self.dfs(y, x, used, length, paths, cur_path)
        paths.append(cur_path.copy())
        cur_path.pop()
        used[i][j] = False
        return

    def gen_paths(self, length, i, j):
        paths = []
        used = []
        for _ in range(board_size):
            used.append([False] * board_size)
        self.dfs(i, j, used, length, paths, [])
        return paths

    def gen_strings(self, length, i, j):
        paths = self.gen_paths(length, i, j)
        strings = []
        for path in paths:
            s = ''
            for y, x in path:
                s += self.letters[y][x]
            strings.append((s, path))
        return strings
