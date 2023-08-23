import sys
# Convert simple.css from hx colors to rgb colors
# split the string into an array, from which we can separate the elements that start with #
# loop over those elements, and append every two characters into a list. so #fe030a; to [fe, 03, 0a]
# loop over that list, for each element, append its equivalent in numbers to another list
# now we have the last created list filled with numbers
# string.replace(elements from old list (#fe030a;) to elements from new list (in numbers) )


hex_to_numbers_dict = dict(zip('0123456789abcdef', range(16)))

strr = sys.stdin.read()

str_split = strr.split()

colors = [color for color in str_split if color.startswith('#') and color.endswith(';')]
list_of_colors = []
for color in colors:
    if len(color) >= 8:
      list_of_colors.append([color[i:i+2] for i in range(1, len(color)-1, 2)])
    elif len(color) == 5 or len(color) == 6:
      list_of_colors.append([2*color[i] for i in range(1, len(color)-1)])
    else:
      list_of_colors.append([color[i:i+2] for i in range(1, len(color)-1, 2)])

print('list_of_colors: ', list_of_colors)
list_of_colors_transformed = []
for index, color in enumerate(list_of_colors):
    print("LENGTH: ", len(color))
    color_transformed = []
    for i, hx in enumerate(color):
        if (i == 3):
           color_transformed.append('/ ' + str((hex_to_numbers_dict[hx[0]]*16 + hex_to_numbers_dict[hx[1]])/255))
        else:
          color_transformed.append(str(hex_to_numbers_dict[hx[0]]*16 + hex_to_numbers_dict[hx[1]]))
    list_of_colors_transformed.append(' '.join(color_transformed))

print('list_of_colors_transformed: ', list_of_colors_transformed)
new_str = strr      
for index, color in enumerate(colors):

    new_str = new_str.replace(color, 'rgb(' + list_of_colors_transformed[index] + ');')

print(new_str)
