import os
import setpath
import sys
import csprojectAnalyzer
import shutil

__cmd_sep__ = ' '
__test_results_dir__ = 'TestResults'


def __perform_xunit_tests__(test_files, platform):
    cmd = ''
    cmd += 'vstest.console.exe' + __cmd_sep__
    for test_file in test_files:
        if os.path.exists(test_file):
            cmd += test_file + __cmd_sep__
        else:
            print('Test file: {arg1} does not exist...'.format(arg1=test_file))
    cmd += '/Logger:trx' + __cmd_sep__
    cmd += '/EnableCodeCoverage' + __cmd_sep__
    cmd += '/Platform:{arg1}'.format(arg1=platform)
    os.system(cmd)


def make_tests(solution, config, platform):
    if os.path.exists(__test_results_dir__):
        shutil.rmtree(__test_results_dir__)

    if os.path.exists(solution):
        analyzer = csprojectAnalyzer.CsProjectsAnalyzer(solution)
        xunit_projects = analyzer.get_xunit_projects()
        test_files = list()
        for xunit_project in xunit_projects:
            test_file = analyzer.get_xunit_filename(xunit_project, config)
            if os.path.exists(test_file):
                test_files.append(test_file)

        __perform_xunit_tests__(test_files, platform)
    else:
        print('Solution {arg1} does not exist...'.format(arg1=solution))


if __name__ == "__main__":
    setpath.set_path()

    print(os.environ['PATH'])

    _solution = ''
    _config = ''
    _platform = ''

    if len(sys.argv) > 1:
        _solution = sys.argv[1]
    if len(sys.argv) > 2:
        _config = sys.argv[2]
    if len(sys.argv) > 3:
        _platform = sys.argv[3]

    if _config == '':
        _config = 'Debug'
    if _platform == '':
        _platform = 'x64'

    make_tests(_solution, _config, _platform)
