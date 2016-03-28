# -*- coding: utf-8 -*-
#
# Copyright (C) 2016 Hewlett Packard Enterprise Development LP
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

"""
topology_lib_scapy communication library implementation.
"""

from __future__ import unicode_literals, absolute_import
from __future__ import print_function, division
from __future__ import with_statement
import requests


class CLI:

    def __init__(self, enode):
        self.enode = enode

    def __enter__(self):
        self.enode.get_shell('bash').send_command('scapy', matches='>>> ')
        return self

    def __exit__(self, type, value, traceback):
        self.enode.get_shell('bash').send_command('exit()')
    
    def load_settings(self, file_name):
        settings = requests.get(file_name).text
        command = 'exec({!r},globals())'.format(settings)
        response = self.send_command(command)
        assert not response

    def send_command(self, command):
        self.enode.get_shell('bash').send_command(command, matches='>>> ')
        response = self.enode.get_shell('bash').get_response()
        return response

__all__ = [
    'CLI'
]
