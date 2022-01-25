'''
adapted from https://github.com/LINGuistLIU/fairseq_transformer_for_inflection/
'''
import sys, os, json

def reformat(fpred, fin, fout):
      with open(fpred) as fpred, open(fin) as fin, open(fout, 'w') as fw:      
          dict_pred = {}
          for line in fpred:
              if line[:2] == 'H-':
                  index, score, pred = line.strip().split('\t')
                  letter, num = index.split('-')
                  num = int(num)
                  dict_pred[num] = pred.replace(' ', '').replace('_', ' ') 
                  
          inputlines = [line.strip() for line in fin]
          for i, line in enumerate(inputlines):
              lines = line.strip().split('\t')
              if len(lines) <= 4 and len(lines) >= 2:
                  lemma = "".join(lines[0].split())
                  raw_msd = lines[-1].strip()
                  if raw_msd[0] == '+':
                    raw_msd = raw_msd[1:]
                  msd = raw_msd.replace(" ", ";")
              else:
                  print(i)
                  print('Please make sure each line in your file is a tab separated 2/3/4-column entry.')
              
              fw.write('\t'.join([lemma, dict_pred[i], msd]) + '\n')
          
            
          


if __name__ == '__main__':

    lang = sys.argv[1]
    lang_fam_dict = json.load(open('task0-data/lang2fam.json'))
    lang_dir_dict = json.load(open('task0-data/lang2dir.json'))
    # datadir = "task0-data/" + lang_dir_dict[lang] +  lang_fam_dict[lang] + '/'
    datadir = "data-bin/" + lang + "/test."
    
    fpred_dir = 'checkpoints/' + lang + '-predictions/'
    fout_dir = 'formatted_prediction/'
    
    fpred = fpred_dir + 'test-checkpoint_best.pt.txt'
    fin = datadir + lang + '.input' 
    fout = fout_dir + lang + '.output'
    
    if not os.path.exists(fout_dir):
        os.makedirs(fout_dir)

    print('reading language:', lang)
    
    if os.path.exists(fpred_dir):
        reformat(fpred, fin, fout)
 



