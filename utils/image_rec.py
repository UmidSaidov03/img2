import easyocr

async def text_recognition (file_path,text_file_name="result.doc"):
    reader =easyocr.Reader(["ru","en"])
    result = reader.readtext(file_path,detail=0,paragraph=True)

    # with open(text_file_name,'w') as file:
    #     for line in result:
    #         file.write(f"{line}\n\n")
    return result


# async def main():
#     file_path=input("Rasm yolini korsating")
#     print(text_recognition(file_path=file_path,text_file_name="read_me_first.txt"))


# if __name__ == "__main__":
#     main()