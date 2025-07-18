

poll_results = {}  # Dictionary to store votes per candidate
voted_voters = set()  # Set to store unique voter IDs


def cast_vote(voter_id: tuple, candidate: str):
    if voter_id in voted_voters:
        return "You have already voted!"
    
    voted_voters.add(voter_id)
    if candidate in poll_results:
        poll_results[candidate] += 1
    else:
        poll_results[candidate] = 1
    return f"Vote cast successfully for {candidate}."


def show_results():
    if not poll_results:
        return "No votes cast yet."
    
    result_str = "\n--- Poll Results ---\n"
    for candidate, count in poll_results.items():
        result_str += f"{candidate}: {count} vote(s)\n"
    return result_str
