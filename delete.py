from google import genai


client = genai.Client()

FILE_SEARCH_STORE_NAME = "fileSearchStores/oyster-eq3dkhc0evtu"

def main():
    client.file_search_stores.delete(file_search_store_name=FILE_SEARCH_STORE_NAME, force=True)
    print("File search store deleted")

if __name__ == "__main__":
    main()
