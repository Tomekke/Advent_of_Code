def split_input_in_layers(input_array):
    layer_width = 25
    layer_heigth = 6
    num_pixel_layers = layer_width * layer_heigth
    layers = []
    i = 0
    while i < len(input_array):
        layers.append(input_array[i:i+num_pixel_layers])
        i += num_pixel_layers
    return layers


def find_colour(input):
    layers = split_input_in_layers(input)
    image = []
    i = 0
    while i < len(layers[0]):
        for layer in layers:
            if layer[i] != '2':
                image.append(layer[i])
                break
        i += 1
    return image


def draw_image(input, width, height):
    image_string = find_colour(input)
    x = 0
    while x < height:
        image = ''
        for y in range (0, width):
            colour = image_string[x*width+y]
            if colour == '0':
                image += ' '
            elif colour == '1':
                image += '#'
        x += 1
        print(image)


def read_and_execute(inputFile, width, heighth):
    with open(inputFile) as file:
        for line in file:
            draw_image(line, width, heighth)

#draw_image('0222112222120000', 2, 2)
#print(find_colour('0222112222120000'))
read_and_execute('Day8_InputFile', 25, 6)
#read_and_execute('Day8_TestInput', 6, 3)