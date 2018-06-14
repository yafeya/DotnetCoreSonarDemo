import csprojectAnalyzer
import os
import subprocess
import sys
import setpath


def __rebuild_project__(project, config='Debug'):
    if os.path.exists(project):
        subprocess.run(['dotnet', 'clean', project])
        subprocess.run(['dotnet', 'build', '-c', config, project])
    else:
        print('{arg1} does not exist...'.format(arg1=project))


def build_xunit_projects(solution_file, config):
    if os.path.exists(solution_file):
        analyzer = csprojectAnalyzer.CsProjectsAnalyzer(solution_file)
        xunit_projects = analyzer.get_xunit_projects()
        for xunit_project in xunit_projects:
            __rebuild_project__(xunit_project, config)
    else:
        print('Solution {arg1} does not exist...'.format(arg1=solution_file))


if __name__ == "__main__":
    setpath.set_path()

    _solution = ''
    _config = ''
    _platform = ''

    if len(sys.argv) > 1:
        _solution = sys.argv[1]
    if len(sys.argv) > 2:
        _config = sys.argv[2]

    if _config == '':
        _config = 'Debug'

    build_xunit_projects(_solution, _config)
