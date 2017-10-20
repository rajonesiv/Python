def rgb_hex():
  invalid_msg = "You have entered invalid values!"
  red = int(raw_input("Enter a value for Red: "))
  if red < 0 | red > 255:
    print invalid_msg
  green = int(raw_input("Enter a value for Green: "))
  if green < 0 | green > 255:
    print invalid_msg
  blue = int(raw_input("Enter a value for Blue: "))
  if blue < 0 | blue > 255:
    print invalid_msg
  val = (red << 16) + (green << 8) + blue
  print "%s" % (hex(val)[2:]).upper()
  
def hex_rgb():
  hex_val = raw_input("Enter a hexadecimal value: ")
  if len(hex_val) != 6:
    print "You have entered an invalid value!"
    return
  else:
    hex_val = int(hex_val, 16)
  two_hex_digits = 2**8
  blue = hex_val % two_hex_digits
  hex_val= hex_val >> 8
  green = hex_val % two_hex_digits
  hex_val = hex_val >> 8
  red = hex_val % two_hex_digits
  print "Red: %s Green: %s Blue: %s" % (red, green, blue)
  
def convert():
  while(True):
    option = raw_input("Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to Exit: ")
    if option == '1':
      print "RGB to Hex..."
      rgb_hex()
    elif option == '2':
      print "Hex to RGB..."
      hex_rgb()
    elif option == 'X' | option == 'x':
      print "Exiting..."
      break
    else:
      print "Error"

convert()