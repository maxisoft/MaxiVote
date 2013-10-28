import platform

if platform.system() == 'Windows':

	from win32event import CreateMutex
	from win32api import CloseHandle, GetLastError
	from winerror import ERROR_ALREADY_EXISTS

	__all__ = ["singleinstance"]

	class singleinstance:
		""" Limits application to single instance """

		def __init__(self):
			self.mutexname = "maxivote_{D0E858DF-985E-4907-B7FB-8D732C3FC3B9}"
			self.mutex = CreateMutex(None, False, self.mutexname)
			self.lasterror = GetLastError()

		def aleradyrunning(self):
			return (self.lasterror == ERROR_ALREADY_EXISTS)

		def __del__(self):
			if self.mutex:
				CloseHandle(self.mutex)



else:  # assume unix
	import fcntl

	class singleinstance:
		""" Limits application to single instance """

		def __init__(self):
			self.mutexname = ".maxivote_{D0E858DF-985E-4907-B7FB-8D732C3FC3B9}"
			self.fp = open(self.mutexname, 'w')

		def aleradyrunning(self):
			try:
				fcntl.lockf(self.fp, fcntl.LOCK_EX | fcntl.LOCK_NB)
			except IOError:
				return True
			else:
				return False

		def __del__(self):
			if self.mutex:
				self.fp.close()
