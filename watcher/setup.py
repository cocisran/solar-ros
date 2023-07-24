from setuptools import setup

package_name = 'watcher'

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
    maintainer_email='robotica23@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'watcher_pub = watcher.watcher_pub:main',
            'watcher_sub = watcher.watcher_sub:main',
            'server_img_delivery =  watcher.deliver_server:main',
            'cliente_img_delivery =  watcher.deliver_client:main'
        ],
    },
)
