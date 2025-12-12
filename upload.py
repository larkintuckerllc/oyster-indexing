import time

from google import genai


client = genai.Client()
FILE_SEARCH_STORE_NAME = "fileSearchStores/oyster-ge1jsz2g0cl0"
FILES = [
    {
        "display_name": "Introduction to Vibrio vulnificus",
        "file": "data/cn-intro.pdf",
        "url": "https://marexgasg.wixsite.com/safeoysters/cn-intro",
    },
    {
        "display_name": "Safely Buying Raw Oysters and Other Molluscan Shellfish",
        "file": "data/cn-buying.pdf",
        "url": "https://marexgasg.wixsite.com/safeoysters/cn-buying",
    },
    {
        "display_name": "Safely Storing Oysters and Other Molluscan Shellfish",
        "file": "data/cn-storing.pdf",
        "url": "https://marexgasg.wixsite.com/safeoysters/cn-storing",
    },
    {
        "display_name": "Safely Cooking Oysters and Other Molluscan Shellfish",
        "file": "data/cn-cooking.pdf",
        "url": "https://marexgasg.wixsite.com/safeoysters/cn-cooking",
    },
    {
        "display_name": "Safely Eating Oysters and Other Molluscan Shellfish",
        "file": "data/copy-of-cooking.pdf",
        "url": "https://marexgasg.wixsite.com/safeoysters/copy-of-cooking",
    },
    {
        "display_name": "Georgia Oyster Recipes - UGA Marine Extension and Georgia Sea Grant",
        "file": "data/ga-recipes.pdf",
        "url": "https://04a669dc-12bf-4b88-83c6-6687cf4c2223.filesusr.com/ugd/9d071d_ea71fe84309548039d280a0d984332b1.pdf",
    },
    {
        "display_name": "Mississippi Oyster Recipes - Mississippi Dept. of Marine Resources",
        "file": "data/ms-recipes.pdf",
        "url": "https://04a669dc-12bf-4b88-83c6-6687cf4c2223.filesusr.com/ugd/9d071d_5d6d8b06b1a7462bbc44cc96615a5d14.pdf",
    },
    {
        "display_name": "Post-Harvest Processed (PHP) Oysters",
        "file": "data/cn-php.pdf",
        "url": "https://marexgasg.wixsite.com/safeoysters/cn-php",
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
