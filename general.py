from os import path, mkdir


# chinhem
# chinhem.com


# each website need to be separated into different projects
def make_new_dir(directory):
    if not path.exists(directory):
        mkdir(directory)
    return


# wire file
def write_file(file_name, content):
    with open(file_name, 'w') as f:
        f.write(content)


# Create queue and crawled files 
def create_data_files(project_name, base_url):
    queue = project_name + '\queue.txt'
    crawled = project_name + '\crawled.txt'
    if not path.isfile(queue):
        write_file(queue, base_url + '\n')
    if not path.isfile(crawled):
        write_file(crawled, '')


# append data
def append_to_file(path, data):
    with open(path, 'a') as f:
        f.write(data + '\n')


# delete file's content
def del_file_content(path):
    with open(path, 'w') as f:
        f.write('')


# read a file and convert each line to set items
def file_to_set(file_name):
    result = set()
    with open(file_name, 'rt') as f:
        for line in f:
            result.add(line.replace('\n', ''))
    return result


# convert set to file
def set_to_file(links, file):
    del_file_content(file)
    for link in sorted(links):
        append_to_file(file, link)
