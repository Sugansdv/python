# 14. Election Vote Counter
# Description: Count votes by candidate.
# Requirements:
# - {candidate_name: vote_count}
# - Increment votes using .get(name, 0)+1
# - Show winner
# - Detect invalid votes (not in candidate list)

candidates = ["Alice", "Bob", "Charlie"]
votes = {}
vote_entries = ["Alice", "Bob", "Charlie", "Bob", "Alice", "Bob", "Diana", "Charlie", "Alice", "Bob"]

def count_votes(vote_list):
    invalid_votes = 0
    for name in vote_list:
        if name in candidates:
            votes[name] = votes.get(name, 0) + 1
        else:
            invalid_votes += 1
    return invalid_votes

def show_winner():
    if not votes:
        print("No votes counted.")
        return
    winner = max(votes, key=votes.get)
    print(f"\nWinner: {winner} with {votes[winner]} votes")

def show_results():
    print("\nVote Results:")
    for name in candidates:
        print(f"{name}: {votes.get(name, 0)}")

invalid_count = count_votes(vote_entries)
show_results()
show_winner()
print(f"\nInvalid votes: {invalid_count}")
