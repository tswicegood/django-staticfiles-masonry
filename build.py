"""
Relocates the files for a given version of Masonry from vendor/masonry
into a Django app for use with Django staticfiles.
"""
import subprocess
import sys

DEFAULT_VERSION = "2.1.05"


def cp(src):
    cmd = [
        "cp -R vendor/masonry/%s masonry/static/masonry/" % src,
    ]
    subprocess.call(cmd, shell=True)


def main():
    args = {
        "version": DEFAULT_VERSION if len(sys.argv) is 1 else sys.argv[1],
    }
    subprocess.call(["mkdir -p ./masonry/static/masonry"], shell=True)
    subprocess.call(
            ["cd vendor/masonry && git checkout v%(version)s" %args],
            shell=True)
    cp("/jquery.masonry*.js")

    with open("./VERSION", "w") as f:
        f.write(args["version"])


if __name__ == "__main__":
    main()
