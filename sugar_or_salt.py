import sys

def main():
  version()
  # ファイル名取得
  infilepath = get_input_file_path()
  if infilepath is None:
    print("ファイルパスを第一引数に与えてください")
    return
  print("ファイルパスは" + infilepath + "です")

def version():
  print("-"*12)
  print("sugar or salt")
  print("ver.0.0.0")
  print("-"*12)

def get_input_file_path():
  args = sys.argv
  if len(args) < 2:
    return None
  return args[1]

main()
