from distutils.core import setup
setup(
  name = 'DjangoTemplateConverter',         # How you named your package folder (MyLib)
  packages = ['DjangoTemplateConverter'],   # Chose the same as "name"
<<<<<<< HEAD
  version = '2.4',      # Start with a small number and increase it with every change you make
=======
  version = '1.5',      # Start with a small number and increase it with every change you make
>>>>>>> 2aa0f00495d06845ff8528a135da2ebf9b742f21
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'TYPE YOUR DESCRIPTION HERE',   # Give a short description about your library
  author = 'YOUR NAME',                   # Type in your name
  author_email = 'iamaksingh11@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/iamaksingh11/DjangoTemplateConverter',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/iamaksingh11/DjangoTemplateConverter/archive/refs/tags/v_1.tar.gz',    # I explain this later on
  keywords = ['SOME', 'MEANINGFULL', 'KEYWORDS'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          # 'validators',
          # 'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
  # scripts=['bin/DjangoTemplateConverter-joke'],
  entry_points={
   'console_scripts': [
        'DjangoTemplateConverter = DjangoTemplateConverter.start:main',
    ],
  }
)