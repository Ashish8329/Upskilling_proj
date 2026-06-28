from sentence_transformers import SentenceTransformer


def load_document():
    with open('mini_rag/data/notes.txt', 'r') as file:
        text = file.read()

    chunks = []

    # indexing
    for line in text.split('\n'):
        line = line.strip() 

        if line:
            chunks.append(line)
    return chunks

doc = load_document()

print("\n Chunks :\n")
print(doc)

model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(doc)

print("\n Embeddings : \n") 
print(embeddings.shape)

print("\nFirst vector (shortened):\n")
print(
    embeddings[0][:10]
)