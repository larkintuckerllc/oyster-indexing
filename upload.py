import time

from google import genai


client = genai.Client()
FILE_SEARCH_STORE_NAME = "fileSearchStores/oyster-bqyx5yps5cij"
FILES = [
    {
        "display_name": "The Role of Water Temperature in Hard Clam Aquaculture",
        "file": "data/FA151.pdf",
        "url": "https://edis.ifas.ufl.edu/publication/FA151",
    },
    {
        "display_name": "The Role of Dissolved Oxygen in Hard Clam Aquaculture",
        "file": "data/FA152.pdf",
        "url": "https://edis.ifas.ufl.edu/publication/FA152",
    },
]
def main():
    for file in FILES:
        operation = client.file_search_stores.upload_to_file_search_store(
            file=file["file"],
            file_search_store_name=FILE_SEARCH_STORE_NAME,
            config={
                "display_name": f"{file['display_name']}|{file['url']}",
            },
        )
        while not operation.done:
            time.sleep(5)
            operation = client.operations.get(operation)
        print(f"{file['file']} uploaded")
    print("files uploaded")

if __name__ == "__main__":
    main()
