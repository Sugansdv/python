from analyzer.core import DirectoryAnalyzer

def main():
    path = input("📁 Enter directory path to analyze: ").strip()
    analyzer = DirectoryAnalyzer(path)
    analyzer.scan()

    print(f"\n📦 Total Directory Size: {analyzer.total_size()}\n")
    
    print("📁 Top 5 Largest Files:")
    for path, size in analyzer.get_largest_files():
        print(f"{path} - {size / (1024 ** 2):.2f} MB")

if __name__ == "__main__":
    main()