#!/usr/bin/env python

from Generator import Generator
from GeneratorUtils import DirectoryBacked
from Types import Service

class servicemgr(Generator):
    '''This is a generator that handles service assignments'''
    __name__ = 'servicemgr'
    __version__ = '$Id$'
    __author__ = 'bcfg-dev@mcs.anl.gov'

    __provides__ = {'Service':{'sshd':'GetService'}}

    def GetService(self,name,metadata):
        # for now sshd is on
        if name == 'sshd':
            return Service('sshd','chkconfig','on','global')
        else:
            return Service(name,'chkconfig','off','local')

