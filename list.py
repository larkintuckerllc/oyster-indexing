from google import genai


client = genai.Client()

def main():
    file_search_stores = client.file_search_stores.list()
    for file_search_store in file_search_stores:
        print(file_search_store.name)

if __name__ == "__main__":
    main()
