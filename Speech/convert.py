import subprocess, os

# path to ffmpeg bin
FFMPEG_PATH = '/usr/local/bin/ffmpeg'

def convert(file_path):
    # create output directory if necessary
    if not os.path.isdir('./audio/converted'):
        os.makedirs('./audio/converted')

    file = file_path.split('/')[-1]
    name_without_extension = ''.join(file.split('.')[:-1])
    output = './audio/converted/{}.wav'.format(name_without_extension)
    
    try:
        # ffmpeg -i my_video.mp4 -threads 8 output_audio.wav 
        command = [
            FFMPEG_PATH, '-i', file_path, '-y', '-loglevel', '16','-threads', '8', output
        ]
        subprocess.call(command)  # call the ffmpeg command to convert
        file_to_remove = os.getcwd() + file_path[1:]
        rm_command = ['rm', file_to_remove]
        subprocess.call(rm_command)
    except Exception, e:
        print e

# convert('./retrieved_audio/13635218_10209465570533683_1943824153_n.mp4')