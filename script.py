from pathlib import Path
import shutil

folder=Path(r"C:\Users\hadiya\Downloads\TestFolder")
for item in folder.iterdir():
    #print(item)
    print("File Name:",item.name)
    print("Extension:",item.suffix) #file extension
    print("Size:",item.stat().st_size) #size of file in bytes
    extension=item.suffix.lower()
    if extension==".jpg" or extension==".png":
        print("Belongs to Images")
        destination=folder / "Images"
        if not destination.exists():
            destination.mkdir()
            print("Image folder created.")
        else:
            print("Folder already exists")
        shutil.move(item,destination)

    elif extension==".pdf" or extension==".txt":
        print("Belongs to Documents")
        destination=folder / "Docs"
        if not destination.exists():
            destination.mkdir()
            print("Docs folder created.")
        else:
            print("Folder already exists")
        shutil.move(item,destination)

    elif extension==".mp3":
        print("Belongs to Audio")
        destination=folder / "Audio"
        if not destination.exists():
            destination.mkdir()
            print("Audio folder created.")
        else:
            print("Folder already exists")
        shutil.move(item,destination)

    print()




