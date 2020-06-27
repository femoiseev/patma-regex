from distutils.core import setup
setup(
  name = 'patma_regex',
  packages = ['patma_regex'],
  version = '0.1',
  license='MIT',
  description = 'A mini-library for destructive group matching of regexes in Python using recently proposed Structural Pattern Matching (https://www.python.org/dev/peps/pep-0622/).',
  author = 'Fedor Moiseev',
  author_email = 'femoiseev@gmail.com',
  url = 'https://github.com/femoiseev/patma-regex',
  download_url = 'https://github.com/femoiseev/patma-regex/archive/v_01.tar.gz',
  keywords = ['pattern matching', 'regex'],
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License', 
    'Programming Language :: Python :: 3'
  ],
)