import sys
import pathlib
import cv2

def main():
  version()
  # Get filename from argument values.
  infilepath = get_input_file_path()
  if infilepath is None:
    print("ファイルパスを第一引数に与えてください")
    return
  # Convert filename to absolute path.
  infilepath = pathlib.Path(infilepath)
  print("ファイルパス：")
  print(infilepath.resolve())

  # Load image.
  image = cv2.imread(str(infilepath.resolve()))
  print(image.shape)

def version():
  print("-"*16)
  print("  sugar or salt")
  print("    ver.0.0.0")
  print("-"*16)

def get_input_file_path():
  args = sys.argv
  if len(args) < 2:
    return None
  return args[1]

main()
