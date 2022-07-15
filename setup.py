from setuptools import setup
 
setup(
    name='tisseglibrary',
    packages=['tisseglibrary'], # Mismo nombre que en la estructura de carpetas de arriba
    version='0.1.1',
    license='Apache License 2.0', # La licencia que tenga tu paquete
    description='It gets the 2D/3D segmentation of the abdomen and the thigh from MR images',
    author='Marina Sandonis',
    author_email='marinasandfer@gmail.com',
    url='https://github.com/MarinaSandonis/TisSegLibrary', # Usa la URL del repositorio de GitHub
    download_url='https://github.com/MarinaSandonis/TisSegLibrary.git', # Te lo explico a continuación
    keywords=['Tissue Segmentation'], # Palabras que definan tu paquete
    classifiers=['Programming Language :: Python',  # Clasificadores de compatibilidad con versiones de Python para tu paquete
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3.3',
                 'Programming Language :: Python :: 3.4',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7'],
)
