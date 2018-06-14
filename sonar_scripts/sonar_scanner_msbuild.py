import build_solution
import make_test
import generate_reports
import os
import setpath
import sys

__solution_name__ = ''
__solution_file__ = ''
__solution_dir__ = ''
__config__ = 'Debug'
__platform__ = 'x64'


def scan_sonar_project():
    msbuild = '"C:\\sonar-scanner-msbuild-netcoreapp2.0\\SonarScanner.MSBuild.dll"'
    key = '{arg1}_key'.format(arg1=__solution_name__)
    name = __solution_name__
    key_arg = '/k:"{arg1}" '.format(arg1=key)
    name_arg = '/n:"{arg1}" '.format(arg1=name)
    coverage_report_arg = '/d:sonar.cs.vscoveragexml.reportsPaths="..\\TestResults\\coverage_report.xml" '
    trx_report_arg = '/d:sonar.cs.vstest.reportsPaths="..\\TestResults\\*.trx"'

    sonar_begin_command = 'dotnet {build} begin {k} {n} /v:"1.0" {cr} {trx}' \
        .format(build=msbuild, k=key_arg, n=name_arg, cr=coverage_report_arg, trx=trx_report_arg)

    sonar_end_command = 'dotnet {build} end'.format(build=msbuild)

    os.system(sonar_begin_command)
    print('Building Projects')
    build_solution.build_solution(__solution_file__, __config__)
    print('Projects Built...')

    print('Executing XUnit Tests...')
    make_test.make_tests(__solution_file__, __config__, __platform__)
    print('XUnit Tests Executed...')

    print('Generating Test Reports...')
    generate_reports.generate_reports(__solution_dir__)
    print('Test Reports Generated...')

    os.system(sonar_end_command)


if __name__ == "__main__":
    setpath.set_path()

    if len(sys.argv) > 1:
        __solution_file__ = sys.argv[1]
    if len(sys.argv) > 2:
        __config__ = sys.argv[2]
    if len(sys.argv) > 3:
        __platform__ = sys.argv[3]

    if __config__ == '':
        __config__ = 'Debug'
    if __platform__ == '':
        __platform__ = 'x64'

    if os.path.exists(__solution_file__):
        __solution_dir__ = os.path.dirname(__solution_file__)
        __solution_name__ = os.path.splitext(__solution_file__)[0]
        __solution_name__ = __solution_name__.replace(__solution_dir__, '')
        if '\\' in __solution_name__:
            __solution_name__ = __solution_name__.replace('\\', '')

    scan_sonar_project()
