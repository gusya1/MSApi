import setuptools

setuptools.setup(name='MSApi',
                 version='0.0.6',
                 description='Python API for manage MoySklad',
                 packages=setuptools.find_packages(),
                 install_requires=["requests>=2.22.0"],
                 author_email='serheos@gmail.com',
                 zip_safe=False)
