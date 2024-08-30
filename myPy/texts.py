import os
import shutil

def proverka(p, destination_folder):
    copied_files = 0

    try:
        for item in os.scandir(p):
            if copied_files >= 200:
                break
            
            if item.is_file() and item.name.lower().endswith('.txt'):
                source_file_path = item.path
                file_size = os.path.getsize(source_file_path)

                if file_size <= 1024 * 1024:
                    shutil.copy2(source_file_path, destination_folder)
                    copied_files += 1

            elif item.is_dir():
                proverka(item.path, destination_folder)

    except PermissionError:
        pass
    except Exception as e:
        pass
