#!/usr/bin/env python
# *_* coding: utf-8 *_*

"""brainfuck kernel class module"""

import os
import shutil
import pexpect
from ipykernel.kernelbase import Kernel

class jansbrainfuckkernel(Kernel):
    """brainfuck kernel creates, com"""
    implementation = 'IPython'
    implementation_version = '8.11.0'
    language = 'brainfuck'
    language_version = '0.1'
    language_info = {
        'name': 'brainfuck',
        'mimetype': 'application/brainfuck',
        'file_extension': '.bf',
    }
    banner = "Brainfuck kernel"

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        if not silent:
            workingdir = "/tmp/jansbrainfuckkernel/"
            if os.path.exists(workingdir):
                shutil.rmtree(workingdir)
            os.mkdir(workingdir)
            os.chdir(workingdir)
            with open(workingdir + "proj.bf", "w", encoding="UTF-8") as file:
                file.write(code)
            os.system('bfc ' + workingdir  + 'proj.bf')
            if os.path.exists(workingdir + 'a.out'):
                solution = pexpect.run(workingdir + 'a.out').decode('UTF-8')
            else:
                solution = "Fuck your brain code did not compile."
            stream_content = {'name': 'stdout', 'text': solution}
            self.send_response(self.iopub_socket, 'stream', stream_content)

        return {'status': 'ok',
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
               }

    def do_shutdown(self, restart):
        workingdir = "/tmp/jansbrainfuckkernel/"
        shutil.rmtree(workingdir)
