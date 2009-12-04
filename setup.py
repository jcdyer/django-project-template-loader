#from distribute_setup import use_setuptools
#use_setuptools()

from setuptools import setup

setup(name='django-project-template-loader',
      version='0.1',
      description='An app to provide a template loader which pulls templates from [project_dir]/templates',
      author='J. Cliff Dyer',
      author_email='jcd@sdf.lonestar.org',
      url='http://bitbucket.org/cliff/django-project-template-loader',
      packages=['project_template_loader', 'project_template_loader.loaders',],
      package_data={},
      install_requires=[
          'distribute',
          'Django',
      ],
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
      )
