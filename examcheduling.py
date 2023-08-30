from collections import defaultdict
class Graph:
    def __init__(self, subjects):
        self.subjects, self.graph = subjects, defaultdict(list)
    def addedge(self, s1, s2):
        self.graph[s1].append(s2)
        self.graph[s2].append(s1)
    def coloring(self):
        color_map={}
        available_colors = set(range(1, len(self.subjects)+1))
        for subject in self.subjects:
            used_colors = set()
            for neighbor in self.graph[subject]:
                if neighbor in color_map:
                    used_colors.add(color_map[neighbor])

            available_colors = available_colors - used_colors

            if available_colors:
                color_map[subject] = min(available_colors)
            else:
                color_map[subject] = len(available_colors) + 1
                available_colors.add(color_map[subject])
        return color_map
    def timeslots(self):
        return max(self.coloring().values())
n = int(input("Enter the number of subjects: "))
sub, stu= [], {}
for i in range(n):
    subject = input(f"Enter subject {i + 1}: ")
    sub.append(subject)
    n_st = int(input(f"Enter the number of students for {subject}: "))
    st_list = [input(f"Enter student {j + 1} for {subject}: ") for j in range(n_st)]
    stu[subject] = st_list
g=Graph(sub)
for _ in range(int(input("Enter the number of edges: "))):
    e = input("Enter edge (subject1 subject2): ").split()
    g.addedge(e[0], e[1])
print(f"\nMinimum time slots needed: {g.timeslots()}")
