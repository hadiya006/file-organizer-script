from pathlib import Path
import shutil
import logging
import argparse


rules={
    ".jpg":"Images",
    ".png":"Images",
    ".pdf":"Docs",
    ".txt":"Docs",
    ".mp3":"Audio"
}
parser=argparse.ArgumentParser()
parser.add_argument("--dry-run",action="store_true")
args=parser.parse_args()

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
    if extension in rules:
        destination=folder / rules[extension]
        if not destination.exists():
            destination.mkdir()
            logging.info(f"Created folder: {destination.name}")
        else:
            print("Folder already exists")
        if args.dry_run:
            logging.info(f"Would move {item.name} to {destination.name}")
        else:
            shutil.move(item,destination)
            logging.info(f"Moving {item.name} to {destination.name}")

    elif extension in rules:
        destination=folder / rules[extension]
        if not destination.exists():
            destination.mkdir()
            logging.info(f"Created folder: {destination.name}")
        else:
            print("Folder already exists")
        if args.dry_run:
            logging.info(f"Would move {item.name} to {destination.name}")
        else:
            shutil.move(item,destination)
            logging.info(f"Moving {item.name} to {destination.name}")

    elif extension in rules:
        destination=folder / rules[extension]
        if not destination.exists():
            destination.mkdir()
            logging.info(f"Created folder: {destination.name}")
        else:
            print("Folder already exists")
        if args.dry_run:
            logging.info(f"Would move {item.name} to {destination.name}")
        else:
            shutil.move(item,destination)
            logging.info(f"Moving {item.name} to {destination.name}")


    print()




