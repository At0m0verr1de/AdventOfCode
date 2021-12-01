"""
    1. You have a lot of adaptors. Each takes input joltage as x - [1, 3] where x is its rating
        that is given as input.
    2. Each adaptor outputs the joltage it is rated as.
    3. The device to charge is rated as y + 3, where y is the highest rated adaptor in our bag.
    4. Input voltage is 0 so only a 1,2,3 joltage adaptor can be used so just keep on using
        adaptors in increasing order of their magnitude.
"""

dataset = """67
118
90
41
105
24
137
129
124
15
59
91
94
60
108
63
112
48
62
125
68
126
131
4
1
44
77
115
75
89
7
3
82
28
97
130
104
54
40
80
76
19
136
31
98
110
133
84
2
51
18
70
12
120
47
66
27
39
109
61
34
121
38
96
30
83
69
13
81
37
119
55
20
87
95
29
88
111
45
46
14
11
8
74
101
73
56
132
23
0
140""".split("\n")

dataset = list(map(int, dataset))
dataset.sort()
ones = 0
triples = 0

for i in range(0, len(dataset)-1):
    if dataset[i+1]-dataset[i] == 1:
        ones += 1
    elif dataset[i+1]-dataset[i] == 3:
        triples += 1

print(f"Ones: {ones}")
print(f"triples: {triples}")