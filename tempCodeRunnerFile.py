goals = [
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 0, 1, 2, 3, 4, 5, 6, 7, 8],
    [2, 1, 0, 1, 2, 3, 4, 5, 6, 7],
    [3, 2, 1, 0, 1, 2, 3, 4, 5, 6],
    [4, 3, 2, 1, 0, 1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1, 0, 1, 2, 3, 4],
    [6, 5, 4, 3, 2, 1, 0, 1, 2, 3],
    [7, 6, 5, 4, 3, 2, 1, 0, 1, 2],
    [8, 7, 6, 5, 4, 3, 2, 1, 0, 1],
    [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
]

wins = [0] * 10
draws = [0] * 10
losses = [0] * 10
goals_scored = [0] * 10
goals_conceded = [0] * 10

for i in range(10):
    for j in range(10):
        if i != j:
            if goals[i][j] > goals[j][i]:
                wins[i] += 1
            elif goals[i][j] < goals[j][i]:
                losses[i] += 1
            else:
                draws[i] += 1
            goals_scored[i] += goals[i][j]
            goals_conceded[i] += goals[j][i]

goal_difference = [goals_scored[i] - goals_conceded[i] for i in range(10)]
points = [wins[i] * 3 + draws[i] for i in range(10)]

for i in range(10):
    print(f"Equipo {i + 1}: Victorias: {wins[i]}, Empates: {draws[i]}, Derrotas: {losses[i]}, Diferencia de goles: {goal_difference[i]}, Puntos: {points[i]}")
#9