def main():
    file_name = input("File name: ").lower().strip()
    file_extension = file_name.rsplit(".",1)[-1]
    medtype = map_ext_medtype(file_extension)
    print(medtype)

def map_ext_medtype(file_extension):
    match file_extension:
        case "gif":
            return "image/gif"
        case "jpg":
            return "image/jpeg"
        case "jpeg":
            return "image/jpeg"
        case "png":
            return "image/png"
        case "pdf":
            return "application/pdf"
        case "txt":
            return "text/plain"
        case "zip":
            return "application/zip"
        case _:
            return "application/octet-stream"
main()
