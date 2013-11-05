# -*- coding: UTF-8 -*-

# Build customizations
# Change this file instead of sconstruct or manifest files, whenever possible.

# Full getext (please don't change)
_ = lambda x : x

# Add-on information variables
addon_info = {
	# for previously unpublished addons, please follow the community guidelines at:
	# https://bitbucket.org/nvdaaddonteam/todo/src/56140dbec531e4d7591338e1dbc6192f3dd422a8/guideLines.txt
	# add-on Name, internal for nvda
	"addon-name" : "bitChe",
	# Add-on summary, usually the user visible name of the addon.
	# TRANSLATORS: user visible addon name to be shown on installation and add-on information.
	"addon-summary" : _("Bit Che"),
	# Add-on description
	# Translators: Long description to be shown for this add-on on add-on information from add-ons manager
	"addon-description" : _("Improves the accessibility of Bit Che, a torrent searching client with NVDA."),
	# version
	"addon-version" : "1.3-dev",
	# Author(s)
	"addon-author" : "Alberto Zanella <lapostadialberto@gmail.com>, Alberto Buffolino <a.buffolino@gmail.com>",
	# URL for the add-on documentation support
	"addon-url" : "http://addons.nvda-project.org"
}


import os.path

# Define the python files that are the sources of your add-on.
# You can use glob expressions here, they will be expanded.
pythonSources = [os.path.join("addon", "appModules", "*.py"), os.path.join("addon", "installTasks.py")]

# Files that contain strings for translation. Usually your python sources
i18nSources = pythonSources + ["buildVars.py", "docHandler.py"]

# Files that will be ignored when building the nvda-addon file
# Paths are relative to the addon directory, not to the root directory of your addon sources.
excludedFiles = []
