import hashlib
import os
import collections
music_folder = 'C:\\Users\\Dorin\\Desktop\\mp3\\' # your folder, it can contain any crap you want


def file_hash(path, max_size=4000000):
    my_file = open(path, 'rb')
    hasher = hashlib.md5()
    buf = my_file.read(max_size)
    while len(buf) > 0:
        hasher.update(buf)
        buf = my_file.read(max_size)
    my_file.close()
    return hasher.hexdigest()


def get_files(path):
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list


def find_dupes(filelist):
    hashes = []
    for files in filelist:
        hashes.append(file_hash(files))
    h_dupes = [item for item, count in collections.Counter(hashes).items() if count > 1]
    d_complete = dict(zip(filelist, hashes))
    d_dupes = {}
    count = 0
    for key, value in d_complete.iteritems():
        if value in h_dupes:
            d_dupes[key] = value
    return d_dupes


def main():
    f_list = get_files(music_folder)
    d_dupes = find_dupes(f_list)
    for dupe in d_dupes:
        print dupe

main()