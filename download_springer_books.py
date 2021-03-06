data = ["http://link.springer.com/openurl?genre=book&isbn=978-0-387-84858-7",
        "http://link.springer.com/openurl?genre=book&isbn=978-0-387-88698-5",
        "http://link.springer.com/openurl?genre=book&isbn=978-0-387-93837-0",
        "http://link.springer.com/openurl?genre=book&isbn=978-3-662-44874-8",
        "http://link.springer.com/openurl?genre=book&isbn=978-3-319-03762-2",
        "http://link.springer.com/openurl?genre=book&isbn=978-3-319-18842-3",
        "http://link.springer.com/openurl?genre=book&isbn=978-3-319-48936-0",
        "http://link.springer.com/openurl?genre=book&isbn=978-3-319-01851-5",
        "http://link.springer.com/openurl?genre=book&isbn=978-3-319-13072-9",
        "http://link.springer.com/openurl?genre=book&isbn=978-3-319-02099-0",
        "http://link.springer.com/openurl?genre=book&isbn=978-3-319-23042-9",
        "http://link.springer.com/openurl?genre=book&isbn=978-3-319-47831-9",
        "http://link.springer.com/openurl?genre=book&isbn=978-3-319-46162-5",
        "http://link.springer.com/openurl?genre=book&isbn=978-1-4471-7307-6",
        "http://link.springer.com/openurl?genre=book&isbn=978-1-84882-935-0",
        "http://link.springer.com/openurl?genre=book&isbn=978-3-319-14142-8",
        "http://link.springer.com/openurl?genre=book&isbn=978-3-540-77974-2",
        "http://link.springer.com/openurl?genre=book&isbn=978-3-319-54413-7",
        "http://link.springer.com/openurl?genre=book&isbn=978-1-4939-2122-5",
        "http://link.springer.com/openurl?genre=book&isbn=978-1-4939-2614-5",
        "http://link.springer.com/openurl?genre=book&isbn=978-3-319-23428-1",
        "http://link.springer.com/openurl?genre=book&isbn=978-94-007-1211-9",
        "http://link.springer.com/openurl?genre=book&isbn=978-3-319-27104-0",
        "http://link.springer.com/openurl?genre=book&isbn=978-3-319-55444-0",
        "http://link.springer.com/openurl?genre=book&isbn=978-3-319-63913-0",
        "http://link.springer.com/openurl?genre=book&isbn=978-3-319-44561-8",
        "http://link.springer.com/openurl?genre=book&isbn=978-3-319-29854-2",
        "http://link.springer.com/openurl?genre=book&isbn=978-1-4471-6419-7",
        "http://link.springer.com/openurl?genre=book&isbn=978-1-4939-6572-4",
        "http://link.springer.com/openurl?genre=book&isbn=978-1-84800-322-4",
        "http://link.springer.com/openurl?genre=book&isbn=978-1-4614-6940-7",
        "http://link.springer.com/openurl?genre=book&isbn=978-3-319-11080-6",
        "http://link.springer.com/openurl?genre=book&isbn=978-3-319-24346-7",
        "http://link.springer.com/openurl?genre=book&isbn=978-1-4613-0041-0",
        "http://link.springer.com/openurl?genre=book&isbn=978-1-4939-2712-8",
        "http://link.springer.com/openurl?genre=book&isbn=978-1-4614-7630-6",
        "http://link.springer.com/openurl?genre=book&isbn=978-1-4614-6227-9",
        "http://link.springer.com/openurl?genre=book&isbn=978-1-4614-7138-7",
        "http://link.springer.com/openurl?genre=book&isbn=978-3-319-44048-4",
        "http://link.springer.com/openurl?genre=book&isbn=978-3-319-12493-3",
        "http://link.springer.com/openurl?genre=book&isbn=978-1-84628-642-1",
        "http://link.springer.com/openurl?genre=book&isbn=978-3-319-19425-7",
        "http://link.springer.com/openurl?genre=book&isbn=978-1-84628-168-6",
        "http://link.springer.com/openurl?genre=book&isbn=978-3-319-14240-1",
        "http://link.springer.com/openurl?genre=book&isbn=978-3-319-15195-3",
        "http://link.springer.com/openurl?genre=book&isbn=978-3-319-24280-4",
        "http://link.springer.com/openurl?genre=book&isbn=978-3-319-50017-1",
        "http://link.springer.com/openurl?genre=book&isbn=978-1-4614-6849-3",
        "http://link.springer.com/openurl?genre=book&isbn=978-3-319-18398-5",
        "http://link.springer.com/openurl?genre=book&isbn=978-1-4471-5601-7",
        "http://link.springer.com/openurl?genre=book&isbn=978-1-4471-6684-9",
        "http://link.springer.com/openurl?genre=book&isbn=978-1-4614-8687-9",
        "http://link.springer.com/openurl?genre=book&isbn=978-3-642-20144-8",
        "http://link.springer.com/openurl?genre=book&isbn=978-3-319-70790-7",
        "http://link.springer.com/openurl?genre=book&isbn=978-3-319-58487-4",
        "http://link.springer.com/openurl?genre=book&isbn=978-3-319-73004-2",
        "http://link.springer.com/openurl?genre=book&isbn=978-3-319-78361-1",
        "http://link.springer.com/openurl?genre=book&isbn=978-3-319-91041-3",
        "http://link.springer.com/openurl?genre=book&isbn=978-3-319-94463-0",
        "http://link.springer.com/openurl?genre=book&isbn=978-3-319-72347-1",
        "http://link.springer.com/openurl?genre=book&isbn=978-3-319-91155-7",
        "http://link.springer.com/openurl?genre=book&isbn=978-3-030-01279-3",
        "http://link.springer.com/openurl?genre=book&isbn=978-3-030-20290-3",
        "http://link.springer.com/openurl?genre=book&isbn=978-3-030-25943-3"]

import os
root='https://link.springer.com/content/pdf/10.1007%2F'
for item in data:
    book_isbn=item.split("=")[2]
    print(book_isbn) 
    download_link=f"{root}{book_isbn}.pdf"
    print(download_link)
    os.system(f"wget {download_link}")
    

# https://link.springer.com/content/pdf/10.1007%2F978-3-662-44874-8.pdf
