import argparse
import re


def set_version(conf_file, version):
    if version == "":
        version = "0.0.1"
    elif re.match(".*(\d)+\.(\d)+\.(\d)+.*", version):
        version = (re.search("(\d)+\.(\d)+\.(\d)+", version)).group()
    else:
        print("An invalid version number was tagged " + version)
        exit(1)
    print("Updating app.conf file with version number: " + version)
    with open(conf_file, "r") as file:
        lines = file.readlines()
    with open(conf_file, "w") as file:
        for line in lines:
            file.write(re.sub(r"VERSION", version, line))
    with open(".env", "w") as env_file:
        env_file.write(f'export VERSION="{version}"')
    file.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=str)
    parser.add_argument("--version", type=str)
    args = parser.parse_args()
    set_version(args.file, args.version)


if __name__ == "__main__":
    main()
