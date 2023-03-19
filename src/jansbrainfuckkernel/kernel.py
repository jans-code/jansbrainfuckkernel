##!/usr/bin/env python
from ipykernel.kernelbase import Kernel
import pexpect, os, shutil

class jansbrainfuckkernel(Kernel):
    implementation = 'IPython'
    implementation_version = '8.10.0'
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
            os.mkdir(workingdir)
            os.chdir(workingdir)
            with open(workingdir + "proj.bf", "w") as f:
                    f.write(code)
            os.system('bfc ' + workingdir  + 'proj.bf')
            solution = pexpect.run(workingdir + 'a.out').decode('ascii')
            shutil.rmtree(workingdir)
            stream_content = {'name': 'stdout', 'text': solution}
            self.send_response(self.iopub_socket, 'stream', stream_content)

        return {'status': 'ok',
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
               }
