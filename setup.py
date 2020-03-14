from setuptools import setup

setup(name="epiphany-editor",
      version="0.4.2",
      description="Map Editor for Epiphany (a Boulder-Dash clone).",
      author="Eric Mangold",
      author_email="teratorn /AT/ zoho /DOT/ com",
      scripts=['epiphany-editor'],
      install_requires=['pygame', 'PyGObject']
      )
