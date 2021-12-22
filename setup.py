import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='xremap',  
    version='0.1.0',
    scripts=['xremap-python'] ,
    author='Takashi Kokubun',
    author_email='takashikkbn@gmail.com',
    description='Generate xremap config from Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/xremap/xremap-python',
    packages=['xremap'],
    install_requires=['pyyaml'],
)
