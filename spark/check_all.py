import os
import glob
import time
import sys
import traceback
import shutil

import nbconvert
import nbformat

# https://nbconvert.readthedocs.io/en/latest/execute_api.html
# https://gist.github.com/minrk/2620876#gistcomment-1240959

ep = nbconvert.preprocessors.ExecutePreprocessor(
    extra_arguments=["--log-level=ERROR"],
    timeout=120
)


def run_notebook(path):
    path = os.path.abspath(path)
    assert path.endswith('.ipynb')
    nb = nbformat.read(path, as_version=4)
    try:
        ep.preprocess(nb, {'metadata': {'path': os.path.dirname(path)}})
    except Exception as e:
        print("\nException raised while running '{}'\n".format(path))
        traceback.print_exc(file=sys.stdout)
        sys.exit(1)


if __name__ == '__main__':
    run = 0
    sys.stdout.write('==========================='
                     ' Starting tests '
                     '===========================\n\n')
    try:
        shutil.rmtree(os.path.join(os.path.dirname(__file__), "metastore_db"))
    except:
        pass
    for path in glob.iglob('*.ipynb'):
        s = time.time()
        sys.stdout.write('Now running ' + path + '\n')
        sys.stdout.flush()
        run_notebook(path)
        sys.stdout.write('\n\033[92m' +
                         '===========================' +
                         ' Ok - {}s '.format(int(time.time() - s)) +
                         '===========================\n' +
                         '\033[0m')
        run += 1
    sys.stdout.write('\n\033[92m' +
                     '===========================' +
                     ' {} notebooks tested '.format(run) +
                     '===========================\n' +
                     '\033[0m')
