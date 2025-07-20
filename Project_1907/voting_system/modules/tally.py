def show_results(votes):
    if not votes:
        print("No votes yet.")
        return

    print("\n📊 Voting Results:")
    for candidate, count in votes.items():
        print(f"{candidate}: {count} votes")

    max_votes = max(votes.values(), default=0)
    winners = [c for c, v in votes.items() if v == max_votes and max_votes > 0]

    if winners:
        print(f"🏆 Winner(s): {', '.join(winners)}")
    else:
        print("No winner.")
