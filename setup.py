from setuptools import setup
# from setuptools.command.install import install
# import json
# import shutil
# import subprocess
# import pathlib

# ROOT = pathlib.Path(__file__).resolve().parent

# class PostInstallCommand(install):
#     def run(self):
#         output = subprocess.check_output(['jupyter', '--paths', '--json'])
#         output_str = output.decode('utf-8')
#         # parse output_str as JSON
#         paths = json.loads(output_str)
#         config_dir = paths['config'][0]
#         shutil.copy(ROOT / 'lean-lsp.json', config_dir)

#         install.run(self)

# setup(
#     cmdclass={
#         'install': PostInstallCommand,
#     }
# )

setup()
