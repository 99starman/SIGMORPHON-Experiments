import sys, os, json

def reformat(fname, finputname, foutputname):
    with open(fname) as f, \
        open(finputname, 'w') as finput, \
        open(foutputname, 'w') as foutput:
        for line in f:
            lines = line.strip().split('\t')
            lemma = lines[0].strip().replace(' ', '_')
            msd = '+' + lines[-1].strip().replace(' ', '_')   # append '+' to the front
            if len(lines) == 3:
                form = lines[1].strip().replace(' ', '_')
            elif len(lines) == 2:
                form = '-'
            else:
                print('Please make sure each line in your file is a tab separated 3-column entry.')
            pos = msd.split(';')[0]
            if '.' in pos:
                pos = pos.split('.')[0]
            #input = [letter for letter in lemma] + [pos, 'CANONICAL'] + ['#'] + [tag for tag in msd.split(';')]
            input = [letter for letter in lemma] + ["\t"] + [tag for tag in msd.split(';')]
            output = [letter for letter in form]
            finput.write(' '.join(input) + '\n')
            foutput.write(' '.join(output) + '\n')

if __name__ == '__main__':

    path_prefix = 'task0-data/'

    lang_fam_dict = json.load(open(path_prefix + 'lang2fam.json'))

    lang_dir_dict = json.load(open(path_prefix + 'lang2dir.json'))

    lang = sys.argv[1]

    datadir = path_prefix + lang_dir_dict[lang]


    train = datadir + lang_fam_dict[lang] + '/' + lang + '.trn'
    trainin = 'train.' + lang + '.input'
    trainout = 'train.' + lang + '.output'

    # print('training data:', train)
    if os.path.exists(train):
        reformat(train, trainin, trainout)

    dev = datadir + lang_fam_dict[lang] + '/' + lang + '.dev'
    devin = 'dev.' + lang + '.input'
    devout = 'dev.' + lang + '.output'

    # print('dev data:', dev)
    if os.path.exists(dev):
        reformat(dev, devin, devout)

    test = datadir + lang_fam_dict[lang] + '/' + lang + '.tst'
    testin = 'test.' + lang + '.input'
    testout = 'test.' + lang + '.output'

    # print('test data:', test)
    if os.path.exists(test):
        reformat(test, testin, testout)