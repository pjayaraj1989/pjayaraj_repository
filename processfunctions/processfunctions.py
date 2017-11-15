import subprocess
import sys

#execute
def execute(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    # Poll process for new output until finished
    while True:
        nextline = process.stdout.readline()
        if nextline == '' and process.poll() is not None:
            break
        sys.stdout.write(nextline)
        sys.stdout.flush()
	output,err = process.communicate()
	exitCode = process.returncode
	print 'Exit code:-' + str(exitCode)
	
	if (exitCode == 0):
		return output
	else:
		raise ProcessException(command, exitCode, output)
	
	return output,err