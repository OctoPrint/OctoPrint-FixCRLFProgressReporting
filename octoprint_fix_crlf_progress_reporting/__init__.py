# coding=utf-8
from __future__ import absolute_import, division, unicode_literals

import logging

import octoprint.plugin

BROKEN_VERSION = "1.4.0"
FIXED_VERSION = "1.4.1"

class FixCRLFProgressReportingPlugin(octoprint.plugin.OctoPrintPlugin,
                                     octoprint.plugin.RestartNeedingPlugin):

	def initialize(self):
		import octoprint.util.comm
		from octoprint.util import bom_aware_open

		def fixed_start(self):
			"""
			Opens the file for reading and determines the file size.
			"""
			octoprint.util.comm.PrintingFileInformation.start(self)
			with self._handle_mutex:
				self._handle = bom_aware_open(self._filename, encoding="utf-8", errors="replace", newline="")
				self._pos = self._handle.tell()
				if self._handle.encoding.endswith("-sig"):
					import codecs
					self._pos += len(codecs.BOM_UTF8)
				self._read_lines = 0

		octoprint.util.comm.PrintingGcodeFileInformation.start = fixed_start
		self._logger.info("octoprint.util.comm.PrintingGcodeFileInformation.start replaced with CRLF compatible version")

	##~~ Softwareupdate hook

	def get_update_information(self):
		return dict(
			fix_crlf_progress_reporting=dict(
				displayName="Fix CRLF Progress Reporting",
				displayVersion=self._plugin_version,

				# version check: github repository
				type="github_release",
				user="OctoPrint",
				repo="OctoPrint-FixCRLFProgressReporting",
				current=self._plugin_version,

				# update method: pip
				pip="https://github.com/OctoPrint/OctoPrint-FixCRLFProgressReporting/archive/{target_version}.zip"
			)
		)


__plugin_name__ = "Fix CRLF Progress Reporting"
__plugin_pythoncompat__ = ">=2.7,<4" # python 2 and 3


def __plugin_check__():
	from octoprint.util.version import is_octoprint_compatible
	compatible = is_octoprint_compatible(">={},<{}".format(BROKEN_VERSION, FIXED_VERSION))
	if not compatible:
		logging.getLogger(__name__).info("Plugin is not needed in OctoPrint versions < 1.4.0 or >= 1.4.1")
	return compatible


def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = FixCRLFProgressReportingPlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
	}

