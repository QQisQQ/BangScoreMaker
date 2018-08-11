# coding=utf-8
import sys
import re
import scoremaker

#####  define  #####
music_info_key_word = {
    'bpm': '#BPM (\d*)',
    'id': '#WAV01 bgm(\d*).wav',
}
#####  read file  ######
def read_file(file_name):
    file_object = open('musicscore/' + file_name,'rU')

    music_info = {}
    note_info = {}
    music_score = []

    read_step = 0
    try:
        for line in file_object:
            if read_step == 0:
                # get music info
                for key_word in music_info_key_word:
                    info = re.match(music_info_key_word[key_word], line)
                    if info:
                        music_info[key_word] = info.group(1)

            # get note info
            info = re.match('#WAV(\d\w) (\w*).wav', line)
            if info:
                if read_step == 0:
                    read_step += 1
                    continue
                elif read_step == 1:
                    note_info[info.group(1)] = info.group(2)

            # get music score
            if line == '*---------------------- MAIN DATA FIELD\n':
                read_step += 1
                continue

            if read_step == 2:
                info = re.match('#(\d\d\d)(\d)(\d):(\w*)', line)

                if info:
                    music_score.append({
                        'unitid': info.group(1),
                        'type': info.group(2),
                        'row': info.group(3),
                        'list': info.group(4),
                    })
    finally:
         file_object.close()

    return music_info, note_info, music_score

def run(file_name):
    music_info, note_info, music_score = read_file(file_name)
    score_image = scoremaker.run(music_info, note_info, music_score)
    print('music information:\nBPM:%s\nBGM:%s\nCombo:%s\n' % (music_info['bpm'], music_info['id'], music_info['combo']))
    score_image.show()

def main(argv):
    run(argv[0])

if __name__ == "__main__":
    main(sys.argv[1:])