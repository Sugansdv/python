def add_account(accounts):
    site = input("Site Name: ").strip().lower()
    if site in accounts:
        print(" Account already exists. Use update instead.")
        return

    username = input("Username: ").strip()
    password = input("Password: ").strip()
    tags = set(tag.strip().lower() for tag in input("Tags (comma-separated): ").split(","))
    accounts[site] = ((username, password), tags)
    print(" Account added.")

def update_account(accounts):
    site = input("Site Name to update: ").strip().lower()
    if site not in accounts:
        print(" Site not found.")
        return

    username = input("New Username: ").strip()
    password = input("New Password: ").strip()
    tags = set(tag.strip().lower() for tag in input("New Tags (comma-separated): ").split(","))
    accounts[site] = ((username, password), tags)
    print("Account updated.")

def delete_account(accounts):
    site = input("Site Name to delete: ").strip().lower()
    if site in accounts:
        del accounts[site]
        print(" Account deleted.")
    else:
        print(" Site not found.")

def search_accounts(accounts):
    query = input("Search by site or tag: ").strip().lower()
    found = False
    for site, ((username, password), tags) in accounts.items():
        if query in site or query in tags:
            print(f"\n Site: {site}")
            print(f"  Username: {username}")
            print(f"  Password: {password}")
            print(f"  Tags: {', '.join(tags)}")
            found = True
    if not found:
        print(" No matching records found.")
