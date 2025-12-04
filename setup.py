

from setuptools import setup, find_packages


setup(name="tap-workday-adaptive-planning",
      version="0.0.1",
      description="Singer.io tap for extracting data from Workday Adaptive Planning API",
      author="Stitch",
      url="http://singer.io",
      classifiers=["Programming Language :: Python :: 3 :: Only"],
      py_modules=["tap_workday_adaptive_planning"],
      install_requires=[
        "singer-python==6.3.0",
        "requests==2.32.4",
        "backoff==2.2.1",
        "parameterized"
      ],
      entry_points="""
          [console_scripts]
          tap-workday-adaptive-planning=tap_workday_adaptive_planning:main
      """,
      packages=find_packages(),
      package_data = {
          "tap_workday_adaptive_planning": ["schemas/*.json"],
      },
      include_package_data=True,
)
