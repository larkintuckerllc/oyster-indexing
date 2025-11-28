from google import genai


client = genai.Client()

FILE_SEARCH_STORE_NAME = "fileSearchStores/oyster-bqyx5yps5cij"

def main():
    client.file_search_stores.delete(name=FILE_SEARCH_STORE_NAME, config={"force": True})
    print("File search store deleted")

if __name__ == "__main__":
    main()
