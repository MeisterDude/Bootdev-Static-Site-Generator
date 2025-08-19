
import os
import sys
import shutil

from generate_page import generate_page


def copy_static_to_public():
    """
    Copies static files from the 'static' directory to the 'public' directory.
    """
    static_dir = os.path.join(os.getcwd(), 'static')
    public_dir = os.path.join(os.getcwd(), 'public')

    if os.path.exists(public_dir):
        shutil.rmtree(public_dir)
    os.mkdir(public_dir)

    copy_dir(static_dir, public_dir)

def copy_dir(source, destination):
    for item in os.listdir(source):
        if os.path.isdir(os.path.join(source, item)):
            new_destination = os.path.join(destination, item)
            os.mkdir(new_destination)
            copy_dir(os.path.join(source, item), new_destination)
        else:
            shutil.copy(os.path.join(source, item), destination)

def generate_pages(basepath):
    """
    Generates pages by reading markdown files from the 'content' directory,
    processing them, and writing the output to the 'public' directory using a template.
    """
    content_dir = os.path.join(os.getcwd(), 'content')
    template_path = os.path.join(os.getcwd(), 'template.html')
    public_dir = os.path.join(os.getcwd(), 'public')
    generate_pages_directories(content_dir, public_dir, template_path)

def generate_pages_directories(content_dir, public_dir, template_path, basepath):
    for filename in os.listdir(content_dir):
        
        if os.path.isdir(os.path.join(content_dir, filename)):
            #print(filename)
            new_public_dir = os.path.join(public_dir, filename)
            os.mkdir(new_public_dir)
            new_content_dir = os.path.join(content_dir, filename)
            generate_pages_directories(new_content_dir, new_public_dir, template_path)
        elif os.path.isfile(os.path.join(content_dir, filename)) and filename.endswith('.md'):
            #print(f"Generating page for {filename}")
            from_path = os.path.join(content_dir, filename)
            dest_path = os.path.join(public_dir, filename.replace('.md', '.html').replace("content", "public"))
            generate_page(from_path, template_path, dest_path, basepath)


def main():
    basepath = sys.argv[0]
    if not basepath:
        basepath = "/"
    #print(f"Running script from: {basepath}")
    copy_static_to_public()
    generate_pages(basepath)


if __name__ == "__main__":
    main()