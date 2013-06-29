# ======================================================== #
# File automagically generated by GUI2Exe version 0.5.3
# Copyright: (c) 2007-2012 Andrea Gavana
# ======================================================== #

# Let's start with some default (for me) imports...

from distutils.core import setup
import glob
import os
import zlib
import shutil

from py2exe.build_exe import py2exe


# Remove the build folder
shutil.rmtree("build", ignore_errors=True)


class Target(object):
	""" A simple class that holds information on our executable file. """

	def __init__(self, **kw):
		""" Default class constructor. Update as you need. """
		self.__dict__.update(kw)
		self.company_name = "Maxisoft"

# Ok, let's explain why I am doing that.
# Often, data_files, excludes and dll_excludes (but also resources)
# can be very long list of things, and this will clutter too much
# the setup call at the end of this file. So, I put all the big lists
# here and I wrap them using the textwrap module.

data_files = [('', ['config.ini', 'MaxiVote.ico'])]

includes = ['importall', 'Crypto', 'requests', 'certifi', "lxml", "email", "mercurial", "cv2", "numpy", "sip",
            "win32gui_struct", "_winreg"]
excludes = ['_gtkagg', '_tkagg', 'bsddb', 'curses', 'email', 'pywin.debugger',
            'pywin.debugger.dbgcon', 'pywin.dialogs', 'tcl',
            'Tkconstants', 'Tkinter', 'importhook']
packages = ['utils', 'Crypto', 'requests', 'certifi', "lxml", "mercurial", "storm"]
dll_excludes = ['tcl84.dll', 'python32.dll']
icon_resources = [(1, 'MaxiVote.ico')]
bitmap_resources = []
other_resources = []


# This is a place where the user custom code may go. You can do almost
# whatever you want, even modify the data_files, includes and friends
# here as long as they have the same variable name that the setup call
# below is expecting.

# No custom code added


# Ok, now we are going to build our target class.
# I chose this building strategy as it works perfectly for me :-D

GUI2Exe_Target_1 = Target(
	# what to build
	script="main.py",
	icon_resources=icon_resources,
	bitmap_resources=bitmap_resources,
	other_resources=other_resources,
	dest_base="MaxiVote",
	version="2",
	name="MaxiVote - Bot Vote",

)


################################################################
# a NT service, modules is required
SERVICE = Target(
	# used for the versioninfo resource
	description="MaxiVote Service - Bot Vote",
	# what to build.  For a service, the module name (not the
	# filename) must be specified!
	modules=["MaxiVoteService"],
	cmdline_style='pywin32',
	icon_resources=[(1, 'Service.ico')]
)

# No custom class for UPX compression or Inno Setup script

# That's serious now: we have all (or almost all) the options py2exe
# supports. I put them all even if some of them are usually defaulted
# and not used. Some of them I didn't even know about.

setup(

	# No UPX or Inno Setup

	data_files=data_files,

	options={"py2exe": {"compressed": 2,
	                    "optimize": 1,
	                    "includes": includes,
	                    "excludes": excludes,
	                    "packages": packages,
	                    "dll_excludes": dll_excludes,
	                    "bundle_files": 1,
	                    "dist_dir": "dist",
	                    "xref": False,
	                    "skip_archive": False,
	                    "ascii": False,
	                    "custom_boot_script": '',
	}
	},

	#zipfile = None,
	console=[],
	windows=[GUI2Exe_Target_1],
	service=[SERVICE],
	com_server=[],
	ctypes_com_server=[]
)

# This is a place where any post-compile code may go.
# You can add as much code as you want, which can be used, for example,
# to clean up your folders or to do some particular post-compilation
# actions.

# No post-compilation code added


# And we are done. That's a setup script :-D

