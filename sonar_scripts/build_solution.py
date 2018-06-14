import os
import sys
import setpath


def build_solution(solution_file, config):
    if os.path.exists(solution_file):
        os.system('dotnet clean {arg1}'.format(arg1=solution_file))
        os.system('dotnet build -c {arg1} {arg2}'.format(arg1=config, arg2=solution_file))
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

    build_solution(_solution, _config)
