from os import listdir, mkdir, path
from os.path import isfile, join

def get_files_path(path_):
    '''
        Given a path returns all the files under that path
        Input: 
            folderpath
        Output: 
            a list of files
    '''
    return [join(path_, f) for f in listdir(path_) if isfile(join(path_, f)) and f[0] != '.']


def get_subfolders_path(path_):
    '''
        Given a path returns all the folders under that path
        Input: 
            folderpath
        Output: 
            a list of subfolders
    '''
    return [join(path_, f) for f in listdir(path_) if not isfile(join(path_, f))]


def run_cmd(cmd):
    '''
        Given a shell command, it runs the command and returns the output and error
        Input:
            command
        Output:
            command output, error
    '''
    import subprocess
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output, error = process.communicate()
    return output,error


def read_csv(csv_path):
    import csv
    output = []

    with open(csv_path, 'r') as csvfile:
        reader = csv.reader(csvfile, quoting = csv.QUOTE_ALL)
        for row in reader: # each row is a list
            #row = [float(v) for v in row ]
            output.append(row)

    return output


def wait_folder_creation(path_):
    '''
        keeps on waiting until a folder at the given path is created
        Input:
            path to the folder
        Output:
            None
    '''
    import time
    while not path.exists(path_):
        time.sleep(1)


def create_folder(path_):
    '''
        Input:
            new folder path
        Output:
            0  if the folder is successfully created
            -1 if the folder already exists
            1  if the folder creation fails (print exception)
    '''
    try:
        success = mkdir(path_)
        wait_folder_creation(path_)
        return 0 
    except Exception as e:
        if path.exists(path_):
            return -1
        else:
            print(e)
            return 1


def sec_to_time(sec):
    micro_secs = int(divmod(sec,1)[1] * 1000000)
    mins, secs = divmod(int(sec), 60)
    hrs, mins = divmod(mins, 60)

    return time(hrs, mins, secs, micro_secs)


def get_frames_count(vid_frames_path):
    '''
        Input: 
            string - path of the extracted frames of a video numbered in %06d format starting from 1 
        Output: 
            int - count of frames in the path
    '''
    frames = get_files_path(vid_frames_path)
    frames.sort()
    
    idx = -1
    got_last_frame = False
    while not got_last_frame:
        try:
            last_frame_filename = frames[idx]
            count = int((last_frame_filename.split('/')[-1]).split('.')[0])
            got_last_frame = True
        except ValueError:
            idx -= 1
            continue

    return count


def path_exists(path_):
    return path.exists(path_)


def make_dir(path_):
    return mkdir(path_)
