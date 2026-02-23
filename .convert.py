import os
import subprocess

def convert_md_to_html():
    current_dir = os.getcwd()

    for filename in os.listdir(current_dir):
        if filename.lower().endswith(".md"):
            md_path = os.path.join(current_dir, filename)
            html_filename = os.path.splitext(filename)[0] + ".html"
            html_path = os.path.join(current_dir, html_filename)

            try:
                subprocess.run(
                    ["pandoc", md_path, "-s", "-o", html_path],
                    check=True
                )
                print(f"Converted: {filename} -> {html_filename}")
            except subprocess.CalledProcessError as e:
                print(f"Failed to convert {filename}: {e}")

if __name__ == "__main__":
    convert_md_to_html()

