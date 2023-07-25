""" program that prompts the user for the name of a file and then outputs
that file's media type if the file's name ends, case-insensitively.
If the file's name ends with some other suffix or has no suffix at all,
output application/octet-stream instead, which is a common default."""

file = input("File name: ").strip().lower()

if file.endswith(".gif"):
    print("image/gif")
elif file.endswith(".jpeg") or file.endswith(".jpg"):
    print("image/jpeg")
elif file.endswith(".png"):
    print("image/png")
elif file.endswith(".pdf"):
    print("application/pdf")
elif file.endswith(".txt"):
    print("text/plain")
elif file.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
