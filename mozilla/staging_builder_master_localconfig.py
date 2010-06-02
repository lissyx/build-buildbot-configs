c = BuildmasterConfig = {}
c['slavePortnum'] = 9010

from buildbot.status.html import WebStatus
c['status'] = [
        WebStatus(http_port=8010, allowForce=True)
]

c['buildbotURL'] = 'http://staging-master.build.mozilla.org:8010/'

from buildbot import manhole
c['manhole'] = manhole.PasswordManhole(1235, "cltbld", "password")

from config import BRANCHES
ACTIVE_BRANCHES = ['mozilla-central', 'addonsmgr', 'places', 'electrolysis']

# Set up our fast slaves
# No need to reload, this is reloaded by builder_master.cfg
import buildbotcustom.misc
buildbotcustom.misc.fastRegexes.extend([
    '-ix-',
    'xserve',
    ])
