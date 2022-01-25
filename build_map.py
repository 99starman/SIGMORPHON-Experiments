import sys, os


def get_alphabet(lang):
  target_line = False
  with open('data-bin/alpha.all', 'r') as al:
    for line in al:
      items = line.split()
      if target_line == True:
        ret_chars = set(items)
        return ret_chars
      if items and items[0] == lang:
        target_line = True
    print("error: lang alphabet not obtained")
    return 0


def construct_map(lang, io_type):   # e.g. construct_map('krl', 'input')
  alpha = get_alphabet(lang)
  if not alpha:
    return 0
  fpath = 'data-bin/' + lang + '/dict.' + lang + '.'+ io_type + '.txt'
  char_type_map = ["padding", "padding", "padding", "padding"] # first 4 paddings: bos, pad, eos, unk
  with open(fpath, 'r') as f:
    for line in f:
      if line.split()[0] in alpha:
        char_type_map.append("character")
      else:
        char_type_map.append("grammatical_symbol")
  return char_type_map  
  
  
def write_to_file(lang, fout):
  fout = open(fout, 'w')
  map = construct_map(lang, 'input')  
  for item in map:
    fout.write(item + '\n')
  
  
if __name__ == '__main__':
  lang = sys.argv[1]
  fpath = 'data-bin/' + lang + '_map.txt'
  write_to_file(lang, fpath)