class AlreadyVotedError(Exception):
    pass

voted = False

try:
    if voted:
        raise AlreadyVotedError("You have already voted.")
    choice = input("Vote for candidate (A/B/C): ").strip().upper()
    voted = True
    print(f"Vote cast for {choice}.")
except AlreadyVotedError as e:
    print(e)
except Exception as e:
    print("Unexpected error:", e)
finally:
    print("Thank you for voting!")
