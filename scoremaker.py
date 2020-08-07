# coding=utf-8
import re
from PIL import Image, ImageDraw, ImageFont

#####  define  #####
alpha = 125
note_image_width = 31
note_image_height = 12
delta_note_image_width = 5
delta_unit_width = 120
image_left_right = 60
image_top_bottom = 60
unit_width = (note_image_width + delta_note_image_width * 2) * 7
unit_height = int(note_image_height * (64 + 16))
row_list = [6, 1, 2, 3, 4, 5, 8]

#####  read resource  #####

note_flick = Image.open("images/note_flick.png")
note_flick = note_flick.resize((note_image_width, note_image_height), Image.ANTIALIAS)
flick_r, flick_g, flick_b, flick_a = note_flick.split()

note_long = Image.open("images/note_long.png")
note_long = note_long.resize((note_image_width, note_image_height), Image.ANTIALIAS)
long_r, long_g, long_b, long_a = note_long.split()

note_normal = Image.open("images/note_normal.png")
note_normal = note_normal.resize((note_image_width, note_image_height), Image.ANTIALIAS)
normal_r, normal_g, normal_b, normal_a = note_normal.split()

note_skill = Image.open("images/note_skill.png")
note_skill = note_skill.resize((note_image_width, note_image_height), Image.ANTIALIAS)
skill_r, skill_g, skill_b, skill_a = note_skill.split()


def run(music_info, note_info, music_score):
    score_image = create_image(music_info, note_info, music_score, )
    return score_image


#####  create score image  ######
def create_image(music_info, note_info, music_score):
    total_unit = int(music_score[-1]['unitid'])
    music_info['combo'] = 0

    # create image
    image_width = (int(total_unit / 4) + 1) * (unit_width + delta_unit_width)
    image_height = 4 * unit_height + image_top_bottom * 2
    music_score_image = Image.new('RGB', (image_width, image_height), (0, 0, 0, 100))

    # draw score lines
    draw = ImageDraw.Draw(music_score_image, 'RGBA')
    font = ImageFont.truetype(font="arial.ttf", size=30)
    big_line_list = []
    for i in range((int(total_unit / 4) + 1) * 2):
        x = image_left_right + i * (unit_width + delta_unit_width)
        # top left
        big_line_list.append((x, -10))
        # bottom left
        big_line_list.append((x, image_height + 10))
        # bottom right
        big_line_list.append((x + unit_width, image_height + 10))
        # top right
        big_line_list.append((x + unit_width, -10))

        for j in range(6):
            small_line_list = []
            # small line i top
            small_line_list.append((x + (j + 1) * (note_image_width + delta_note_image_width * 2), -10))
            # small line i bottom
            small_line_list.append((x + (j + 1) * (note_image_width + delta_note_image_width * 2), image_height + 10))
            draw.line(small_line_list, fill=(255, 255, 255), width=1)

    draw.line(big_line_list, fill=(137, 207, 240), width=5)

    # drow unit lines and text
    for i in range(total_unit + 2):
        x = image_left_right + int(i / 4) * (unit_width + delta_unit_width)
        y = image_height - (i % 4) * unit_height - image_top_bottom
        line_list = [(x, y), (x + unit_width, y)]
        draw.line(line_list, fill=(255, 255, 255), width=2)
        line_list = [(x, y - unit_height), (x + unit_width, y - unit_height)]
        draw.line(line_list, fill=(255, 255, 255), width=2)

        text_size = font.getsize(str(i))
        draw.text((x - text_size[0] - 5, y - 16), str(i), font=font, fill=(255, 255, 255))

        if i % 4 == 0:
            draw.text((x - text_size[0] - unit_width - delta_unit_width - 5, image_top_bottom - 16), str(i), font=font, fill=(255, 255, 255))

    polygon_list = {
        'a': {},
        'a_end': {},
        'b': {},
        'b_end': {},
    }
    green_note_paste_list = []
    paste_image = True
    last_unitid = 0
    line_slide_positions = []
    # draw notes
    # when drawing type 1 slide, if at last have one ,needs one more loop to draw the last slide
    # so set max u equals len(music_score), and droop after the drawing
    for u in range(len(music_score) + 1):
        if u != len(music_score):
            unitid = int(music_score[u]['unitid'])
            score_note_type = int(music_score[u]['type'])
            row = int(music_score[u]['row'])
            list = re.findall('.{2}', music_score[u]['list'])

        if unitid == 0:
            last_unitid = unitid
            continue

        if last_unitid != unitid or u == len(music_score):
            # draw combo
            if u == len(music_score):
                tempunitid = unitid + 1
            else:
                tempunitid = unitid

            x = image_left_right + int(tempunitid / 4) * (unit_width + delta_unit_width)
            y = image_height - (tempunitid % 4) * unit_height - image_top_bottom

            text_size = font.getsize(str(music_info['combo']))
            draw.text((x - text_size[0] - 5, y + 16), str(music_info['combo']), font=font, fill=(255, 255, 255))

            if tempunitid % 4 == 0:
                text_size = font.getsize(str(music_info['combo']))
                draw.text((x - text_size[0] - unit_width - delta_unit_width - 5, image_top_bottom + 16), str(music_info['combo']), font=font, fill=(255, 255, 255))

            # sort polygon list
            a_index_list = sorted(polygon_list['a'])
            a_end_index_list = sorted(polygon_list['a_end'])
            b_index_list = sorted(polygon_list['b'])
            b_end_index_list = sorted(polygon_list['b_end'])

            a_slide_index_list = sorted(a_index_list + a_end_index_list)
            b_slide_index_list = sorted(b_index_list + b_end_index_list)

            # draw slide
            for type in ['a', 'b']:
                if type == 'a':
                    slide_index_list = a_slide_index_list
                    index_list = a_index_list
                    end_index_list = a_end_index_list
                elif type == 'b':
                    slide_index_list = b_slide_index_list
                    index_list = b_index_list
                    end_index_list = b_end_index_list

                index_list_num = len(index_list)
                end_index_list_num = len(end_index_list)
                range_num = len(slide_index_list)

                if index_list_num == 0 or end_index_list_num == 0:
                    continue

                start_note_index = 0
                for i in range(range_num):
                    # check slide end
                    if slide_index_list[i] not in polygon_list[type + '_end']:
                        continue
                    else:
                        end_note_index = i
                    # draw slide
                    slide_end = False
                    for j in range(start_note_index, end_note_index + 1):
                        if slide_index_list[j] in polygon_list[type]:
                            start_note = polygon_list[type][slide_index_list[j]]
                        else:
                            break

                        if j + 1 != end_note_index:
                            end_note = polygon_list[type][slide_index_list[j + 1]]
                        else:
                            end_note = polygon_list[type + '_end'][slide_index_list[j + 1]]
                            slide_end = True

                        # check new row
                        if start_note[1] > end_note[1]:
                            # check new unit first
                            if start_note[1] == image_height - image_top_bottom:
                                green_slide_list = [
                                    (start_note[0] - unit_width - delta_unit_width, image_height - start_note[1]),
                                    (end_note[0] - unit_width - delta_unit_width, end_note[1] - image_height + image_top_bottom * 2),
                                    (end_note[0] + note_image_width - unit_width - delta_unit_width, end_note[1] - image_height + image_top_bottom * 2),
                                    (start_note[0] + note_image_width - unit_width - delta_unit_width, image_height - start_note[1])
                                ]
                                draw.polygon(green_slide_list, fill=(0, 255, 0, alpha))

                                green_note_paste_list.append([note_long, (start_note[0] - unit_width - delta_unit_width, image_height - start_note[1] - int(note_image_height / 2)), long_a])

                            # not new row
                            green_slide_list = [
                                (start_note[0], start_note[1]),
                                (end_note[0], end_note[1]),
                                (end_note[0] + note_image_width, end_note[1]),
                                (start_note[0] + note_image_width, start_note[1])
                            ]
                        else:
                            # draw bottom
                            green_slide_list = [
                                (start_note[0] + unit_width + delta_unit_width, image_height + start_note[1] - image_top_bottom * 2),
                                (end_note[0], end_note[1]),
                                (end_note[0] + note_image_width, end_note[1]),
                                (start_note[0] + note_image_width + unit_width + delta_unit_width, image_height + start_note[1] - image_top_bottom * 2)
                            ]
                            draw.polygon(green_slide_list, fill=(0, 255, 0, alpha))

                            green_note_paste_list.append(
                                [note_long, (end_note[0] - unit_width - delta_unit_width, image_top_bottom * 2 - image_height + end_note[1] - int(note_image_height / 2)), long_a])

                            # new row
                            green_slide_list = [
                                (start_note[0], start_note[1]),
                                (end_note[0] - unit_width - delta_unit_width, image_top_bottom * 2 - image_height + end_note[1]),
                                (end_note[0] + note_image_width - unit_width - delta_unit_width, image_top_bottom * 2 - image_height + end_note[1]),
                                (start_note[0] + note_image_width, start_note[1])
                            ]

                        draw.polygon(green_slide_list, fill=(0, 255, 0, alpha))

                        # del start note in the list
                        del polygon_list[type][slide_index_list[j]]
                        if slide_end:
                            del polygon_list[type + '_end'][slide_index_list[j + 1]]
                            break

                    start_note_index = end_note_index + 1

        if u == len(music_score):
            break

        # in some score file, line slide is defined by 5
        # in some score file, line slide and other slide are both defined in 1
        if score_note_type == 1:
            # get rate
            delta_row = int(unit_height / len(list))
            note_in_unit_location = -1

            for note in list:
                note_in_unit_location += 1
                if note == '00':
                    continue
                elif note in note_info:
                    music_info['combo'] += 1

                    # get paste point
                    unit_location = (image_left_right + int(unitid / 4) * (unit_width + delta_unit_width),
                                     image_height - unitid % 4 * unit_height - image_top_bottom)
                    x = unit_location[0] + row_list.index(row) * (note_image_width + delta_note_image_width * 2) + delta_note_image_width
                    y = unit_location[1] - note_in_unit_location * delta_row - int(note_image_height / 2)

                    # get paste image and paste mask
                    if note_info[note] == 'bd' or note_info[note] == 'fever_note':
                        # normal note
                        paste_image = note_normal
                        paste_mask = normal_a
                    elif note_info[note] == 'skill':
                        # skill note
                        paste_image = note_skill
                        paste_mask = skill_a
                    elif note_info[note] == 'flick' or note_info[note] == 'fever_note_flick':
                        # flick note
                        paste_image = note_flick
                        paste_mask = flick_a
                    elif note_info[note] == 'slide_end_flick_a' or note_info[note] == 'slide_end_flick_b':
                        # flick note
                        slide_type = note_info[note][-1:]
                        polygon_list[slide_type + '_end'][note_in_unit_location * delta_row + unitid * unit_height] = [x, y + int(note_image_height / 2)]

                        green_note_paste_list.append([note_flick, (x, y), flick_a])
                        paste_image = False

                    elif note_info[note] == 'slide_a' or note_info[note] == 'slide_b' or note_info[note] == 'slide_end_a' or note_info[note] == 'slide_end_b':
                        # slide note
                        # get info
                        info = re.split('_', note_info[note])
                        if len(info) == 2:
                            # start
                            slide_type = info[1]
                            polygon_list[slide_type][note_in_unit_location * delta_row + unitid * unit_height] = [x, y + int(note_image_height / 2)]

                        elif len(info) == 3:
                            # end
                            slide_type = info[2]
                            polygon_list[slide_type + '_end'][note_in_unit_location * delta_row + unitid * unit_height] = [x, y + int(note_image_height / 2)]

                        green_note_paste_list.append([note_long, (x, y), long_a])
                        paste_image = False
                    else:
                        print(note_info[note] + 'is not support (score_note_type = 1)')
                        continue

                    # paste note image
                    if paste_image:
                        # check new row
                        if unitid % 4 == 0 and note_in_unit_location == 0:
                            music_score_image.paste(paste_image, (x - unit_width - delta_unit_width, image_height - y - note_image_height), paste_mask)

                        music_score_image.paste(paste_image, (x, y), paste_mask)
                    else:
                        paste_image = True
        elif score_note_type == 5:
            # get rate
            delta_row = int(unit_height / len(list))
            note_in_unit_location = -1

            for note in list:
                note_in_unit_location += 1
                if note == '00':
                    continue
                elif note in note_info:
                    music_info['combo'] += 1
                    # get paste point
                    unit_location = (image_left_right + int(unitid / 4) * (unit_width + delta_unit_width), image_height - unitid % 4 * unit_height - image_top_bottom)
                    x = unit_location[0] + row_list.index(row) * (note_image_width + delta_note_image_width * 2) + delta_note_image_width
                    y = unit_location[1] - note_in_unit_location * delta_row - int(note_image_height / 2)

                    # get paste image and paste mask
                    if note_info[note] == 'bd' or note_info[note] == 'fever_note':
                        # normal note
                        slide_image = note_long
                        slide_mask = long_a
                    elif note_info[note] == 'flick' or note_info[note] == 'fever_note_flick':
                        # normal note
                        slide_image = note_flick
                        slide_mask = flick_a
                    elif note_info[note] == 'skill':
                        # normal note
                        slide_image = note_skill
                        slide_mask = skill_a
                    else:
                        print(note_info[note] + 'is not support (score_note_type = 5)')
                        continue

                    if line_slide_positions == []:
                        line_slide_positions.append([x, y + int(note_image_height / 2)])
                    else:
                        new_slide_start_note = True
                        for line_slide_position in line_slide_positions:
                            # check new row
                            if line_slide_position[0] == x - unit_width - delta_unit_width:
                                new_slide_start_note = False
                                # draw top
                                line_slide_end_position = [x - unit_width - delta_unit_width, y + image_top_bottom * 2 - image_height + int(note_image_height / 2)]
                                green_slide_list = [
                                    (line_slide_position[0], line_slide_position[1]),
                                    (line_slide_end_position[0], line_slide_end_position[1]),
                                    (line_slide_end_position[0] + note_image_width, line_slide_end_position[1]),
                                    (line_slide_position[0] + note_image_width, line_slide_position[1])
                                ]
                                draw.polygon(green_slide_list, fill=(0, 255, 0, alpha))
                                green_note_paste_list.append([note_long, (line_slide_end_position[0], line_slide_end_position[1] - int(note_image_height / 2)), long_a])

                                # draw bottom
                                line_slide_end_position = [x, y - int(note_image_height / 2)]
                                green_slide_list = [
                                    (line_slide_position[0] + unit_width + delta_unit_width, image_height + line_slide_position[1]),
                                    (line_slide_end_position[0], line_slide_end_position[1] + note_image_height),
                                    (line_slide_end_position[0] + note_image_width, line_slide_end_position[1] + note_image_height),
                                    (line_slide_position[0] + note_image_width + unit_width + delta_unit_width, image_height + line_slide_position[1])
                                ]
                                draw.polygon(green_slide_list, fill=(0, 255, 0, alpha))

                                del line_slide_positions[line_slide_positions.index(line_slide_position)]

                            elif line_slide_position[0] == x:
                                new_slide_start_note = False
                                # same row
                                line_slide_end_position = [x, y + int(note_image_height / 2)]
                                green_slide_list = [
                                    (line_slide_position[0], line_slide_position[1]),
                                    (line_slide_end_position[0], line_slide_end_position[1]),
                                    (line_slide_end_position[0] + note_image_width, line_slide_end_position[1]),
                                    (line_slide_position[0] + note_image_width, line_slide_position[1])
                                ]

                                draw.polygon(green_slide_list, fill=(0, 255, 0, alpha))
                                del line_slide_positions[line_slide_positions.index(line_slide_position)]

                        # not the same row, add it to position list
                        if new_slide_start_note:
                            line_slide_positions.append([x, y + int(note_image_height / 2)])

                    green_note_paste_list.append([slide_image, (x, y), slide_mask])

        last_unitid = unitid

    # paste green note
    for green_note in green_note_paste_list:
        music_score_image.paste(green_note[0], green_note[1], green_note[2])

    return music_score_image
