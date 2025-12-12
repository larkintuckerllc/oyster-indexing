from google import genai


client = genai.Client()

FILE_SEARCH_STORE_NAME = "fileSearchStores/oyster-ge1jsz2g0cl0"

def main():
    client.file_search_stores.delete(name=FILE_SEARCH_STORE_NAME, config={"force": True})
    print("File search store deleted")

if __name__ == "__main__":
    main()
