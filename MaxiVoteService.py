import win32serviceutil
import win32service
import win32event
import win32evtlogutil
from subprocess import Popen
import os
import sys

class MaxiVoteService(win32serviceutil.ServiceFramework):
	_svc_name_ = "MaxiVote"
	_svc_display_name_ = "MaxiVote"
	_svc_deps_ = []

	def __init__(self, args):
		win32serviceutil.ServiceFramework.__init__(self, args)
		self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
		self.popen = None

	def SvcStop(self):
		if self.popen:
			try:
				if self.popen.returncode is None:
					self.popen.kill()
			except:
				pass
		self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
		win32event.SetEvent(self.hWaitStop)

	def SvcDoRun(self):
		import servicemanager
		if not self.popen:
			self.popen = Popen("MaxiVote.exe", cwd=os.path.dirname(sys.argv[0]))

		# wait for beeing stopped...
		win32event.WaitForSingleObject(self.hWaitStop, win32event.INFINITE)


if __name__ == '__main__':
	# Note that this code will not be run in the 'frozen' exe-file!!!
	win32serviceutil.HandleCommandLine(MaxiVoteService)
