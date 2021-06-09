import os
#absolute path
this_file_path = os.path.abspath(__file__)
print(this_file_path)

#parent dir
BASE_DIR = os.path.dirname(this_file_path)
ENTIRE_PROJECT_DIR = os.path.dirname(BASE_DIR)
print(BASE_DIR, ENTIRE_PROJECT_DIR)

#relative path
email_txt = os.path.join("template", "email.txt")
print(email_txt)
content = ""
with open(email_txt, 'r') as f:
    content = f.read()

print(content.format(name='Subham'))