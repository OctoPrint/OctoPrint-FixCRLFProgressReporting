---
layout: plugin

id: fix_crlf_progress_reporting
title: Fix CRLF Progress Reporting
description: Fixes progress reporting on GCODE files with CRLF line endings
author: Gina Häußge
license: AGPLv3

date: 2020-03-23

homepage: https://github.com/OctoPrint/OctoPrint-FixCRLFProgressReporting
source: https://github.com/OctoPrint/OctoPrint-FixCRLFProgressReporting
archive: https://github.com/OctoPrint/OctoPrint-FixCRLFProgressReporting/archive/master.zip

tags:
- workaround
- fix
- progress

compatibility:
  python: ">=2.7,<4"

---

Fixes progress reporting on GCODE files with CRLF line endings. If your GCODE viewer appears to be way behind on 
what is currently being printed in *OctoPrint 1.4.0*, try this plugin.

The underlying issue in question will be fixed in OctoPrint 1.4.1, at which point this plugin will no longer be 
required. Consequently it will only run on OctoPrint 1.4.0.

See also [this topic on the community forums](https://community.octoprint.org/t/curious-issue-with-print-progress/16304/).
