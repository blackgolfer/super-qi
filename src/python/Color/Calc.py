import colorsys

def rgb2hex(val:tuple[int,int,int])->str:
    """
    Takes tuple and converts to hex value.
    """
    conversion = '#%02x%02x%02x' % val
    return conversion
 
def hex2rgb(val:str)->tuple[int,int,int]:
    """
    Takes hex string and converts to rgb tuple.
    """
    hexNum = val.strip('#')
    hexLen = len(hexNum)
    conversion = tuple(int(hexNum[i:i+hexLen//3], 16) for i in range(0, hexLen, hexLen//3))
    return conversion

def complementary(val:tuple[int,int,int])->tuple[int,int,int]:
    """
    Takes rgb tuple and produces complimentary color.
    """
    #value has to be 0 < x 1 in order to convert to hls
    r, g, b = map(lambda x: x/255.0, val)
    #hls provides color in radial scale
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    #get hue changes at 150 and 210 degrees
    deg_180_hue = h + (180.0 / 360.0)
    color_180_rgb = tuple(map(lambda x: round(x * 255),colorsys.hls_to_rgb(deg_180_hue, l, s)))
    return color_180_rgb

def rgb_complementary(c:tuple[int,int,int])->tuple[int,int,int]:
    return tuple(map(lambda x:255-x,c))

def shade(c:tuple[int,int,int],factor:float)->tuple[int,int,int]:
    return tuple(map(lambda x:int(x*(1-factor)),c))

def tint(c:tuple[int,int,int],factor:float)->tuple[int,int,int]:
    return tuple(map(lambda x:int(x+(255-x)*(1-factor)),c))

def triadic(val:tuple[int,int,int])->list[tuple[int,int,int]]:
    """
    Takes rgb tuple and produces list of triadic colors.
    """
    #value has to be 0 < x 1 in order to convert to hls
    r, g, b = map(lambda x: x/255.0, val)
    #hls provides color in radial scale
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    #get hue changes at 120 and 240 degrees
    deg_120_hue = h + (120.0 / 360.0)
    deg_240_hue = h + (240.0 / 360.0)
    #convert to rgb
    color_120_rgb = tuple(map(lambda x: round(x * 255),colorsys.hls_to_rgb(deg_120_hue, l, s)))
    color_240_rgb = tuple(map(lambda x: round(x * 255),colorsys.hls_to_rgb(deg_240_hue, l, s)))
    return [color_120_rgb, color_240_rgb]

def tetradic(val:tuple[int,int,int])->list[tuple[int,int,int]]:
    """
    Takes rgb tuple and produces list of tetradic colors.
    """
    #value has to be 0 <span id="mce_SELREST_start" style="overflow:hidden;line-height:0;"></span>&lt; x 1 in order to convert to hls
    r, g, b = map(lambda x: x/255.0, val)
    #hls provides color in radial scale
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    #get hue changes at 120 and 240 degrees
    deg_60_hue = h + (60.0 / 360.0)
    deg_180_hue = h + (180.0 / 360.0)
    deg_240_hue = h + (240.0 / 360.0)
    #convert to rgb
    color_60_rgb = tuple(map(lambda x: round(x * 255),colorsys.hls_to_rgb(deg_60_hue, l, s)))
    color_180_rgb = tuple(map(lambda x: round(x * 255),colorsys.hls_to_rgb(deg_180_hue, l, s)))
    color_240_rgb = tuple(map(lambda x: round(x * 255),colorsys.hls_to_rgb(deg_240_hue, l, s)))
    return [color_60_rgb, color_180_rgb, color_240_rgb]

def add(a:str,b:str)->str:
    rgb1=hex2rgb(a); rgb2=hex2rgb(b)
    return rgb2hex(tuple(map(lambda x:x[0]+x[1],zip(rgb1,rgb2))))

def luminance(c:str)->float:
    color = c[1:]
    hex_red = int(color[0:2], base=16)
    hex_green = int(color[2:4], base=16)
    hex_blue = int(color[4:6], base=16)
    return hex_red * 0.2126 + hex_green * 0.7152 + hex_blue * 0.0722

def foreground(c:str)->str:
    l=luminance(c)
    if l<140: return '#ffffff'
    else: return '#000000'