import os
import difflib

def load_documents(folder_path):
    documents = {}
    try:
        for filename in os.listdir(folder_path):
            if filename.endswith(".txt"):
                with open(os.path.join(folder_path, filename), "r", encoding="utf-8") as f:
                    content = f.read().strip()
                    if not content:
                        raise ValueError(f"{filename} is empty.")
                    documents[filename] = content
    except Exception as e:
        raise Exception(f"Error reading documents: {e}")
    return documents

def compare_documents(documents, threshold=0.7):
    """Yields document pairs with similarity above the threshold"""
    keys = list(documents.keys())
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            doc1, doc2 = keys[i], keys[j]
            ratio = difflib.SequenceMatcher(None, documents[doc1], documents[doc2]).ratio()
            if ratio >= threshold:
                yield doc1, doc2, round(ratio * 100, 2)

def main():
    folder = "documents"  # 📁 Create this folder and add .txt files
    if not os.path.exists(folder):
        os.makedirs(folder)
        with open(os.path.join(folder, "doc1.txt"), "w", encoding="utf-8") as f:
            f.write("Python is a great programming language.")
        with open(os.path.join(folder, "doc2.txt"), "w", encoding="utf-8") as f:
            f.write("Python is a powerful programming language loved by many.")
        print("📄 Sample documents created. Run again to compare.")

    try:
        docs = load_documents(folder)
        matches = list(compare_documents(docs))

        if matches:
            print("\n🔍 Plagiarism Report:")
            for doc1, doc2, similarity in matches:
                print(f"{doc1} ⬌ {doc2} => {similarity}% similarity")
        else:
            print("✅ No suspicious similarity found.")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
