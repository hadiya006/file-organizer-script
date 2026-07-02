from pathlib import Path
import shutil
import logging

logging.basicConfig(
    filename="organizer.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logging.info("Program started")
folder=Path(r"C:\Users\hadiya\Downloads\TestFolder")
for item in folder.iterdir():
    #print(item)
    #print("File Name:",item.name)
    #print("Extension:",item.suffix) #file extension
    #print("Size:",item.stat().st_size) #size of file in bytes
    extension=item.suffix.lower()
    if extension==".jpg" or extension==".png":
        destination=folder / "Images"
        if not destination.exists():
            destination.mkdir()
            logging.info(f"Created folder: {destination.name}")
        else:
            print("Folder already exists")
        shutil.move(item,destination)
        logging.info(f"Moving {item.name} to {destination.name}")

    elif extension==".pdf" or extension==".txt":
        destination=folder / "Docs"
        if not destination.exists():
            destination.mkdir()
            logging.info(f"Created folder: {destination.name}")
        else:
            print("Folder already exists")
        shutil.move(item,destination)
        logging.info(f"Moving {item.name} to {destination.name}")

    elif extension==".mp3":
        destination=folder / "Audio"
        if not destination.exists():
            destination.mkdir()
            logging.info(f"Created folder: {destination.name}")
        else:
            print("Folder already exists")
        shutil.move(item,destination)
        logging.info(f"Moving {item.name} to {destination.name}")


    print()




