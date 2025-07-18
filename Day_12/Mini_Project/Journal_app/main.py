import argparse
from journal.entry import add_entry
from journal.viewer import view_entries, search_entries
from journal.exporter import export_all

def main():
    parser = argparse.ArgumentParser(description="📓 Daily Journal CLI App")
    sub = parser.add_subparsers(dest="command", required=True)

    # Add entry
    p_add = sub.add_parser("add", help="Add a new journal entry")
    p_add.add_argument("text", help="Text for the entry")

    # View entry
    p_view = sub.add_parser("view", help="View journal entries")
    p_view.add_argument("--date", help="Date to view (YYYY-MM-DD)")

    # Search entry
    p_search = sub.add_parser("search", help="Search journal entries")
    p_search.add_argument("keyword", help="Keyword or regex")

    # Export
    p_export = sub.add_parser("export", help="Export all journal entries")

    args = parser.parse_args()

    if args.command == "add":
        add_entry(args.text)
    elif args.command == "view":
        view_entries(args.date)
    elif args.command == "search":
        search_entries(args.keyword)
    elif args.command == "export":
        export_all()

if __name__ == "__main__":
    main()
