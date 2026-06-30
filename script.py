from pathlib import Path

folder=Path(r"C:\Users\hadiya\Downloads\TestFolder")
for item in folder.iterdir():
    #print(item)
    print("File Name:",item.name)
    print("Extension:",item.suffix) #file extension
    print("Size:",item.stat().st_size) #size of file in bytes
    extension=item.suffix.lower()
    if extension==".jpg" or extension==".png":
        print("Belongs to Images")
       
    elif extension==".pdf" or extension==".txt":
        print("Belongs to Documents")

    elif extension==".mp3":
        print("Belongs to Audio")
  
    print()




