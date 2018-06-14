import os

__msbuild__ = 'C:\\Program Files (x86)\\Microsoft Visual Studio\\2017\\Enterprise\\MSBuild\\15.0\\Bin;'

__vs_test_console__ = 'C:\\Program Files (x86)\\Microsoft Visual Studio\\2017\\' \
                      'Enterprise\\Common7\\IDE\\CommonExtensions\\Microsoft\\TestWindow;'

__code_coverage__ = 'C:\\Program Files (x86)\\Microsoft Visual Studio\\2017\\' \
                    'Enterprise\\Team Tools\\Dynamic Code Coverage Tools'

_adding_paths = [__msbuild__, __vs_test_console__, __code_coverage__]


def set_path():

    path = os.environ['PATH']+';'

    for adding_path in _adding_paths:
        if adding_path not in path:
            path += adding_path

    os.environ['PATH'] = path


if __name__ == "__main__":
    set_path()