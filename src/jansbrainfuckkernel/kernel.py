##!/usr/bin/env python
from ipykernel.kernelbase import Kernel
import pexpect, os, shutil

class jansbrainfuckkernel(Kernel):
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
            with open(workingdir + "proj.bf", "w") as f:
                    f.write(code)
            os.system('bfc ' + workingdir  + 'proj.bf')
            if os.path.exists(workingdir + 'a.out'):
                solution = pexpect.run(workingdir + 'a.out').decode('utf-8')
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
