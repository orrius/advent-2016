from collections import Counter
from string import ascii_lowercase
import re
import unittest
from operator import itemgetter
from pathlib import Path


def sum_real_sector_ids():
    count = 0
    with (Path(__file__).parent / 'four_input.txt').open() as f:
        for room in f:
            letters, sector_id, checksum = parse_room(room)
            counts = Counter(letters.replace('-', ''))
            sorted_count = sorted(counts.items(), key=itemgetter(0))
            sorted_count = sorted(sorted_count, key=itemgetter(1), reverse=True)
            if all(check == letter[0] for check, letter in zip(checksum, sorted_count)):
                count += int(sector_id)
                real_room_name = decrypt_room_name(letters, int(sector_id))
                if 'north' in real_room_name:
                    print('{} has sector_id: {}'.format(real_room_name, sector_id))
    return count

regex = re.compile('([a-z\-]*)([\d]*)\[([a-z]*)\]')

def parse_room(room):
    return regex.match(room).groups()

def decrypt_room_name(letters, sector_id):
    rotations = sector_id % len(ascii_lowercase)
    decrypted_name = ''
    for letter in letters:
        if letter not in ascii_lowercase:
            decrypted_name += letter
            continue
        start_index = ascii_lowercase.index(letter)
        final_index = start_index + rotations
        if final_index > len(ascii_lowercase) - 1:
            final_index = final_index - len(ascii_lowercase)
        decrypted_name += ascii_lowercase[final_index]
    return decrypted_name


print('The sum of all real sector_ids is: {}'.format(sum_real_sector_ids()))
