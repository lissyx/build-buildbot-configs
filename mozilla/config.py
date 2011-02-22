from copy import deepcopy

import project_branches
reload(project_branches)
from project_branches import PROJECT_BRANCHES

import localconfig
reload(localconfig)
from localconfig import MAC_SNOW_MINIS, MAC_MINIS, XSERVES, LINUX_VMS, \
                        LINUX_IXS, WIN32_VMS, WIN32_IXS, SLAVES, \
                        TRY_SLAVES

GLOBAL_VARS = {
    # It's a little unfortunate to have both of these but some things (HgPoller)
    # require an URL while other things (BuildSteps) require only the host.
    # Since they're both right here it shouldn't be
    # a problem to keep them in sync.
    'hgurl': 'http://hg.mozilla.org/',
    'hghost': 'hg.mozilla.org',
    'config_subdir': 'mozilla2',
    'objdir': 'obj-firefox',
    'mobile_objdir': 'obj-fennec',
    'objdir_unittests': 'objdir',
    'stage_username': 'ffxbld',
    'stage_username_xulrunner': 'xrbld',
    'stage_username_mobile': 'ffxbld',
    'stage_base_path': '/home/ftp/pub/firefox',
    'stage_base_path_xulrunner': '/home/ftp/pub/xulrunner',
    'stage_base_path_mobile': '/home/ftp/pub/mobile',
    'stage_group': None,
    'stage_ssh_key': 'ffxbld_dsa',
    'stage_ssh_xulrunner_key': 'xrbld_dsa',
    'stage_ssh_mobile_key': 'ffxbld_dsa',
    'symbol_server_path': '/mnt/netapp/breakpad/symbols_ffx/',
    'symbol_server_post_upload_cmd': '/usr/local/bin/post-symbol-upload.py',
    'symbol_server_mobile_path': '/mnt/netapp/breakpad/symbols_mob/',
    'symbol_server_xulrunner_path': '/mnt/netapp/breakpad/symbols_xr/',
    'aus2_user': 'cltbld',
    'aus2_ssh_key': 'cltbld_dsa',
    'hg_username': 'ffxbld',
    'hg_ssh_key': '~cltbld/.ssh/ffxbld_dsa',
    'graph_selector': '/server/collect.cgi',
    'compare_locales_repo_path': 'build/compare-locales',
    'compare_locales_tag': 'RELEASE_AUTOMATION',
    'default_build_space': 5,
    'default_l10n_space': 3,
    'default_clobber_time': 24*7, # 1 week
    'unittest_suites': [
        ('mochitests', dict(suite='mochitest-plain', chunkByDir=4, totalChunks=5)),
        ('mochitest-other', ['mochitest-chrome', 'mochitest-browser-chrome',
            'mochitest-a11y', 'mochitest-ipcplugins']),
        ('reftest', ['reftest']),
        ('crashtest', ['crashtest']),
        ('xpcshell', ['xpcshell']),
        ('jsreftest', ['jsreftest']),
    ],
    'geriatric_masters': [],
    'platforms': {
        'linux': {},
        'linuxqt': {},
        'linux64': {},
        'win32': {},
        'macosx64': {},
        'linux-debug': {},
        'linux64-debug': {},
        'macosx-debug': {},
        'macosx64-debug': {},
        'win32-debug': {},
    },
    'mobile_repo_path': 'mobile-browser',
    'mobile_platforms': {
        'maemo5-gtk': {},
        'maemo5-qt': {},
        'android-r7': {},
        'android-r7-nothumb': {},
        'linux': {},
        'win32': {},
        'macosx': {},
    },
    'product_name': 'firefox',
    'app_name': 'browser',
    'brand_name': 'Minefield',
    'enable_shark': True,
    'enable_codecoverage': False,
    'enable_blocklist_update': False,
    'blocklist_update_on_closed_tree': False,
    'enable_nightly': True,

    # if true, this branch will get bundled and uploaded to ftp.m.o for users
    # to download and thereby accelerate their cloning
    'enable_weekly_bundle': False,

    'enable_mobile_nightly': True,
    'enable_mobile_dep': True,
    'hash_type': 'sha512',
    'create_snippet': False,
    'create_partial': False,
    'create_partial_l10n': False,
    'l10n_modules': [
            'browser', 'extensions/reporter',
            'other-licenses/branding/firefox', 'netwerk', 'dom', 'toolkit',
            'security/manager',
            'sync/services',
            ],
    'scratchbox_path': '/builds/scratchbox/moz_scratchbox',
    'scratchbox_home': '/scratchbox/users/cltbld/home/cltbld',
    'use_old_updater': False,

}
GLOBAL_VARS.update(localconfig.GLOBAL_VARS.copy())

# shorthand, because these are used often
OBJDIR = GLOBAL_VARS['objdir']
MOBILE_OBJDIR = GLOBAL_VARS['mobile_objdir']
SYMBOL_SERVER_PATH = GLOBAL_VARS['symbol_server_path']
SYMBOL_SERVER_POST_UPLOAD_CMD = GLOBAL_VARS['symbol_server_post_upload_cmd']
SYMBOL_SERVER_MOBILE_PATH = GLOBAL_VARS['symbol_server_mobile_path']

MOBILE_PLATFORM_VARS = {
    'maemo5-gtk':{
        'base_name': 'Maemo 5 GTK %(branch)s',
        'mozconfig': 'mobile/maemo5-gtk/mobile-browser/nightly',
        'profiled_build': False,
        'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
        'build_space': 6,
        'generate_symbols': True,
        'slaves': SLAVES['linux'],
        'platform_objdir': MOBILE_OBJDIR,
        'enable_ccache': False,
        'env': {
            'CC': '/scratchbox/compilers/bin/gcc',
            'CXX': '/scratchbox/compilers/bin/g++',
            'SYMBOL_SERVER_HOST': localconfig.SYMBOL_SERVER_HOST,
            'SYMBOL_SERVER_USER': 'ffxbld',
            'SYMBOL_SERVER_PATH': SYMBOL_SERVER_MOBILE_PATH,
            'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
            'SYMBOL_SERVER_SSH_KEY': "/home/cltbld/.ssh/ffxbld_dsa",
            'MOZ_OBJDIR': MOBILE_OBJDIR,
            'CCACHE_DIR': '/builds/slave/ccache',
            'CCACHE_UMASK': '002',
        },
        'package_globlist': ['dist/*.tar.bz2', 'dist/*.zip',
                             'mobile/*.deb', 'dist/deb_name.txt'],
        'upload_platform': 'linux',
        'scratchbox_target': 'FREMANTLE_ARMEL',
        'multi_locale': False,
        'l10n_repo_path': 'l10n-central',
        'compare_locales_tag': 'RELEASE_AUTOMATION',
        'l10n_tag': 'default',
        'merge_locales': True,
    },
    'maemo5-qt':{
        'base_name': 'Maemo 5 QT %(branch)s',
        'mozconfig': 'mobile/maemo5-qt/mobile-browser/nightly',
        'profiled_build': False,
        'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
        'build_space': 6,
        'generate_symbols': True,
        'slaves': SLAVES['linux'],
        'platform_objdir': MOBILE_OBJDIR,
        'enable_ccache': False,
        'env': {
            'CC': '/scratchbox/compilers/bin/gcc',
            'CXX': '/scratchbox/compilers/bin/g++',
            'SYMBOL_SERVER_HOST': localconfig.SYMBOL_SERVER_HOST,
            'SYMBOL_SERVER_USER': 'ffxbld',
            'SYMBOL_SERVER_PATH': SYMBOL_SERVER_MOBILE_PATH,
            'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
            'SYMBOL_SERVER_SSH_KEY': "/home/cltbld/.ssh/ffxbld_dsa",
            'MOZ_OBJDIR': MOBILE_OBJDIR,
            'CCACHE_DIR': '/builds/slave/ccache',
            'CCACHE_UMASK': '002',
        },
        'package_globlist': ['dist/*.tar.bz2', 'dist/*.zip',
                             'mobile/*.deb', 'dist/deb_name.txt'],
        'upload_platform': 'linux',
        'scratchbox_target': 'FREMANTLE_ARMEL',
        'multi_locale': False,
        'l10n_repo_path': 'l10n-central',
        'compare_locales_tag': 'RELEASE_AUTOMATION',
        'l10n_tag': 'default',
        'merge_locales': True,
    },
    'android-r7': {
        'base_name': 'Android R7 %(branch)s',
        'mozconfig': 'mobile/android/mobile-browser/nightly',
        'mozharness_config': 'multi_locale/trunk_android.json',
        'profiled_build': False,
        'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
        'build_space': 6,
        'generate_symbols': True,
        'slaves': SLAVES['linux'],
        'platform_objdir': MOBILE_OBJDIR,
        'enable_ccache': True,
        'update_platform': 'Android_arm-eabi-gcc3',
        'env': {
            'JAVA_HOME': '/tools/jdk6',
            'PATH': '/tools/jdk6/bin:/opt/local/bin:/tools/python/bin:/tools/buildbot/bin:/usr/kerberos/bin:/usr/local/bin:/bin:/usr/bin:/home/',
            'SYMBOL_SERVER_HOST': localconfig.SYMBOL_SERVER_HOST,
            'SYMBOL_SERVER_USER': 'ffxbld',
            'SYMBOL_SERVER_PATH': SYMBOL_SERVER_MOBILE_PATH,
            'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
            'SYMBOL_SERVER_SSH_KEY': "/home/cltbld/.ssh/ffxbld_dsa",
            'MOZ_OBJDIR': MOBILE_OBJDIR,
            'CCACHE_DIR': '/builds/slave/ccache',
            'CCACHE_UMASK': '002',
            'LC_ALL': 'C',
        },
        'multi_locale': True,
        'package_globlist': ['embedding/android/*.apk'],
        'talos_masters': GLOBAL_VARS['talos_masters'],
    },
    'android-r7-nothumb': {
        'base_name': 'Android R7 Thumbless %(branch)s',
        'mozconfig': 'mobile/android-nothumb/mobile-browser/nightly',
        'profiled_build': False,
        'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
        'build_space': 6,
        'generate_symbols': True,
        'slaves': SLAVES['linux'],
        'platform_objdir': MOBILE_OBJDIR,
        'enable_ccache': True,
        'enable_mobile_dep': False,
        'env': {
            'JAVA_HOME': '/tools/jdk6',
            'PATH': '/tools/jdk6/bin:/opt/local/bin:/tools/python/bin:/tools/buildbot/bin:/usr/kerberos/bin:/usr/local/bin:/bin:/usr/bin:/home/',
            'SYMBOL_SERVER_HOST': localconfig.SYMBOL_SERVER_HOST,
            'SYMBOL_SERVER_USER': 'ffxbld',
            'SYMBOL_SERVER_PATH': SYMBOL_SERVER_MOBILE_PATH,
            'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
            'SYMBOL_SERVER_SSH_KEY': "/home/cltbld/.ssh/ffxbld_dsa",
            'MOZ_OBJDIR': MOBILE_OBJDIR,
            'CCACHE_DIR': '/builds/slave/ccache',
            'CCACHE_UMASK': '002',
            'LC_ALL': 'C',
        },
        'package_globlist': ['embedding/android/*.apk'],
    },
    'linux': {
        'base_name': 'Linux Mobile Desktop %(branch)s',
        'mozconfig': 'mobile/linux-i686/mobile-browser/nightly',
        'profiled_build': False,
        'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
        'build_space': 6,
        'generate_symbols': True,
        'l10n_chunks': 6,
        'slaves': SLAVES['linux'],
        'platform_objdir': MOBILE_OBJDIR,
        'enable_ccache': True,
        'env': {
            'HG_SHARE_BASE_DIR': '/builds/hg-shared',
            'SYMBOL_SERVER_HOST': localconfig.SYMBOL_SERVER_HOST,
            'SYMBOL_SERVER_USER': 'ffxbld',
            'SYMBOL_SERVER_PATH': SYMBOL_SERVER_MOBILE_PATH,
            'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
            'SYMBOL_SERVER_SSH_KEY': "/home/cltbld/.ssh/ffxbld_dsa",
            'MOZ_OBJDIR': MOBILE_OBJDIR,
            'CCACHE_DIR': '/builds/slave/ccache',
            'CCACHE_UMASK': '002',
            'LC_ALL': 'C',
        },
        'package_globlist': ['-r', 'dist/*.tar.bz2', 'dist/*.zip'],
    },
    'macosx': {
        'base_name': 'OS X 10.5.2 Mobile Desktop %(branch)s',
        'mozconfig': 'mobile/macosx-i686/mobile-browser/nightly',
        'profiled_build': False,
        'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
        'build_space': 6,
        'generate_symbols': True,
        'slaves': SLAVES['macosx'],
        'platform_objdir': MOBILE_OBJDIR,
        'enable_ccache': True,
        'enable_mobile_dep': False,
        'env': {
            'SYMBOL_SERVER_HOST': localconfig.SYMBOL_SERVER_HOST,
            'SYMBOL_SERVER_USER': 'ffxbld',
            'SYMBOL_SERVER_PATH': SYMBOL_SERVER_MOBILE_PATH,
            'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
            'SYMBOL_SERVER_SSH_KEY': "/Users/cltbld/.ssh/ffxbld_dsa",
            'MOZ_OBJDIR': MOBILE_OBJDIR,
            'CCACHE_DIR': '/builds/slave/ccache',
            'CCACHE_UMASK': '002',
            'CHOWN_ROOT': '~/bin/chown_root',
            'CHOWN_REVERT': '~/bin/chown_revert',
            'LC_ALL': 'C',
        },
        'package_globlist': ['-r', 'dist/*.dmg'],
     },
     'win32': {
        'base_name': 'WINNT 5.2 Mobile Desktop %(branch)s',
        'mozconfig': 'mobile/win32-i686/mobile-browser/nightly',
        'profiled_build': False,
        'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
        'build_space': 6,
        'generate_symbols': True,
        'l10n_chunks': 6,
        'slaves': SLAVES['win32'],
        'platform_objdir': MOBILE_OBJDIR,
        'enable_mobile_dep': False,
        'env': {
            'SYMBOL_SERVER_HOST': localconfig.SYMBOL_SERVER_HOST,
            'SYMBOL_SERVER_USER': 'ffxbld',
            'SYMBOL_SERVER_PATH': SYMBOL_SERVER_MOBILE_PATH,
            'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
            'SYMBOL_SERVER_SSH_KEY': "/c/Documents and Settings/cltbld/.ssh/ffxbld_dsa",
            'MOZ_OBJDIR': MOBILE_OBJDIR,
        },
        'package_globlist': ['-r', 'dist/*.zip'],
    },
}


PLATFORM_VARS = {
        'linux': {
            'base_name': 'Linux %(branch)s',
            'mozconfig': 'linux/%(branch)s/nightly',
            'profiled_build': False,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 6,
            'upload_symbols': True,
            'download_symbols': True,
            'packageTests': True,
            'slaves': SLAVES['linux'],
            'platform_objdir': OBJDIR,
            'update_platform': 'Linux_x86-gcc3',
            'enable_ccache': True,
            'enable_shared_checkouts': True,
            'env': {
                'DISPLAY': ':2',
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': localconfig.SYMBOL_SERVER_HOST,
                'SYMBOL_SERVER_USER': 'ffxbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
                'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
                'SYMBOL_SERVER_SSH_KEY': "/home/cltbld/.ssh/ffxbld_dsa",
                'TINDERBOX_OUTPUT': '1',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_COMPRESS': '1',
                'CCACHE_UMASK': '002',
                'LC_ALL': 'C',
            },
            'enable_opt_unittests': False,
            'enable_checktests': True,
            'talos_masters': GLOBAL_VARS['talos_masters'],
        },
        'linuxqt': {
            'base_name': 'Linux QT %(branch)s',
            'mozconfig': 'linux/%(branch)s/qt',
            'xr_mozconfig': 'linux/%(branch)s/xulrunner-qt',
            'profiled_build': False,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 6,
            'upload_symbols': True,
            'download_symbols': True,
            'packageTests': True,
            'slaves': SLAVES['linux'],
            'platform_objdir': OBJDIR,
            'update_platform': 'Linux_x86-gcc3',
            'enable_ccache': True,
            'enable_shared_checkouts': True,
            'enable_nightly': False,
            'env': {
                'DISPLAY': ':2',
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': localconfig.SYMBOL_SERVER_HOST,
                'SYMBOL_SERVER_USER': 'ffxbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
                'SYMBOL_SERVER_SSH_KEY': "/home/cltbld/.ssh/ffxbld_dsa",
                'TINDERBOX_OUTPUT': '1',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_COMPRESS': '1',
                'CCACHE_UMASK': '002',
                'LC_ALL': 'C',
            },
            'enable_opt_unittests': False,
            'enable_checktests': True,
            'talos_masters': None #GLOBAL_VARS['talos_masters'],
        },
        'linux64': {
            'base_name': 'Linux x86-64 %(branch)s',
            'mozconfig': 'linux64/%(branch)s/nightly',
            'profiled_build': False,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 6,
            'upload_symbols': True,
            'download_symbols': False,
            'packageTests': True,
            'slaves': SLAVES['linux64'],
            'platform_objdir': OBJDIR,
            'update_platform': 'Linux_x86_64-gcc3',
            'enable_shared_checkouts': True,
            'env': {
                'DISPLAY': ':2',
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': localconfig.SYMBOL_SERVER_HOST,
                'SYMBOL_SERVER_USER': 'ffxbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
                'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
                'SYMBOL_SERVER_SSH_KEY': "/home/cltbld/.ssh/ffxbld_dsa",
                'MOZ_SYMBOLS_EXTRA_BUILDID': 'linux64',
                'TINDERBOX_OUTPUT': '1',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_COMPRESS': '1',
                'CCACHE_UMASK': '002',
                'LC_ALL': 'C',
            },
            'enable_opt_unittests': False,
            'enable_checktests': True,
            'talos_masters': GLOBAL_VARS['talos_masters'],
        },
        'macosx': {
            'base_name': 'OS X 10.5.2 %(branch)s',
            'mozconfig': 'macosx/%(branch)s/nightly',
            'profiled_build': False,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 10,
            'upload_symbols': True,
            'download_symbols': True,
            'packageTests': True,
            'slaves': SLAVES['macosx'],
            'platform_objdir': "%s/ppc" % OBJDIR,
            'update_platform': 'Darwin_Universal-gcc3',
            'enable_shared_checkouts': True,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': localconfig.SYMBOL_SERVER_HOST,
                'SYMBOL_SERVER_USER': 'ffxbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
                'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
                'SYMBOL_SERVER_SSH_KEY': "/Users/cltbld/.ssh/ffxbld_dsa",
                'TINDERBOX_OUTPUT': '1',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'CHOWN_ROOT': '~/bin/chown_root',
                'CHOWN_REVERT': '~/bin/chown_revert',
                'LC_ALL': 'C',
            },
            'enable_opt_unittests': False,
            'enable_checktests': True,
            'talos_masters': GLOBAL_VARS['talos_masters'],
        },
        'macosx64': {
            'base_name': 'OS X 10.6.2 %(branch)s',
            'mozconfig': 'macosx64/%(branch)s/nightly',
            'packageTests': True,
            'profiled_build': False,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 12,
            'upload_symbols': True,
            'download_symbols': True,
            'slaves': SLAVES['macosx64'],
            'platform_objdir': "%s/i386" % OBJDIR,
            'update_platform': 'Darwin_x86_64-gcc3',
            'enable_shared_checkouts': True,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'SYMBOL_SERVER_HOST': localconfig.SYMBOL_SERVER_HOST,
                'SYMBOL_SERVER_USER': 'ffxbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
                'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
                'SYMBOL_SERVER_SSH_KEY': "/Users/cltbld/.ssh/ffxbld_dsa",
                'MOZ_SYMBOLS_EXTRA_BUILDID': 'macosx64',
                'TINDERBOX_OUTPUT': '1',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'CHOWN_ROOT': '~/bin/chown_root',
                'CHOWN_REVERT': '~/bin/chown_revert',
                'LC_ALL': 'C',
            },
            'enable_opt_unittests': False,
            'enable_checktests': True,
            'talos_masters': GLOBAL_VARS['talos_masters'],
        },
        'win32': {
            'base_name': 'WINNT 5.2 %(branch)s',
            'mozconfig': 'win32/%(branch)s/nightly',
            'profiled_build': True,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'build_space': 12,
            'upload_symbols': True,
            'download_symbols': True,
            'packageTests': True,
            'slaves': SLAVES['win32'],
            'platform_objdir': OBJDIR,
            'mochitest_leak_threshold': 484,
            'crashtest_leak_threshold': 484,
            'update_platform': 'WINNT_x86-msvc',
            'enable_shared_checkouts': True,
            'env': {
                'CVS_RSH': 'ssh',
                'MOZ_OBJDIR': OBJDIR,
                'SYMBOL_SERVER_HOST': localconfig.SYMBOL_SERVER_HOST,
                'SYMBOL_SERVER_USER': 'ffxbld',
                'SYMBOL_SERVER_PATH': SYMBOL_SERVER_PATH,
                'POST_SYMBOL_UPLOAD_CMD': SYMBOL_SERVER_POST_UPLOAD_CMD,
                'SYMBOL_SERVER_SSH_KEY': "/c/Documents and Settings/cltbld/.ssh/ffxbld_dsa",
                'TINDERBOX_OUTPUT': '1',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                # Source server support, bug 506702
                'PDBSTR_PATH': '/c/Program Files/Debugging Tools for Windows/srcsrv/pdbstr.exe',
                'HG_SHARE_BASE_DIR': 'e:/builds/hg-shared',
            },
            'enable_opt_unittests': False,
            'enable_checktests': True,
            'talos_masters': GLOBAL_VARS['talos_masters'],
        },
        'linux-debug': {
            'base_name': 'Linux %(branch)s leak test',
            'mozconfig': 'linux/%(branch)s/debug',
            'profiled_build': False,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'download_symbols': True,
            'packageTests': True,
            'build_space': 7,
            'slaves': SLAVES['linux'],
            'platform_objdir': OBJDIR,
            'enable_ccache': True,
            'enable_shared_checkouts': True,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'DISPLAY': ':2',
                'LD_LIBRARY_PATH': '%s/dist/bin' % OBJDIR,
                'XPCOM_DEBUG_BREAK': 'stack-and-abort',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_COMPRESS': '1',
                'CCACHE_UMASK': '002',
                'LC_ALL': 'C',
            },
            'enable_unittests': False,
            'enable_checktests': True,
            'talos_masters': GLOBAL_VARS['talos_masters'],
        },
        'linux64-debug': {
            'base_name': 'Linux x86-64 %(branch)s leak test',
            'mozconfig': 'linux64/%(branch)s/debug',
            'profiled_build': False,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'download_symbols': False,
            'packageTests': True,
            'build_space': 7,
            'slaves': SLAVES['linux64'],
            'platform_objdir': OBJDIR,
            'enable_ccache': False,
            'enable_shared_checkouts': True,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'DISPLAY': ':2',
                'LD_LIBRARY_PATH': '%s/dist/bin' % OBJDIR,
                'XPCOM_DEBUG_BREAK': 'stack-and-abort',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'CCACHE_DIR': '/builds/ccache',
                'CCACHE_COMPRESS': '1',
                'CCACHE_UMASK': '002',
                'LC_ALL': 'C',
            },
            'enable_unittests': False,
            'enable_checktests': True,
            'talos_masters': GLOBAL_VARS['talos_masters'],
        },
        'macosx-debug': {
            'base_name': 'OS X 10.5.2 %(branch)s leak test',
            'mozconfig': 'macosx/%(branch)s/debug',
            'profiled_build': False,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'download_symbols': True,
            'packageTests': True,
            'build_space': 10,
            'slaves': SLAVES['macosx'],
            'platform_objdir': OBJDIR,
            'enable_shared_checkouts': True,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'XPCOM_DEBUG_BREAK': 'stack-and-abort',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'LC_ALL': 'C',
            },
            'enable_unittests': False,
            'enable_checktests': True,
            'talos_masters': GLOBAL_VARS['talos_masters'],
        },
        'macosx64-debug': {
            'base_name': 'OS X 10.6.2 %(branch)s leak test',
            'mozconfig': 'macosx64/%(branch)s/debug',
            'packageTests': True,
            'profiled_build': False,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'download_symbols': True,
            'build_space': 10,
            'slaves': SLAVES['macosx64'],
            'platform_objdir': OBJDIR,
            'enable_shared_checkouts': True,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'HG_SHARE_BASE_DIR': '/builds/hg-shared',
                'XPCOM_DEBUG_BREAK': 'stack-and-abort',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'LC_ALL': 'C',
            },
            'enable_unittests': False,
            'enable_checktests': True,
            'talos_masters': GLOBAL_VARS['talos_masters'],
        },
        'win32-debug': {
            'base_name': 'WINNT 5.2 %(branch)s leak test',
            'mozconfig': 'win32/%(branch)s/debug',
            'profiled_build': False,
            'builds_before_reboot': localconfig.BUILDS_BEFORE_REBOOT,
            'download_symbols': True,
            'packageTests': True,
            'build_space': 9,
            'slaves': SLAVES['win32'],
            'platform_objdir': OBJDIR,
            'enable_shared_checkouts': True,
            'env': {
                'MOZ_OBJDIR': OBJDIR,
                'XPCOM_DEBUG_BREAK': 'stack-and-abort',
                'MOZ_CRASHREPORTER_NO_REPORT': '1',
                'HG_SHARE_BASE_DIR': 'e:/builds/hg-shared',
            },
            'enable_unittests': False,
            'enable_checktests': True,
            'talos_masters': GLOBAL_VARS['talos_masters'],
        },
}

PROJECTS = {
    'fuzzing': {
        'platforms': ['linux', 'linux64', 'macosx', 'macosx64', 'win32'],
    },
    'nanojit': {
        'platforms': ['linux', 'linux64', 'macosx', 'macosx64', 'win32', 'arm'],
        'hgurl': 'http://hg.mozilla.org',
        'repo_path': 'projects/nanojit-central',
    },
    'valgrind': {
        'platforms': ['linux', 'linux64'],
        'job_interval': 24*3600, # Once a day
        'linux': {'env': PLATFORM_VARS['linux']['env']},
        'linux64': {'env': PLATFORM_VARS['linux64']['env']},
    },
    'spidermonkey': {
        'platforms': {
            'linux':    ['nomethodjit', 'notracejit'],
            'linux64':  ['nomethodjit', 'notracejit'],
            'win32':    ['nomethodjit', 'notracejit'],
            'macosx64': ['nomethodjit', 'notracejit', 'dtrace', 'shark'],
            'macosx':   ['nomethodjit', 'notracejit', 'dtrace', 'shark'],
        },
        'env': {
            'linux': PLATFORM_VARS['linux']['env'],
            'linux64': PLATFORM_VARS['linux64']['env'],
            'win32': PLATFORM_VARS['win32']['env'],
            'macosx64': PLATFORM_VARS['macosx64']['env'],
            'macosx': PLATFORM_VARS['macosx']['env'],
        },
        'hgurl': 'http://hg.mozilla.org',
        'repo_path': 'tracemonkey',
    },
}

for k, v in localconfig.PROJECTS.items():
    if k not in PROJECTS:
        PROJECTS[k] = {}
    for k1, v1 in v.items():
        PROJECTS[k][k1] = v1


# All branches that are to be built MUST be listed here, along with their
# platforms (if different from the default set).
BRANCHES = {
    'mozilla-central': {
        'mobile_platforms': {
            'android-r7': {},
            'android-r7-nothumb': {},
            'linux': {},
            'win32': {},
        }
    },
    'shadow-central': {
        'mobile_platforms': {},
    },
    'mozilla-2.0': {
        'mobile_platforms': {},
    },
    'mozilla-1.9.1': {
        'platforms': {
            'linux': {}, 'linux-debug': {}, 'linux64': {}, 'linux64-debug': {},
            'macosx': {}, 'macosx-debug': {}, 'win32': {}, 'win32-debug': {},
        },
        'mobile_platforms': {},
    },
    'mozilla-1.9.2': {
        'platforms': {
            'linux': {}, 'linux-debug': {}, 'linux64': {}, 'linux64-debug': {},
            'macosx': {}, 'macosx-debug': {}, 'win32': {}, 'win32-debug': {},
        },
        'mobile_platforms': {},
    },
    'tracemonkey': {
    },
    'places': {
    },
    'electrolysis': {
    },
    'jaegermonkey': {
    },
    'tryserver': {
        'mobile_platforms': {
            'maemo5-gtk': {},
            'maemo5-qt': {},
            'android-r7': {},
        },
    },
}

# Copy project branches into BRANCHES keys
for key, value in PROJECT_BRANCHES.items():
    BRANCHES[key] = value

# Copy global vars in first, then platform vars
for branch in BRANCHES.keys():
    for key, value in GLOBAL_VARS.items():
        # Don't override platforms if it's set
        if key == 'platforms' and 'platforms' in BRANCHES[branch]:
            continue
        elif key == 'mobile_platforms' and 'mobile_platforms' in BRANCHES[branch]:
            continue
        BRANCHES[branch][key] = deepcopy(value)

    for platform, platform_config in PLATFORM_VARS.items():
        if platform in BRANCHES[branch]['platforms']:
            for key, value in platform_config.items():
                value = deepcopy(value)
                if isinstance(value, str):
                    value = value % locals()
                BRANCHES[branch]['platforms'][platform][key] = value

    for mobile_platform, mobile_platform_config in MOBILE_PLATFORM_VARS.items():
        if mobile_platform in BRANCHES[branch]['mobile_platforms'].keys():
            BRANCHES[branch]['mobile_platforms'][mobile_platform] = deepcopy(mobile_platform_config)

    # Copy in local config
    if branch in localconfig.BRANCHES:
        for key, value in localconfig.BRANCHES[branch].items():
            if key == 'platforms':
                # Merge in these values
                if 'platforms' not in BRANCHES[branch]:
                    BRANCHES[branch]['platforms'] = {}

                for platform, platform_config in value.items():
                    for key, value in platform_config.items():
                        value = deepcopy(value)
                        if isinstance(value, str):
                            value = value % locals()
                        BRANCHES[branch]['platforms'][platform][key] = value
            else:
                BRANCHES[branch][key] = deepcopy(value)

    for platform, platform_config in localconfig.PLATFORM_VARS.items():
        if platform in BRANCHES[branch]['platforms']:
            for key, value in platform_config.items():
                value = deepcopy(value)
                if isinstance(value, str):
                    value = value % locals()
                BRANCHES[branch]['platforms'][platform][key] = value

    for mobile_platform, mobile_platform_config in MOBILE_PLATFORM_VARS.items():
        if mobile_platform in BRANCHES[branch]['mobile_platforms']:
            BRANCHES[branch]['mobile_platforms'][mobile_platform] = deepcopy(mobile_platform_config)


######## mozilla-central
# This is a path, relative to HGURL, where the repository is located
# HGURL + repo_path should be a valid repository
BRANCHES['mozilla-central']['repo_path'] = 'mozilla-central'
BRANCHES['mozilla-central']['l10n_repo_path'] = 'l10n-central'
BRANCHES['mozilla-central']['start_hour'] = [3]
BRANCHES['mozilla-central']['start_minute'] = [2]
# Enable XULRunner / SDK builds
BRANCHES['mozilla-central']['enable_xulrunner'] = True
# Enable unit tests
BRANCHES['mozilla-central']['geriatric_masters'] = [
    ('10.250.48.137:9989', False),
]
BRANCHES['mozilla-central']['enable_mac_a11y'] = True
BRANCHES['mozilla-central']['enable_weekly_bundle'] = True
BRANCHES['mozilla-central']['unittest_build_space'] = 6
# And code coverage
BRANCHES['mozilla-central']['enable_codecoverage'] = True
# L10n configuration
BRANCHES['mozilla-central']['enable_l10n'] = True
BRANCHES['mozilla-central']['enable_l10n_onchange'] = True
BRANCHES['mozilla-central']['l10nNightlyUpdate'] = True
BRANCHES['mozilla-central']['l10n_platforms'] = ['linux', 'linux64', 'win32',
                                                 'macosx64']
BRANCHES['mozilla-central']['l10nDatedDirs'] = True
BRANCHES['mozilla-central']['l10n_tree'] = 'fx37x'
#make sure it has an ending slash
BRANCHES['mozilla-central']['l10nUploadPath'] = \
    '/home/ftp/pub/mozilla.org/firefox/nightly/latest-mozilla-central-l10n/'
BRANCHES['mozilla-central']['enUS_binaryURL'] = \
    GLOBAL_VARS['download_base_url'] + '/nightly/latest-mozilla-central'
BRANCHES['mozilla-central']['allLocalesFile'] = 'browser/locales/all-locales'
BRANCHES['mozilla-central']['enable_multi_locale'] = True
BRANCHES['mozilla-central']['upload_mobile_symbols'] = True
# If True, a complete update snippet for this branch will be generated and
# uploaded to. Any platforms with 'debug' in them will not have snippets
# generated.
BRANCHES['mozilla-central']['create_snippet'] = True
BRANCHES['mozilla-central']['create_mobile_snippet'] = True
BRANCHES['mozilla-central']['create_partial'] = True
BRANCHES['mozilla-central']['create_partial_l10n'] = True
BRANCHES['mozilla-central']['aus2_user'] = 'ffxbld'
BRANCHES['mozilla-central']['aus2_ssh_key'] = 'ffxbld_dsa'
BRANCHES['mozilla-central']['aus2_base_upload_dir'] = '/opt/aus2/incoming/2/Firefox/mozilla-central'
BRANCHES['mozilla-central']['aus2_base_upload_dir_l10n'] = '/opt/aus2/incoming/2/Firefox/mozilla-central'
BRANCHES['mozilla-central']['aus2_mobile_base_upload_dir'] = '/opt/aus2/incoming/2/Fennec/mozilla-central'
BRANCHES['mozilla-central']['aus2_mobile_base_upload_dir_l10n'] = '/opt/aus2/incoming/2/Fennec/mozilla-central'
BRANCHES['mozilla-central']['mobile_platforms']['android-r7']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'mozilla-central'
BRANCHES['mozilla-central']['mobile_platforms']['android-r7-nothumb']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'mozilla-central-nothumb'
BRANCHES['mozilla-central']['enable_blocklist_update'] = True
BRANCHES['mozilla-central']['blocklist_update_on_closed_tree'] = True

######## shadow-central
# custom settings for shadow-central repo
BRANCHES['shadow-central']['hgurl'] = 'https://hgpvt.mozilla.org/'
# have to use complete config repo path so it doesn't look to https://hgpvt.mozilla.org
BRANCHES['shadow-central']['config_repo_path'] = 'http://hg.mozilla.org/build/buildbot-configs'
# This is a path, relative to HGURL, where the repository is located
# HGURL + repo_path should be a valid repository
BRANCHES['shadow-central']['repo_path'] = 'shadow-central'
BRANCHES['shadow-central']['start_hour'] = [3]
BRANCHES['shadow-central']['start_minute'] = [2]
BRANCHES['shadow-central']['create_snippet'] = False
BRANCHES['shadow-central']['enable_nightly'] = False
# Enable XULRunner / SDK builds
BRANCHES['shadow-central']['enable_xulrunner'] = False
# Disable codesighs for now until ability to upload/download from secure server exists bug 581106
BRANCHES['shadow-central']['enable_codesighs'] = True
# Enable unit tests
BRANCHES['shadow-central']['enable_mac_a11y'] = True
BRANCHES['shadow-central']['unittest_build_space'] = 6
# L10n configuration
BRANCHES['shadow-central']['enable_l10n'] = False
BRANCHES['shadow-central']['l10nNightlyUpdate'] = False
BRANCHES['shadow-central']['l10nDatedDirs'] = False
# need this or master.cfg will bail
BRANCHES['shadow-central']['aus2_base_upload_dir'] = 'fake'
BRANCHES['shadow-central']['platforms']['linux']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'shadow-central'
BRANCHES['shadow-central']['platforms']['linuxqt']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'shadow-central'
BRANCHES['shadow-central']['platforms']['linux64']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'linux64-shadow-central'
BRANCHES['shadow-central']['platforms']['win32']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'shadow-central'
BRANCHES['shadow-central']['platforms']['macosx64']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'macosx64-shadow-central'

######## mozilla-2.0
BRANCHES['mozilla-2.0']['repo_path'] = 'releases/mozilla-2.0'
BRANCHES['mozilla-2.0']['l10n_repo_path'] = 'l10n-central'
BRANCHES['mozilla-2.0']['start_hour'] = [3]
BRANCHES['mozilla-2.0']['start_minute'] = [2]
# Enable XULRunner / SDK builds
BRANCHES['mozilla-2.0']['enable_xulrunner'] = True
# Enable unit tests
BRANCHES['mozilla-2.0']['geriatric_masters'] = [
    ('10.250.48.137:9989', False),
]
BRANCHES['mozilla-2.0']['enable_mac_a11y'] = True
BRANCHES['mozilla-2.0']['unittest_build_space'] = 6
# And code coverage
BRANCHES['mozilla-2.0']['enable_codecoverage'] = False
BRANCHES['mozilla-2.0']['enable_blocklist_update'] = False
BRANCHES['mozilla-2.0']['blocklist_update_on_closed_tree'] = False
# L10n configuration
BRANCHES['mozilla-2.0']['enable_l10n'] = True
BRANCHES['mozilla-2.0']['enable_l10n_onchange'] = True
BRANCHES['mozilla-2.0']['l10nNightlyUpdate'] = True
BRANCHES['mozilla-2.0']['l10n_platforms'] = ['linux' , 'linux64', 'win32',
                                             'macosx64']
BRANCHES['mozilla-2.0']['l10nDatedDirs'] = True
BRANCHES['mozilla-2.0']['l10n_tree'] = 'fx40x'
#make sure it has an ending slash
BRANCHES['mozilla-2.0']['l10nUploadPath'] = \
    '/home/ftp/pub/mozilla.org/firefox/nightly/latest-mozilla-2.0-l10n/'
BRANCHES['mozilla-2.0']['enUS_binaryURL'] = \
    GLOBAL_VARS['download_base_url'] + '/nightly/latest-mozilla-2.0'
BRANCHES['mozilla-2.0']['allLocalesFile'] = 'browser/locales/all-locales'
BRANCHES['mozilla-2.0']['enable_multi_locale'] = True
BRANCHES['mozilla-2.0']['upload_mobile_symbols'] = True
# If True, a complete update snippet for this branch will be generated and
# uploaded to. Any platforms with 'debug' in them will not have snippets
# generated.
BRANCHES['mozilla-2.0']['create_snippet'] = True
# turn on in bug 594867
BRANCHES['mozilla-2.0']['create_mobile_snippet'] = False
BRANCHES['mozilla-2.0']['create_partial'] = True
BRANCHES['mozilla-2.0']['create_partial_l10n'] = True
BRANCHES['mozilla-2.0']['aus2_user'] = 'ffxbld'
BRANCHES['mozilla-2.0']['aus2_ssh_key'] = 'ffxbld_dsa'
BRANCHES['mozilla-2.0']['aus2_base_upload_dir'] = '/opt/aus2/incoming/2/Firefox/mozilla-2.0'
BRANCHES['mozilla-2.0']['aus2_base_upload_dir_l10n'] = '/opt/aus2/incoming/2/Firefox/mozilla-2.0'
BRANCHES['mozilla-2.0']['aus2_mobile_base_upload_dir'] = '/opt/aus2/incoming/2/Fennec/mozilla-2.0'
BRANCHES['mozilla-2.0']['aus2_mobile_base_upload_dir_l10n'] = '/opt/aus2/incoming/2/Fennec/mozilla-2.0'

######## mozilla-1.9.1
BRANCHES['mozilla-1.9.1']['repo_path'] = 'releases/mozilla-1.9.1'
BRANCHES['mozilla-1.9.1']['l10n_repo_path'] = 'releases/l10n-mozilla-1.9.1'
BRANCHES['mozilla-1.9.1']['brand_name'] = 'Shiretoko'
BRANCHES['mozilla-1.9.1']['start_hour'] = [3]
BRANCHES['mozilla-1.9.1']['start_minute'] = [2]
BRANCHES['mozilla-1.9.1']['use_old_updater'] = True
BRANCHES['mozilla-1.9.1']['platforms']['win32']['build_space'] = 7
BRANCHES['mozilla-1.9.1']['platforms']['macosx']['build_space'] = 7
BRANCHES['mozilla-1.9.1']['platforms']['linux-debug']['build_space'] = 3
BRANCHES['mozilla-1.9.1']['platforms']['linux64-debug']['build_space'] = 3
BRANCHES['mozilla-1.9.1']['platforms']['win32-debug']['build_space'] = 4
BRANCHES['mozilla-1.9.1']['platforms']['macosx-debug']['build_space'] = 3
# Enable XULRunner / SDK builds
BRANCHES['mozilla-1.9.1']['enable_xulrunner'] = True
# Enable unit tests
BRANCHES['mozilla-1.9.1']['unittest_suites'] = [
    ('mochitests', ['mochitest-plain']),
    ('mochitest-other', ['mochitest-chrome', 'mochitest-browser-chrome',
        'mochitest-a11y']),
    ('reftest', ['reftest']),
    ('crashtest', ['crashtest']),
    ('xpcshell', ['xpcshell']),
]
BRANCHES['mozilla-1.9.1']['platforms']['linux']['enable_unittests'] = True
BRANCHES['mozilla-1.9.1']['platforms']['linux']['enable_opt_unittests'] = False
BRANCHES['mozilla-1.9.1']['platforms']['linux']['enable_checktests'] = False
BRANCHES['mozilla-1.9.1']['platforms']['linux-debug']['enable_unittests'] = False
BRANCHES['mozilla-1.9.1']['platforms']['linux-debug']['enable_checktests'] = False
BRANCHES['mozilla-1.9.1']['platforms']['linux-debug']['packageTests'] = False
BRANCHES['mozilla-1.9.1']['platforms']['linux64-debug']['enable_checktests'] = False
BRANCHES['mozilla-1.9.1']['platforms']['linux64-debug']['packageTests'] = False
BRANCHES['mozilla-1.9.1']['platforms']['macosx']['enable_unittests'] = True
BRANCHES['mozilla-1.9.1']['platforms']['macosx']['enable_opt_unittests'] = False
BRANCHES['mozilla-1.9.1']['platforms']['macosx']['enable_checktests'] = False
BRANCHES['mozilla-1.9.1']['platforms']['macosx-debug']['enable_unittests'] = False
BRANCHES['mozilla-1.9.1']['platforms']['macosx-debug']['enable_checktests'] = False
BRANCHES['mozilla-1.9.1']['platforms']['macosx-debug']['packageTests'] = False
BRANCHES['mozilla-1.9.1']['platforms']['win32']['enable_unittests'] = True
BRANCHES['mozilla-1.9.1']['platforms']['win32']['enable_opt_unittests'] = False
BRANCHES['mozilla-1.9.1']['platforms']['win32']['enable_checktests'] = False
BRANCHES['mozilla-1.9.1']['platforms']['win32-debug']['enable_unittests'] = False
BRANCHES['mozilla-1.9.1']['platforms']['win32-debug']['enable_checktests'] = False
BRANCHES['mozilla-1.9.1']['platforms']['win32-debug']['packageTests'] = False
BRANCHES['mozilla-1.9.1']['enable_mac_a11y'] = False
BRANCHES['mozilla-1.9.1']['unittest_build_space'] = 5
# L10n configuration
BRANCHES['mozilla-1.9.1']['enable_l10n'] = True
BRANCHES['mozilla-1.9.1']['enable_l10n_onchange'] = True
BRANCHES['mozilla-1.9.1']['l10n_platforms'] = ['linux','win32','macosx']
BRANCHES['mozilla-1.9.1']['l10nNightlyUpdate'] = False
BRANCHES['mozilla-1.9.1']['l10nDatedDirs'] = False
BRANCHES['mozilla-1.9.1']['l10n_tree'] = 'fx35x'
BRANCHES['mozilla-1.9.1']['l10n_modules'] =  [
    'browser', 'extensions/reporter',
    'other-licenses/branding/firefox', 'netwerk', 'dom', 'toolkit',
    'security/manager',
    ]
#make sure it has an ending slash
BRANCHES['mozilla-1.9.1']['l10nUploadPath'] = \
    '/home/ftp/pub/mozilla.org/firefox/nightly/latest-mozilla-1.9.1-l10n/'
BRANCHES['mozilla-1.9.1']['enUS_binaryURL'] = \
    GLOBAL_VARS['download_base_url'] + '/nightly/latest-mozilla-1.9.1'
BRANCHES['mozilla-1.9.1']['allLocalesFile'] = 'browser/locales/all-locales'
BRANCHES['mozilla-1.9.1']['create_snippet'] = True
BRANCHES['mozilla-1.9.1']['create_partial'] = True
BRANCHES['mozilla-1.9.1']['create_partial_l10n'] = False
BRANCHES['mozilla-1.9.1']['aus2_user'] = 'ffxbld'
BRANCHES['mozilla-1.9.1']['aus2_ssh_key'] = 'ffxbld_dsa'
BRANCHES['mozilla-1.9.1']['aus2_base_upload_dir'] = '/opt/aus2/incoming/2/Firefox/mozilla-1.9.1'
BRANCHES['mozilla-1.9.1']['aus2_base_upload_dir_l10n'] = '/opt/aus2/incoming/2/Firefox/mozilla-1.9.1'
BRANCHES['mozilla-1.9.1']['enable_blocklist_update'] = True
BRANCHES['mozilla-1.9.1']['blocklist_update_on_closed_tree'] = True

######## mozilla-1.9.2
BRANCHES['mozilla-1.9.2']['repo_path'] = 'releases/mozilla-1.9.2'
BRANCHES['mozilla-1.9.2']['mobile_repo_path'] = 'releases/mobile-1.1'
BRANCHES['mozilla-1.9.2']['l10n_repo_path'] = 'releases/l10n-mozilla-1.9.2'
BRANCHES['mozilla-1.9.2']['brand_name'] = 'Namoroka'
BRANCHES['mozilla-1.9.2']['start_hour'] = [3]
BRANCHES['mozilla-1.9.2']['start_minute'] = [32]
BRANCHES['mozilla-1.9.2']['use_old_updater'] = True
BRANCHES['mozilla-1.9.2']['platforms']['linux']['build_space'] = 8
BRANCHES['mozilla-1.9.2']['platforms']['linux64']['build_space'] = 8
BRANCHES['mozilla-1.9.2']['platforms']['win32']['build_space'] = 8
BRANCHES['mozilla-1.9.2']['platforms']['macosx']['build_space'] = 7
BRANCHES['mozilla-1.9.2']['platforms']['linux-debug']['build_space'] = 3
BRANCHES['mozilla-1.9.2']['platforms']['linux64-debug']['build_space'] = 3
BRANCHES['mozilla-1.9.2']['platforms']['win32-debug']['build_space'] = 4
BRANCHES['mozilla-1.9.2']['platforms']['macosx-debug']['build_space'] = 3
# Enable XULRunner / SDK builds
BRANCHES['mozilla-1.9.2']['enable_xulrunner'] = True
# Enable unit tests
BRANCHES['mozilla-1.9.2']['unittest_suites'] = [
    ('mochitests', ['mochitest-plain']),
    ('mochitest-other', ['mochitest-chrome', 'mochitest-browser-chrome',
        'mochitest-a11y']),
    ('reftest', ['reftest']),
    ('crashtest', ['crashtest']),
    ('xpcshell', ['xpcshell']),
]
BRANCHES['mozilla-1.9.2']['platforms']['linux']['enable_unittests'] = True
BRANCHES['mozilla-1.9.2']['platforms']['linux']['enable_checktests'] = False
BRANCHES['mozilla-1.9.2']['platforms']['linux-debug']['enable_unittests'] = False
BRANCHES['mozilla-1.9.2']['platforms']['linux-debug']['enable_checktests'] = False
BRANCHES['mozilla-1.9.2']['platforms']['linux64-debug']['enable_checktests'] = False
BRANCHES['mozilla-1.9.2']['platforms']['macosx']['enable_unittests'] = True
BRANCHES['mozilla-1.9.2']['platforms']['macosx']['enable_checktests'] = False
BRANCHES['mozilla-1.9.2']['platforms']['macosx-debug']['enable_unittests'] = False
BRANCHES['mozilla-1.9.2']['platforms']['macosx-debug']['enable_checktests'] = False
BRANCHES['mozilla-1.9.2']['platforms']['win32']['enable_unittests'] = True
BRANCHES['mozilla-1.9.2']['platforms']['win32']['enable_checktests'] = False
BRANCHES['mozilla-1.9.2']['platforms']['win32-debug']['enable_unittests'] = False
BRANCHES['mozilla-1.9.2']['platforms']['win32-debug']['enable_checktests'] = False
BRANCHES['mozilla-1.9.2']['enable_mac_a11y'] = False
BRANCHES['mozilla-1.9.2']['unittest_build_space'] = 5
# L10n configuration
BRANCHES['mozilla-1.9.2']['enable_l10n'] = True
BRANCHES['mozilla-1.9.2']['enable_l10n_onchange'] = True
BRANCHES['mozilla-1.9.2']['l10n_platforms'] = ['linux','win32','macosx']
BRANCHES['mozilla-1.9.2']['l10nNightlyUpdate'] = True
BRANCHES['mozilla-1.9.2']['l10nDatedDirs'] = True
BRANCHES['mozilla-1.9.2']['l10n_tree'] = 'fx36x'
BRANCHES['mozilla-1.9.2']['l10n_modules'] =  [
    'browser', 'extensions/reporter',
    'other-licenses/branding/firefox', 'netwerk', 'dom', 'toolkit',
    'security/manager',
    ]
#make sure it has an ending slash
BRANCHES['mozilla-1.9.2']['l10nUploadPath'] = \
    '/home/ftp/pub/mozilla.org/firefox/nightly/latest-mozilla-1.9.2-l10n/'
BRANCHES['mozilla-1.9.2']['enUS_binaryURL'] = \
    GLOBAL_VARS['download_base_url'] + '/nightly/latest-mozilla-1.9.2'
BRANCHES['mozilla-1.9.2']['allLocalesFile'] = 'browser/locales/all-locales'
BRANCHES['mozilla-1.9.2']['create_snippet'] = True
BRANCHES['mozilla-1.9.2']['create_partial'] = True
BRANCHES['mozilla-1.9.2']['create_partial_l10n'] = True
BRANCHES['mozilla-1.9.2']['aus2_user'] = 'ffxbld'
BRANCHES['mozilla-1.9.2']['aus2_ssh_key'] = 'ffxbld_dsa'
BRANCHES['mozilla-1.9.2']['aus2_base_upload_dir'] = '/opt/aus2/incoming/2/Firefox/mozilla-1.9.2'
BRANCHES['mozilla-1.9.2']['aus2_base_upload_dir_l10n'] = '/opt/aus2/incoming/2/Firefox/mozilla-1.9.2'
BRANCHES['mozilla-1.9.2']['enable_blocklist_update'] = True
BRANCHES['mozilla-1.9.2']['blocklist_update_on_closed_tree'] = True

######## tracemonkey
BRANCHES['tracemonkey']['repo_path'] = 'tracemonkey'
BRANCHES['tracemonkey']['start_hour'] = [3]
BRANCHES['tracemonkey']['start_minute'] = [32]
BRANCHES['tracemonkey']['platforms']['linux']['build_space'] = 7
BRANCHES['tracemonkey']['platforms']['linuxqt']['build_space'] = 7
BRANCHES['tracemonkey']['platforms']['linux64']['build_space'] = 7
# Disable XULRunner / SDK builds
BRANCHES['tracemonkey']['enable_xulrunner'] = False
BRANCHES['tracemonkey']['enable_mac_a11y'] = True
BRANCHES['tracemonkey']['unittest_build_space'] = 6
# L10n configuration
BRANCHES['tracemonkey']['enable_l10n'] = False
BRANCHES['tracemonkey']['enable_l10n_onchange'] = False
BRANCHES['tracemonkey']['l10nNightlyUpdate'] = False
BRANCHES['tracemonkey']['l10nDatedDirs'] = False
BRANCHES['tracemonkey']['platforms']['linux-debug']['enable_valgrind_checktests'] = True
BRANCHES['tracemonkey']['platforms']['linux64-debug']['enable_valgrind_checktests'] = True
BRANCHES['tracemonkey']['platforms']['linux']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'tracemonkey'
BRANCHES['tracemonkey']['platforms']['linuxqt']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'linuxqt-tracemonkey'
BRANCHES['tracemonkey']['platforms']['linux64']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'linux64-tracemonkey'
BRANCHES['tracemonkey']['platforms']['win32']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'tracemonkey'
BRANCHES['tracemonkey']['platforms']['macosx64']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'macosx64-tracemonkey'
BRANCHES['tracemonkey']['mobile_platforms']['maemo5-gtk']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'tracemonkey-maemo5-gtk'
BRANCHES['tracemonkey']['mobile_platforms']['maemo5-qt']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'tracemonkey-maemo5-qt'
BRANCHES['tracemonkey']['mobile_platforms']['linux']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'tracemonkey'
BRANCHES['tracemonkey']['mobile_platforms']['win32']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'tracemonkey'
BRANCHES['tracemonkey']['mobile_platforms']['macosx']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'tracemonkey'
BRANCHES['tracemonkey']['mobile_platforms']['linux']['l10n_chunks'] = None
BRANCHES['tracemonkey']['mobile_platforms']['win32']['l10n_chunks'] = None
BRANCHES['tracemonkey']['create_snippet'] = True
BRANCHES['tracemonkey']['create_partial'] = True
BRANCHES['tracemonkey']['create_partial_l10n'] = False
BRANCHES['tracemonkey']['aus2_user'] = 'ffxbld'
BRANCHES['tracemonkey']['aus2_ssh_key'] = 'ffxbld_dsa'
BRANCHES['tracemonkey']['aus2_base_upload_dir'] = '/opt/aus2/incoming/2/Firefox/tracemonkey'
BRANCHES['tracemonkey']['aus2_base_upload_dir_l10n'] = '/opt/aus2/incoming/2/Firefox/tracemonkey'

######## places
BRANCHES['places']['repo_path'] = 'projects/places'
BRANCHES['places']['start_hour'] = [4]
BRANCHES['places']['start_minute'] = [2]
BRANCHES['places']['create_snippet'] = False
BRANCHES['places']['enable_nightly'] = False
# Disable XULRunner / SDK builds
BRANCHES['places']['enable_xulrunner'] = False
BRANCHES['places']['enable_mac_a11y'] = True
BRANCHES['places']['unittest_build_space'] = 6
# L10n configuration
BRANCHES['places']['enable_l10n'] = False
BRANCHES['places']['enable_l10n_onchange'] = False
# need this or the master.cfg will bail
BRANCHES['places']['aus2_base_upload_dir'] = 'fake'
BRANCHES['places']['platforms']['linux']['update_platform'] = 'fake'
BRANCHES['places']['platforms']['linuxqt']['update_platform'] = 'fake'
BRANCHES['places']['platforms']['linux64']['update_platform'] = 'fake'
BRANCHES['places']['platforms']['win32']['update_platform'] = 'fake'
BRANCHES['places']['platforms']['linux']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'places'
BRANCHES['places']['platforms']['linuxqt']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'linuxqt-places'
BRANCHES['places']['platforms']['linux64']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'linux64-places'
BRANCHES['places']['platforms']['win32']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'places'
BRANCHES['places']['platforms']['macosx64']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'macosx64-places'
BRANCHES['places']['platforms']['linux64']['build_space'] = 6
BRANCHES['places']['platforms']['linux']['build_space'] = 6
BRANCHES['places']['platforms']['linuxqt']['build_space'] = 6
BRANCHES['places']['mobile_platforms']['linux']['l10n_chunks'] = None
BRANCHES['places']['mobile_platforms']['win32']['l10n_chunks'] = None

######## electrolysis
BRANCHES['electrolysis']['repo_path'] = 'projects/electrolysis'
BRANCHES['electrolysis']['start_hour'] = [4]
BRANCHES['electrolysis']['start_minute'] = [2]
BRANCHES['electrolysis']['enable_nightly'] = False
BRANCHES['electrolysis']['enable_mobile_nightly'] = False
# Disable XULRunner / SDK builds
BRANCHES['electrolysis']['enable_xulrunner'] = False
BRANCHES['electrolysis']['platforms']['win32']['profiled_build'] = False
BRANCHES['electrolysis']['enable_mac_a11y'] = True
BRANCHES['electrolysis']['unittest_build_space'] = 6
# L10n configuration
BRANCHES['electrolysis']['enable_l10n'] = False
BRANCHES['electrolysis']['enable_l10n_onchange'] = False
BRANCHES['electrolysis']['l10nNightlyUpdate'] = False
BRANCHES['electrolysis']['l10nDatedDirs'] = False
BRANCHES['electrolysis']['platforms']['linux']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'electrolysis'
BRANCHES['electrolysis']['platforms']['linuxqt']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'linuxqt-electrolysis'
BRANCHES['electrolysis']['platforms']['linux64']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'linux64-electrolysis'
BRANCHES['electrolysis']['platforms']['win32']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'electrolysis'
BRANCHES['electrolysis']['platforms']['macosx64']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'macosx64-electrolysis'
BRANCHES['electrolysis']['mobile_platforms']['maemo5-gtk']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'electrolysis-maemo5-gtk'
BRANCHES['electrolysis']['mobile_platforms']['maemo5-gtk']['mozconfig'] = 'mobile/maemo5-gtk/mobile-e10s/nightly'
BRANCHES['electrolysis']['mobile_platforms']['maemo5-qt']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'electrolysis-maemo5-qt'
BRANCHES['electrolysis']['mobile_platforms']['maemo5-qt']['mozconfig'] = 'mobile/maemo5-qt/mobile-e10s/nightly'
BRANCHES['electrolysis']['mobile_platforms']['linux']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'electrolysis'
BRANCHES['electrolysis']['mobile_platforms']['linux']['mozconfig'] = 'mobile/linux-i686/mobile-e10s/nightly'
BRANCHES['electrolysis']['mobile_platforms']['win32']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'electrolysis'
BRANCHES['electrolysis']['mobile_platforms']['win32']['mozconfig'] = 'mobile/win32-i686/mobile-e10s/nightly'
BRANCHES['electrolysis']['mobile_platforms']['macosx']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'electrolysis'
BRANCHES['electrolysis']['mobile_platforms']['macosx']['mozconfig'] = 'mobile/macosx-i686/mobile-e10s/nightly'
BRANCHES['electrolysis']['mobile_platforms']['linux']['l10n_chunks'] = None
BRANCHES['electrolysis']['mobile_platforms']['win32']['l10n_chunks'] = None
BRANCHES['electrolysis']['create_snippet'] = True
BRANCHES['electrolysis']['create_partial'] = True
BRANCHES['electrolysis']['create_partial_l10n'] = False
BRANCHES['electrolysis']['aus2_user'] = 'ffxbld'
BRANCHES['electrolysis']['aus2_ssh_key'] = 'ffxbld_dsa'
BRANCHES['electrolysis']['aus2_base_upload_dir'] = '/opt/aus2/incoming/2/Firefox/electrolysis'
BRANCHES['electrolysis']['aus2_base_upload_dir_l10n'] = '/opt/aus2/incoming/2/Firefox/electrolysis'

######## jaegermonkey
BRANCHES['jaegermonkey']['repo_path'] = 'projects/jaegermonkey'
BRANCHES['jaegermonkey']['start_hour'] = [4]
BRANCHES['jaegermonkey']['start_minute'] = [2]
BRANCHES['jaegermonkey']['enable_nightly'] = False
BRANCHES['jaegermonkey']['enable_mobile_nightly'] = False
BRANCHES['jaegermonkey']['create_snippet'] = False
# Disable XULRunner / SDK builds
BRANCHES['jaegermonkey']['enable_xulrunner'] = False
# Enable unit tests
BRANCHES['jaegermonkey']['platforms']['linux64']['enable_checktests'] = True
BRANCHES['jaegermonkey']['enable_mac_a11y'] = True
BRANCHES['jaegermonkey']['enable_shark'] = False
# L10n configuration
BRANCHES['jaegermonkey']['enable_l10n'] = False
BRANCHES['jaegermonkey']['l10nNightlyUpdate'] = False
BRANCHES['jaegermonkey']['l10nDatedDirs'] = False
# need this or the master.cfg will bail
BRANCHES['jaegermonkey']['aus2_base_upload_dir'] = 'fake'
BRANCHES['jaegermonkey']['platforms']['linux']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'jaegermonkey'
BRANCHES['jaegermonkey']['platforms']['linuxqt']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'linuxqt-jaegermonkey'
BRANCHES['jaegermonkey']['platforms']['linux64']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'linux64-jaegermonkey'
BRANCHES['jaegermonkey']['platforms']['win32']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'jaegermonkey'
BRANCHES['jaegermonkey']['platforms']['macosx64']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'macosx64-jaegermonkey'
BRANCHES['jaegermonkey']['mobile_platforms']['linux']['l10n_chunks'] = None
BRANCHES['jaegermonkey']['mobile_platforms']['win32']['l10n_chunks'] = None

######## tryserver
# Try-specific configs
BRANCHES['tryserver']['stage_username'] = 'trybld'
BRANCHES['tryserver']['stage_username_mobile'] = 'trybld'
BRANCHES['tryserver']['stage_ssh_key'] = 'trybld_dsa'
BRANCHES['tryserver']['stage_ssh_mobile_key'] = 'trybld_dsa'
BRANCHES['tryserver']['stage_base_path'] = '/home/ftp/pub/firefox/tryserver-builds'
BRANCHES['tryserver']['stage_base_path_mobile'] = '/home/ftp/pub/firefox/tryserver-builds'
BRANCHES['tryserver']['enable_merging'] = False
BRANCHES['tryserver']['enable_try'] = True
BRANCHES['tryserver']['package_dir'] ='%(who)s-%(got_revision)s'
# This is a path, relative to HGURL, where the repository is located
# HGURL  repo_path should be a valid repository
BRANCHES['tryserver']['repo_path'] = 'try'
BRANCHES['tryserver']['start_hour'] = [3]
BRANCHES['tryserver']['start_minute'] = [2]
# Disable Nightly builds
BRANCHES['tryserver']['enable_nightly'] = False
BRANCHES['tryserver']['enable_mobile_nightly'] = False
# Disable XULRunner / SDK builds
BRANCHES['tryserver']['enable_xulrunner'] = False
BRANCHES['tryserver']['enable_mac_a11y'] = True
# only do unittests locally until they are switched over to talos-r3
BRANCHES['tryserver']['enable_l10n'] = False
BRANCHES['tryserver']['enable_l10n_onchange'] = False
BRANCHES['tryserver']['l10nNightlyUpdate'] = False
BRANCHES['tryserver']['l10nDatedDirs'] = False
BRANCHES['tryserver']['enable_codecoverage'] = False
BRANCHES['tryserver']['enable_shark'] = False
BRANCHES['tryserver']['create_snippet'] = False
# need this or the master.cfg will bail
BRANCHES['tryserver']['aus2_base_upload_dir'] = 'fake'
BRANCHES['tryserver']['platforms']['linux']['slaves'] = TRY_SLAVES['linux']
BRANCHES['tryserver']['platforms']['linux64']['slaves'] = TRY_SLAVES['linux64']
BRANCHES['tryserver']['platforms']['linuxqt']['slaves'] = TRY_SLAVES['linux']
BRANCHES['tryserver']['platforms']['win32']['slaves'] = TRY_SLAVES['win32']
BRANCHES['tryserver']['platforms']['macosx64']['slaves'] = TRY_SLAVES['macosx64']
BRANCHES['tryserver']['platforms']['linux-debug']['slaves'] = TRY_SLAVES['linux']
BRANCHES['tryserver']['platforms']['linux64-debug']['slaves'] = TRY_SLAVES['linux64']
BRANCHES['tryserver']['platforms']['win32-debug']['slaves'] = TRY_SLAVES['win32']
BRANCHES['tryserver']['platforms']['macosx-debug']['slaves'] = TRY_SLAVES['macosx']
BRANCHES['tryserver']['platforms']['macosx64-debug']['slaves'] = TRY_SLAVES['macosx64']
BRANCHES['tryserver']['platforms']['linux']['upload_symbols'] = False
BRANCHES['tryserver']['platforms']['linux64']['upload_symbols'] = False
BRANCHES['tryserver']['platforms']['linuxqt']['upload_symbols'] = False
BRANCHES['tryserver']['platforms']['macosx64']['upload_symbols'] = False
BRANCHES['tryserver']['platforms']['win32']['upload_symbols'] = True
BRANCHES['tryserver']['platforms']['win32']['env']['SYMBOL_SERVER_USER'] = 'trybld'
BRANCHES['tryserver']['platforms']['win32']['env']['SYMBOL_SERVER_PATH'] = '/symbols/windows'
BRANCHES['tryserver']['platforms']['win32']['env']['SYMBOL_SERVER_SSH_KEY'] = '/c/Documents and Settings/cltbld/.ssh/trybld_dsa'
BRANCHES['tryserver']['mobile_platforms']['android-r7']['mozconfig'] = 'mobile-tryserver/android'
BRANCHES['tryserver']['mobile_platforms']['maemo5-gtk']['mozconfig'] = 'mobile-tryserver/maemo5-gtk/'
BRANCHES['tryserver']['mobile_platforms']['maemo5-qt']['mozconfig'] = 'mobile-tryserver/maemo5-qt'
BRANCHES['tryserver']['mobile_platforms']['android-r7']['slaves'] = TRY_SLAVES['linux']
BRANCHES['tryserver']['mobile_platforms']['maemo5-gtk']['slaves'] = TRY_SLAVES['linux']
BRANCHES['tryserver']['mobile_platforms']['maemo5-qt']['slaves'] = TRY_SLAVES['linux']
BRANCHES['tryserver']['mobile_platforms']['android-r7']['upload_symbols'] = False
BRANCHES['tryserver']['mobile_platforms']['maemo5-gtk']['upload_symbols'] = False
BRANCHES['tryserver']['mobile_platforms']['maemo5-qt']['upload_symbols'] = False

######## generic branch configs
for branch in PROJECT_BRANCHES.keys():
    # we need to check for an overriden repo path
    if 'repo_path' not in BRANCHES[branch].keys():
        BRANCHES[branch]['repo_path'] = 'projects/' + branch
    BRANCHES[branch]['start_hour'] = [4]
    BRANCHES[branch]['start_minute'] = [2]
    BRANCHES[branch]['enable_nightly'] = False
    BRANCHES[branch]['enable_mobile_nightly'] = False
    BRANCHES[branch]['create_snippet'] = False
    # Disable XULRunner / SDK builds
    BRANCHES[branch]['enable_xulrunner'] = False
    # Enable unit tests
    BRANCHES[branch]['platforms']['linux64']['enable_checktests'] = True
    BRANCHES[branch]['enable_mac_a11y'] = True
    BRANCHES[branch]['enable_shark'] = False
    # L10n configuration
    BRANCHES[branch]['enable_l10n'] = False
    BRANCHES[branch]['l10nNightlyUpdate'] = False
    BRANCHES[branch]['l10nDatedDirs'] = False
    # need this or the master.cfg will bail
    BRANCHES[branch]['aus2_base_upload_dir'] = 'fake'
    BRANCHES[branch]['platforms']['linux']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = branch
    BRANCHES[branch]['platforms']['linuxqt']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'linuxqt-' + branch
    BRANCHES[branch]['platforms']['linux64']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'linux64-' + branch
    BRANCHES[branch]['platforms']['win32']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = branch
    BRANCHES[branch]['platforms']['macosx64']['env']['MOZ_SYMBOLS_EXTRA_BUILDID'] = 'macosx64-' + branch
    BRANCHES[branch]['mobile_platforms']['linux']['l10n_chunks'] = None
    BRANCHES[branch]['mobile_platforms']['win32']['l10n_chunks'] = None
    # point to the generic project branch mozconfigs
    for platform in BRANCHES[branch]['platforms']:
        if platform.endswith('debug'):
            BRANCHES[branch]['platforms'][platform]['mozconfig'] = platform.split('-')[0] + '/generic/debug'
        elif platform.endswith('qt'):
            BRANCHES[branch]['platforms'][platform]['mozconfig'] = 'linux/generic/qt'
        else:
            BRANCHES[branch]['platforms'][platform]['mozconfig'] = platform + '/generic/nightly'

# Bug 578880, remove the following block after gcc-4.5 switch
for branch in ('birch', 'cedar', 'electrolysis', 'jaegermonkey', 'maple',
               'mozilla-2.0', 'mozilla-central', 'places', 'shadow-central',
               'tracemonkey', 'tryserver', 'build-system', 'services-central'):
    BRANCHES[branch]['platforms']['linux']['env']['LD_LIBRARY_PATH'] = '/tools/gcc-4.3.3/installed/lib'
    BRANCHES[branch]['platforms']['linuxqt']['env']['LD_LIBRARY_PATH'] = '/tools/gcc-4.3.3/installed/lib'
    BRANCHES[branch]['platforms']['linux64']['env']['LD_LIBRARY_PATH'] = '/tools/gcc-4.3.3/installed/lib64'
    BRANCHES[branch]['platforms']['linux-debug']['env']['LD_LIBRARY_PATH'] ='/tools/gcc-4.3.3/installed/lib:%s/dist/bin' % OBJDIR
    BRANCHES[branch]['platforms']['linux64-debug']['env']['LD_LIBRARY_PATH'] ='/tools/gcc-4.3.3/installed/lib64:%s/dist/bin' % OBJDIR
    BRANCHES[branch]['platforms']['linux']['unittest-env'] = {
        'LD_LIBRARY_PATH': '/tools/gcc-4.3.3/installed/lib',
    }
    BRANCHES[branch]['platforms']['linuxqt']['unittest-env'] = {
        'LD_LIBRARY_PATH': '/tools/gcc-4.3.3/installed/lib',
    }
    BRANCHES[branch]['platforms']['linux64']['unittest-env'] = {
        'LD_LIBRARY_PATH': '/tools/gcc-4.3.3/installed/lib64',
    }
    BRANCHES[branch]['platforms']['linux-debug']['unittest-env'] = {
        'LD_LIBRARY_PATH': '/tools/gcc-4.3.3/installed/lib',
    }
    BRANCHES[branch]['platforms']['linux64-debug']['unittest-env'] = {
        'LD_LIBRARY_PATH': '/tools/gcc-4.3.3/installed/lib64',
    }

if __name__ == "__main__":
    import sys, pprint
    args = sys.argv[1:]

    if len(args) > 0:
        branches = args
    else:
        branches = BRANCHES.keys()

    for branch in branches:
        print branch
        pprint.pprint(BRANCHES[branch])

    pprint.pprint(PROJECTS)
