high_score_board = []  

def record_game(player, *scores, bonus=0, multiplier=1.0):
  
    global high_score_board

    if len(scores) == 0:
        return (player, 0, 0, "no rounds played")

    if any(s < 0 for s in scores):
        return (player, 0, 0, "negative score not allowed")

    raw_total = sum(scores)
    total = int((raw_total + bonus) * multiplier)
    rounds = len(scores)

    for i, (p, s) in enumerate(high_score_board):
        if p == player:
            if total > s:
                high_score_board[i] = (player, total)
            break
    else:
        high_score_board.append((player, total))

    sorted_board = sorted(high_score_board, key=lambda x: x[1], reverse=True)
    current_score = max(total, next(s for p, s in high_score_board if p == player))
    rank = next(i + 1 for i, (p, s) in enumerate(sorted_board) if p == player)

    status = "high score!" if rank == 1 else f"rank {rank}"

    return (player, rounds, total, status)


print("=" * 50)
print("         🎮 GAME SCOREBOARD SYSTEM 🎮")
print("=" * 50)

results = []

r1 = record_game("Hussain", 80, 95, 70, bonus=20, multiplier=1.5)
results.append(r1)

r2 = record_game("Ali", 60, 55, 90, 75)
results.append(r2)

r3 = record_game("Sara", 100, 100, 95, bonus=50, multiplier=2.0)
results.append(r3)

r4 = record_game("Omar")
results.append(r4)

r5 = record_game("Noor", 80, -10, 50)
results.append(r5)

r6 = record_game("Hussain", 99, 99, 99, bonus=10, multiplier=1.0)
results.append(r6)

print("\n📋 Round Results:")
print("-" * 50)
for player, rounds, total, status in results:
    print(f"  {player:<10} | rounds: {rounds} | total: {total:<6} | {status}")

print("\n🏆 Final Leaderboard:")
print("-" * 50)
sorted_board = sorted(high_score_board, key=lambda x: x[1], reverse=True)
for rank, (player, total) in enumerate(sorted_board, start=1):
    medal = "🥇" if rank == 1 else "🥈" if rank == 2 else "🥉" if rank == 3 else "  "
    print(f"  {medal} Rank {rank}: {player:<10} → {total} pts")

print("=" * 50)