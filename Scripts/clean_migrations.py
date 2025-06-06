import os

deleted = 0

for root, dirs, files in os.walk("."):
    if "migrations" in root:
        for file in files:
            if file.endswith(".pyc") or (file.endswith(".py") and file != "__init__.py"):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                    deleted += 1
                except Exception as e:
                    print(f"Failed to delete {file_path}: {e}")

print(f"\nTotal files deleted: {deleted}")