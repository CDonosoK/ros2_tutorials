from setuptools import find_packages, setup

package_name = 'ros2_tutorial_python_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='cdonoso',
    maintainer_email='cdonoso@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            #nombre_nodo_a_llamar = nombre_paquete.nombre_archivo:funcion_a_llamar
            'tutorial_00_py_node = ros2_tutorial_python_pkg.my_first_node:main'
        ],
    },
)
