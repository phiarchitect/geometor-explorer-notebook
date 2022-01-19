'''
create melt script to assemble animation
'''

import os as os
import stat as stat
import sys as sys

offsets = [3, 5, 8, 13, 21, 34, 55, 89]
offsets = list(reversed(offsets))

def concat_png(dirname):
    """list files in folder

    :dirname: TODO
    :returns: TODO

    """
    filename = dirname + '/concat.txt'

    with open(filename, mode='w') as file:

        files = os.listdir(dirname)
        files = filter(lambda f: f.endswith('.png'), files)
        files = sorted(files)

        i = 0

        for f in files:
            duration = 2
            if i < len(offsets):
                out = offsets[i]

            file.write(f'file "{f}" \n')
            file.write(f'duration "{f}" \n')
            i+=1


def melt_png(dirname):
    """list files in folder

    :dirname: TODO
    :returns: TODO

    """
    filename = dirname + '/melt_build.sh'

    with open(filename, mode='w') as file:
        os.chmod(filename, stat.S_IRWXU)

        file.write('melt ')

        files = os.listdir(dirname)
        files = filter(lambda f: f.endswith('.png'), files)
        files = sorted(files)

        i = 0

        for f in files:
            out = 2
            if i < len(offsets):
                out = offsets[i]

            file.write(f'{f} out={out} ')
            i+=1

if __name__ == '__main__':
    dirname = '.'
    if len(sys.argv) > 1:
        dirname = sys.argv[1] 
    melt_png(dirname)
