def vote(voter, candidates, voters, votes):
    if not candidates:
        print("No candidates available.")
        return
    
    print("\nCandidates:")
    for i, candidate in enumerate(candidates, 1):
        print(f"{i}. {candidate}")

    choice = input("Enter candidate name to vote: ").strip()
    if choice in candidates:
        votes[choice] += 1
        voters.add(voter)
        print("✅ Vote cast.")
    else:
        print("❌ Invalid candidate.")
