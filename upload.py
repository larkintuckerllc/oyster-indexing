import os
import time

from google import genai


client = genai.Client()
DATA_FOLDER = "data"
FILE_SEARCH_STORE_NAME = "fileSearchStores/oyster-eq3dkhc0evtu"

def main():
    for filename in os.listdir(DATA_FOLDER):
        file_path = os.path.join(DATA_FOLDER, filename)
        operation = client.file_search_stores.upload_to_file_search_store(
            file=file_path,
            file_search_store_name=FILE_SEARCH_STORE_NAME,
        )
        while not operation.done:
            time.sleep(5)
            operation = client.operations.get(operation)
        print(f"{filename} uploaded")
    print("files uploaded")

if __name__ == "__main__":
    main()
