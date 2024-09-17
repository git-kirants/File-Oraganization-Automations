from os import scandir, rename
from os.path import splitext, exists, join
from shutil import move
from time import sleep
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Define source and destination directories
source_dir = "C:\\Users\\Kiran T S\\Downloads"
dest_dir_music = "C:\\Users\\Kiran T S\\Music\\Downloaded Musics"
dest_dir_video = "C:\\Users\\Kiran T S\\Videos\\Downloaded Videos"
dest_dir_image = "C:\\Users\\Kiran T S\\Pictures\\Downloaded Images"
dest_dir_documents = "C:\\Users\\Kiran T S\\Documents\\Downloaded Documents"
dest_dir_zip = "C:\\Users\\Kiran T S\\Downloads\\[ZIP] Files"
dest_dir_photoshop = "C:\\Users\\Kiran T S\\Documents\\[Photoshop] Files"
dest_dir_aftereffects = "C:\\Users\\Kiran T S\\Documents\\[AfterEffects] Files"

# Supported file extensions
image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".webp", ".tiff", ".bmp", ".heif", ".heic", ".svg", ".ai", ".eps", ".ico"]
video_extensions = [".webm", ".mpg", ".mp4", ".avi", ".mov", ".flv", ".wmv"]
audio_extensions = [".m4a", ".flac", ".mp3", ".wav", ".wma", ".aac"]
document_extensions = [".doc", ".docx", ".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]
zip_extensions = [".zip", ".rar", ".7z"]
psd_extensions = [".psd", ".psb"]
ae_extensions = [".aep"]

# Utility function to ensure unique filenames
def make_unique(dest, name):
    filename, extension = splitext(name)
    counter = 1
    while exists(f"{dest}/{name}"):
        name = f"{filename}({str(counter)}){extension}"
        counter += 1
    return name

# Move files to the destination directory
def move_file(dest, entry, name):
    if exists(f"{dest}/{name}"):
        unique_name = make_unique(dest, name)
        oldName = join(dest, name)
        newName = join(dest, unique_name)
        rename(oldName, newName)
    move(entry, dest)

# Event handler for file modifications
class MoverHandler(FileSystemEventHandler):
    def on_modified(self, event):
        with scandir(source_dir) as entries:
            for entry in entries:
                name = entry.name
                self.check_audio_files(entry, name)
                self.check_video_files(entry, name)
                self.check_image_files(entry, name)
                self.check_document_files(entry, name)
                self.check_zip_files(entry,name)
                self.check_psd_files(entry, name)
                self.check_ae_files(entry, name)

    def check_audio_files(self, entry, name):
        for audio_extension in audio_extensions:
            if name.endswith(audio_extension) or name.endswith(audio_extension.upper()):
                move_file(dest_dir_music, entry, name)

    def check_video_files(self, entry, name):
        for video_extension in video_extensions:
            if name.endswith(video_extension) or name.endswith(video_extension.upper()):
                move_file(dest_dir_video, entry, name)

    def check_image_files(self, entry, name):
        for image_extension in image_extensions:
            if name.endswith(image_extension) or name.endswith(image_extension.upper()):
                move_file(dest_dir_image, entry, name)

    def check_document_files(self, entry, name):
        for documents_extension in document_extensions:
            if name.endswith(documents_extension) or name.endswith(documents_extension.upper()):
                move_file(dest_dir_documents, entry, name)

    def check_psd_files(self, entry, name):
        for psd_extension in psd_extensions:
            if name.endswith(psd_extension) or name.endswith(psd_extension.upper()):
                move_file(dest_dir_photoshop, entry, name)

    def check_ae_files(self, entry, name):
        for ae_extension in ae_extensions:
            if name.endswith(ae_extension) or name.endswith(ae_extension.upper()):
                move_file(dest_dir_aftereffects, entry, name)
    def check_zip_files(self, entry, name):
        for zip_extension in zip_extensions:
            if name.endswith(zip_extension) or name.endswith(zip_extension.upper()):
                move_file(dest_dir_zip, entry, name)

# Main program execution
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source_dir
    event_handler = MoverHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
