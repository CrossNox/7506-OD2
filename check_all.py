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

class NotebookExecutionError(Exception):
    pass

def run_notebook(path):
    path = os.path.abspath(path)
    assert path.endswith('.ipynb')
    nb = nbformat.read(path, as_version=4)
    try:
        ep.preprocess(nb, {'metadata': {'path': os.path.dirname(path)}})
    except Exception as e:
        print("\nException raised while running '{}'\n".format(path))
        traceback.print_exc(file=sys.stdout)
        raise NotebookExecutionError


if __name__ == '__main__':
    run, errors, ok = 0, 0, 0
    sys.stdout.write('==========================='
                     ' Starting tests '
                     '===========================\n\n')
    try:
        shutil.rmtree(os.path.join(os.path.dirname(__file__), "metastore_db"))
    except:
        pass
    for path in glob.iglob(os.path.join(os.path.dirname(__file__), '**/*.ipynb'), recursive=True):
        s = time.time()
        sys.stdout.write('\n\033[34m' +
                         '===========================' +
                         'Now running ' + path +
                         '===========================\n' +
                         '\033[0m')
        sys.stdout.flush()
        try:
            run_notebook(path)
            sys.stdout.write('\n\033[92m' +
                             '===========================' +
                             ' Ok - {}s '.format(int(time.time() - s)) +
                             '===========================\n' +
                             '\033[0m')
            ok += 1
        except:
            sys.stdout.write('\n\033[91m' +
                             '===========================' +
                             ' Error - {}s '.format(int(time.time() - s)) +
                             '===========================\n' +
                             '\033[0m')
            errors += 1
        finally:
            run += 1
    sys.stdout.write('\n\033[93m' +
                     '===========================' +
                     ' {} notebooks tested - {} ok, {} errors'.format(run, ok, errors) +
                     '===========================\n' +
                     '\033[0m')
