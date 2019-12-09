

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


def find_layer_with_less_zeroes(input):
    layers = split_input_in_layers(input)
    clean_layer = layers[0]
    for layer in layers:
        if layer.count('0') < clean_layer.count('0'):
            clean_layer = layer
    return clean_layer


def count_ones_and_twos(layer):
    return layer.count('1')*layer.count('2')


def read_and_execute(inputFile):
    result = -1
    with open(inputFile) as file:
        for line in file:
            result = count_ones_and_twos(find_layer_with_less_zeroes(line))
    return result


#print(count_ones_and_twos(find_layer_with_less_zeroes('123456789012')))
print(read_and_execute('Day8_InputFile'))
#print(read_and_execute('Day8_TestInput'))