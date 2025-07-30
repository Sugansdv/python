from core.shortener import URLShortener
from utils.decorators import cache

shortener = URLShortener()

@cache
def get_redirect_url(code):
    return shortener.redirect(code)

def main():
    while True:
        print("\n1. Shorten URL\n2. Redirect\n3. Delete\n4. List All\n5. Expired URLs\n6. Exit")
        choice = input("Enter choice: ")
        
        try:
            if choice == '1':
                url = input("Enter the original URL: ")
                code = shortener.shorten(url)
                print(f"Shortened URL: {code}")
            elif choice == '2':
                code = input("Enter short code: ")
                print("Original URL:", get_redirect_url(code))
            elif choice == '3':
                code = input("Enter short code to delete: ")
                if shortener.delete(code):
                    print("Deleted successfully.")
                else:
                    print("Short code not found.")
            elif choice == '4':
                for c, d in shortener.list_urls().items():
                    print(f"{c} => {d['url']} (Expires: {d['expiry']})")
            elif choice == '5':
                for exp in shortener.expired_urls():
                    print(f"Expired: {exp}")
            elif choice == '6':
                break
            else:
                print("Invalid choice.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
