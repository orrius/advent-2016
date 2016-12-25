import hashlib

def calculate_next_hash(door_id, begin):
    while(True):
        to_hash = door_id + bytes(str(begin), encoding='utf-8')
        hasher = hashlib.md5()
        hasher.update(to_hash)
        hash = hasher.hexdigest()
        begin += 1
        if hash[:5] == '00000':
            return hash[5], begin

def generate_password(door_id):
    password = ''
    begin = 0
    bytes_door_id = bytes(door_id, encoding='utf-8')
    for _ in range(8):
        next_char, begin = calculate_next_hash(bytes_door_id, begin)
        password += next_char
    return password

print('The password for door_id ffykfhsq is: {}'.format(generate_password('ffykfhsq')))
