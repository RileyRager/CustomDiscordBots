import os

commit_description = input("What do you want the commit reason to be (required): ")

os.system("git add --all")
os.system(f'git commit -m "{commit_description}"')
os.system("git push")
os.system("git pull")
