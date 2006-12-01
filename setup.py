#!/usr/bin/env python

from distutils.core import setup
from glob import glob

setup(name="Bcfg2.Server",
      version="0.8.7pre1",
      description="Bcfg2 Server",
      author="Narayan Desai",
      author_email="desai@mcs.anl.gov",
      packages=["Bcfg2", 'Bcfg2.Server', "Bcfg2.Server.Plugins", "Bcfg2.Server.Hostbase",
                "Bcfg2.Server.Hostbase.hostbase", "Bcfg2.Server.Reports",
                "Bcfg2.Server.Reports.reports", "Bcfg2.Client", "Bcfg2.Client.Tools"],
      package_dir = {'Bcfg2':'src/lib'}, 
      scripts = glob('src/sbin/*'),
      data_files = [('share/bcfg2/schemas',
                     glob('schemas/*.xsd')),
                    ('share/bcfg2/xsl-transforms',
                     glob('reports/xsl-transforms/*.xsl')),
                    ('share/bcfg2/xsl-transforms/xsl-transform-includes',
                     glob('reports/xsl-transforms/xsl-transform-includes/*.xsl')),
                    ('share/man/man1', ['man/bcfg2.1']),
                    ('share/man/man5', glob("man/*.5")),
                    ('share/man/man8', glob("man/*.8"))]
      )
