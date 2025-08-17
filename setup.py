from setuptools import find_packages, setup

package_name = 'rostest'

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
    maintainer='atharv',
    maintainer_email='m.atharv07@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "listener = rostest.listenerNode:main",
            "talker = rostest.talkerNode:main",
            "hi = rostest.hi:main",
            "bye = rostest.bye:main"
        ],
    },
)
