releaseConfig = {}

# Release Notification
releaseConfig['AllRecipients']       = ['release@mozilla.com',]
releaseConfig['PassRecipients']      = ['release-drivers@mozilla.org',]
releaseConfig['AVVendorsRecipients'] = ['av-vendor-release-announce@mozilla.org',]
releaseConfig['releaseTemplates']    = 'release_templates'
releaseConfig['messagePrefix']       = '[release] '

# Basic product configuration
#  Names for the product/files
releaseConfig['productName']         = 'firefox'
releaseConfig['appName']             = 'browser'
releaseConfig['binaryName']          = releaseConfig['productName'].capitalize()
releaseConfig['oldBinaryName']       = releaseConfig['binaryName']
#  Current version info
releaseConfig['version']             = '4.0.1'
releaseConfig['appVersion']          = releaseConfig['version']
releaseConfig['milestone']           = '2.0.1'
releaseConfig['buildNumber']         = 1
releaseConfig['baseTag']             = 'FIREFOX_4_0_1'
#  Old version info
releaseConfig['oldVersion']          = '4.0rc2'
releaseConfig['oldAppVersion']       = '4.0'
releaseConfig['oldBuildNumber']      = 3
releaseConfig['oldBaseTag']          = 'FIREFOX_4_0rc2'
#  Next (nightly) version info
releaseConfig['nextAppVersion']      = '4.0.2pre'
releaseConfig['nextMilestone']       = '2.0.2pre'
#  Repository configuration, for tagging
releaseConfig['sourceRepositories']  = {
    'mozilla': {
        'name': 'mozilla-2.0',
        'path': 'releases/mozilla-2.0',
        'revision': 'fdfd2af3498e',
        'relbranch': None,
        'bumpFiles': {
            'browser/config/version.txt': {
                'version': releaseConfig['appVersion'],
                'nextVersion': releaseConfig['nextAppVersion']
            },
            'config/milestone.txt': {
                'version': releaseConfig['milestone'],
                'nextVersion': releaseConfig['nextMilestone']
            },
            'js/src/config/milestone.txt': {
                'version': releaseConfig['milestone'],
                'nextVersion': releaseConfig['nextMilestone']
            },
        }
    }
}
#  L10n repositories
releaseConfig['l10nRelbranch']       = None
releaseConfig['l10nRepoPath']        = 'releases/l10n-mozilla-2.0'
releaseConfig['l10nRevisionFile']    = 'l10n-changesets_mozilla-2.0'
#  Support repositories
releaseConfig['otherReposToTag']     = {
    'build/compare-locales': 'RELEASE_AUTOMATION',
    'build/buildbot': 'production-0.8',
    'build/partner-repacks': 'default'
}

# Platform configuration
releaseConfig['enUSPlatforms']       = ('linux', 'linux64', 'win32', 'macosx64')
releaseConfig['talosTestPlatforms']  = releaseConfig['enUSPlatforms']
releaseConfig['unittestPlatforms']   = ()
releaseConfig['xulrunnerPlatforms']  = releaseConfig['enUSPlatforms']

# L10n configuration
releaseConfig['l10nPlatforms']       = releaseConfig['enUSPlatforms']
releaseConfig['shippedLocalesPath']  = 'browser/locales/shipped-locales'
releaseConfig['l10nChunks']          = 6
releaseConfig['mergeLocales']        = True

# Mercurial account
releaseConfig['hgUsername']          = 'ffxbld'
releaseConfig['hgSshKey']            = '~cltbld/.ssh/ffxbld_dsa'

# Update-specific configuration
releaseConfig['cvsroot']             = ':ext:cltbld@cvs.mozilla.org:/cvsroot'
releaseConfig['patcherConfig']       = 'moz20-branch-patcher2.cfg'
releaseConfig['commitPatcherConfig'] = True
releaseConfig['patcherToolsTag']     = 'UPDATE_PACKAGING_R13'
releaseConfig['ftpServer']           = 'ftp.mozilla.org'
releaseConfig['stagingServer']       = 'stage-old.mozilla.org'
releaseConfig['bouncerServer']       = 'download.mozilla.org'
releaseConfig['ausServerUrl']        = 'https://aus2.mozilla.org'
releaseConfig['ausUser']             = 'cltbld'
releaseConfig['ausSshKey']           = 'cltbld_dsa'
releaseConfig['releaseNotesUrl']     = None
releaseConfig['testOlderPartials']   = False
releaseConfig['useBetaChannel']      = 1
releaseConfig['verifyConfigs']       = {
    'linux':  'moz20-firefox-linux.cfg',
    'linux64':  'moz20-firefox-linux64.cfg',
    'macosx64': 'moz20-firefox-mac64.cfg',
    'win32':  'moz20-firefox-win32.cfg'
}

# Partner repack configuration
releaseConfig['doPartnerRepacks']    = True
releaseConfig['partnersRepoPath']    = 'build/partner-repacks'

# Major update configuration
releaseConfig['majorUpdateRepoPath'] = 'releases/mozilla-2.0'
releaseConfig['majorUpdateToVersion']   = '5.0b2'
releaseConfig['majorUpdateAppVersion']  = '5.0'
releaseConfig['majorUpdateBuildNumber'] = 1
releaseConfig['majorUpdateBaseTag']     = 'FIREFOX_5_0b2'
releaseConfig['majorUpdateReleaseNotesUrl']  = 'https://www.mozilla.com/%locale%/firefox/5.0/details/'
releaseConfig['majorUpdatePatcherConfig']    = 'moz20-branch-major-update-patcher2.cfg'
releaseConfig['majorPatcherToolsTag']        = 'UPDATE_PACKAGING_R11_1_MU'
releaseConfig['majorUpdateVerifyConfigs']    = {
    'linux':  'moz20-firefox-linux-major.cfg',
    'linux64':  'moz20-firefox-linux64-major.cfg',
    'macosx64': 'moz20-firefox-mac64-major.cfg',
    'win32':  'moz20-firefox-win32-major.cfg'
}
releaseConfig['majorFakeMacInfoTxt'] = True
# Tuxedo/Bouncer configuration
releaseConfig['tuxedoConfig']        = 'firefox-tuxedo.ini'
releaseConfig['tuxedoServerUrl']     = 'https://bounceradmin.mozilla.com/api/'
releaseConfig['extraBouncerPlatforms'] = ('solaris-sparc', 'solaris-i386',
                                          'opensolaris-sparc',
                                          'opensolaris-i386')

# Misc configuration
releaseConfig['enable_repo_setup'] = False
