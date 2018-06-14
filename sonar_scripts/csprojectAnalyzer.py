import os
import xml.etree.ElementTree as xmltree


class CsProjectsAnalyzer:
    _solution_file = ''
    _solution_folder = ''
    _project_sep = ', '

    def __init__(self, solution_file):
        if os.path.exists(solution_file):
            self._solution_file = solution_file
            self._solution_folder = os.path.dirname(solution_file)

    def get_xunit_projects(self):
        result = []
        projects = self.__get_projects__()
        for project in projects:
            project = os.path.join(self._solution_folder, project)
            if os.path.exists(project):
                project_tree = xmltree.parse(project)
                reference_nodes = project_tree.findall('.//PackageReference')
                for reference_node in reference_nodes:
                    package = reference_node.get('Include')
                    if 'xunit' in package:
                        result.append(project)
                        break

        return result

    def get_target_framework(self, project):
        target = 'netcoreapp2.0'
        if os.path.exists(project):
            project_tree = xmltree.parse(project)
            target_nodes = project_tree.findall('.//TargetFramework')
            if len(target_nodes) > 0:
                target_node = target_nodes.pop(0)
                target = target_node.text
        return target

    def get_output_assembly_name(self, project):
        output = ''
        if os.path.exists(project):
            project_tree = xmltree.parse(project)
            assembly_nodes = project_tree.findall('.//AssemblyName')
            if len(assembly_nodes) > 0:
                assembly_node = assembly_nodes.pop(0)
                output = assembly_node.text
            else:
                dirname = os.path.dirname(project)
                output = os.path.splitext(project)[0]
                output = output.replace(dirname, '')
                if '\\' in output:
                    output = output.replace('\\', '')
                elif '/' in output:
                    output = output.replace('/', '')

        if not output == '':
            output += '.dll'

        return output

    def get_xunit_filename(self, project, config='Debug'):
        filename = ''
        if os.path.exists(project):
            dirname = os.path.dirname(project)
            assembly_name = self.get_output_assembly_name(project)
            framework = self.get_target_framework(project)
            filename = os.path.join(dirname, 'bin', config, framework, assembly_name)
        return filename

    def __get_projects__(self):
        projects = []
        if os.path.exists(self._solution_file):
            try:
                fp = open(self._solution_file)
                lines = fp.readlines()
                for line in lines:
                    proj = self.__get_proj_from_line__(line)
                    if not proj == '':
                        projects.append(proj)
            finally:
                fp.close()
        return projects

    def __get_proj_from_line__(self, line):
        result = ''
        if line.startswith('Project'):
            parts = line.split(self._project_sep)
            if len(parts) >= 3:
                proj = parts[1]
                proj = proj.replace('"', '')
                if proj.endswith('.csproj'):
                    result = proj
        return result