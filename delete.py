from google import genai


client = genai.Client()

FILE_SEARCH_STORE_NAME = "fileSearchStores/oyster-teszfl6gu0e3"

def main():
    client.file_search_stores.delete(name=FILE_SEARCH_STORE_NAME, config={"force": True})
    print("File search store deleted")

if __name__ == "__main__":
    main()
