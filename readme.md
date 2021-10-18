# Organizer

Organizer is a python program that organizes your downloads folder, it can run as a service and so will start along with the system, and the best, you do not need to run it runs once you think your folder needs to be organized, it observes by new items in the Downloads folder and organizes them automatically for you!

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.

```bash
pip install -r requirements.txt

## Usage

This script searches for a file called types.json in your home directory, you need that file there with the following pattern:

json
[
  {
    "name": "image",
    "extensions": [
      ".png",
      ".jpg",
      ".jpeg",
      ".gif",
      ".jpgx",
      ".svg",
      ".webp"
    ]
  },
  {
    "name": "compressed",
    "extensions": [
      ".gz",
      ".gzip",
      ".zip",
      ".7z",
      ".tar.gz",
      ".tag",
      ".rar",
      ".xz"
    ]
  }, 
  {
    "name": "video",
    "extensions": [
      ".mp4",
      ".mkv"
    ]
  },
  {
    "name": "packages",
    "extensions": [
      ".deb",
      ".AppImage"
    ]
  },
  { 
    "name": "data",
    "extensions": [
      ".csv",
      ".json",
      ".sql"
    ]
  },
  {
    "name": "executable",
    "extensions": [
      ".py",
      ".bin",
      ".exe",
      ".sh",
      ".bash"
    ]
  },
  { 
    "name": "fonts",
    "extensions": [
      ".ttf",
      ".otf"
    ]
  },

  {
    "name": "dev",
    "extensions": [
      ".css", 
      ".js",
      ".tsx",
      ".ts",
      ".mjs"
    ]
  },
  {
    "name": "document",
    "extensions": [
      ".pdf",
      ".rtf", 
      ".txt",
      ".doc",
      ".docx",
      ".ods"
    ]
  }
]

Each name will be converted to a folder, and the array of extensions are the types of files that must be sent to that folder.

You can change these names and extensions in any way you think is best, you should only keep the same file name and it needs to be in your home folder.




bash
python3 . #in the clone folder

## You can run this script as a service without any problems!

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)