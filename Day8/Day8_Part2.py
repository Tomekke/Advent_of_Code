def split_input_in_layers(input_array):
    layer_width = 2
    layer_heigth = 2
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
            if layer[i] != '0':
                image.append(layer[i])
                i = 0
                break
            i += 1
    return image


print(find_colour('0222112222120000'))