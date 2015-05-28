import itertools
import subprocess
import sys

#http://pastebin.com/zj72xk4N

#run when system password box is showing eg. keychain password dialog

#apple script for automating dialog box input
sys_script = '''
tell application "System Events" to tell process "SecurityAgent"
	set value of text field 1 of window 1 to $(PASS)
	click button 1 of group 1 of window 1
end tell
'''

#fill this array with chars for combination
keys = ['s','t','a','r','t']

def automate_login():
	for l in xrange(0, len(keys)+1):
		for subset in itertools.permutations(keys, l):
			guess = ''.join(subset)
			tmp = sys_script.replace('$(PASS)', '"%s"' % guess)
			try:
				subprocess.check_output('osascript -e \'%s\'' % tmp, shell=True)
				sys.stdout.write('\rtrying %s  ' % guess)
				sys.stdout.flush()
			except subprocess.CalledProcessError:
				print('\nfailed')
				return
	return

automate_login()