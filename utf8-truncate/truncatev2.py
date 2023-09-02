# UTF-8 truncation
# the cases file is in the format: every new line, the first byte returns an unsigned integer that signifies
# the length of the line
# this program truncates the strings accordingly so that the output.bin is equal to the expected file

with open('cases', 'rb') as f:
    hex_content = f.read()

with open('output.bin', 'wb') as output:
    length = 0
    i = 0
    while i < len(hex_content):
        length = hex_content[i]
        if length == 0:
            output.write(b'\n')
            while hex(hex_content[i]) != '0xa':
                i += 1
            i += 1
            continue
        end_index = i + length
        j = i
        i += 1
        for j in range(i, end_index):
            if hex(hex_content[j]) == '0xa':
                output.write(hex_content[i:j])
                output.write(b'\n')
                break
        i = j + 1
        if i == end_index:
            start = end_index - length + 1
            if (hex_content[end_index + 1] & 0xC0) == 0x80:  # if the next byte after the truncation has the form 10xxxxxx
                while (hex_content[end_index] & 0xC0) != 0xC0:  # move end_index backwards until before the start of the multibyte utf8
                    end_index -= 1
                end_index -= 1
            output.write(hex_content[start:end_index + 1])
            output.write(b'\n')
            while hex(hex_content[i]) != '0xa':
                i += 1
            i += 1
