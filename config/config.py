import os.path

current_dir = os.path.dirname(os.path.abspath(__file__))
rel_file_path = os.path.join(current_dir, "database.ini")
abs_file_path = os.path.abspath(rel_file_path)