from setuptools import setup

package_name = 'poly_dust'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='robotica23',
    maintainer_email='fcoemmdmm@ciencias.unam.mx',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'poly_dust_server = poly_dust.poly_dust_server:main',
            'poly_dust_client = poly_dust.poly_dust_client:main'
        ],
    },
)
