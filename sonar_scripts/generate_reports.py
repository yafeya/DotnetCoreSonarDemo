import setpath
import os
import glob
import sys
import shutil
import subprocess

__test_results_path__ = 'TestResults'


def __handle_trx_file__(solution_dir):
    trx_pattern = __test_results_path__ + '/*.trx'
    trx_founded = glob.glob(trx_pattern, recursive=True)
    trx_report = trx_founded.pop(0) if len(trx_founded) else ''
    if os.path.exists(trx_report):
        target_trx = os.path.join(solution_dir, __test_results_path__, 'target.trx')
        shutil.copyfile(trx_report, target_trx)


def __handle_coverage_report__(solution_dir):
    coverage_pattern = __test_results_path__ + '/**/*.coverage'
    coverage_founded = glob.glob(coverage_pattern, recursive=True)
    coverage_report = coverage_founded.pop(0) if len(coverage_founded) else ''
    if os.path.exists(coverage_report):
        target_report = os.path.join(solution_dir, __test_results_path__, 'coverage_report.xml')
        analyze_arg = 'analyze'
        output_arg = '/output:' + target_report
        subprocess.run(['CodeCoverage.exe', analyze_arg, output_arg, coverage_report])


def generate_reports(solution_dir):
    output_dir = os.path.join(solution_dir, __test_results_path__)

    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)

    if os.path.exists(__test_results_path__):
        os.mkdir(output_dir)
        print('Generating code coverage report...')
        __handle_coverage_report__(solution_dir)
        print('Generated code coverage report...')

        print('Copying the trx report...')
        __handle_trx_file__(solution_dir)
        print('Copied the trx report...')

    else:
        print('{arg1} does not exist, make sure the xunit has been executed...'.format(arg1=__test_results_path__))


if __name__ == "__main__":
    setpath.set_path()

    if len(sys.argv) > 1:
        _solution_dir = sys.argv[1]

    generate_reports(_solution_dir)
