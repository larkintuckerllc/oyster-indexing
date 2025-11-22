from google import genai


client = genai.Client()

def main():
    file_search_store = client.file_search_stores.create(config={"display_name": "oyster"})
    print(file_search_store.name)

if __name__ == "__main__":
    main()
