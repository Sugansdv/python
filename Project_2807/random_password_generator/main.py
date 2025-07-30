from core.generator import infinite_passwords

def main():
    count = 5
    print(f"Generating {count} secure passwords:\n")
    gen = infinite_passwords(length=12, exclude_similar=True)

    for _ in range(count):
        print(next(gen))

if __name__ == "__main__":
    main()
