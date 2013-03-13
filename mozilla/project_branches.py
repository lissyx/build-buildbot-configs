PROJECT_BRANCHES = {
    ### PLEASE ADD NEW BRANCHES ALPHABETICALLY (twigs at the bottom, also alphabetically)
    'build-system': {
        'pgo_strategy': 'periodic',
        'platforms': {
            'win32': {
                'pgo_platform': 'win64',
            },
        },
    },
    'devtools': {
        'enable_nightly': True,
        'enabled_products': ['firefox'],
        'platforms': {
            'macosx64': {
                'slave_platforms': ['snowleopard', 'lion', 'mountainlion'],
            },
        },
        'mobile_platforms': {
            'android': {
                'enable_opt_unittests': False,
                'enable_debug_unittests': False,
                'tegra_android': {},
            },
            'android-armv6': {
                'enable_opt_unittests': False,
                'enable_debug_unittests': False,
                'tegra_android': {},
            },
        },
    },
    # DISABLED because of builder limit problems - bug 721854
    #'electrolysis': {
    #    'mozconfig_dir': 'electrolysis',
    #    'enable_talos': True,
    #},
    'fx-team': {
        'repo_path': 'integration/fx-team',
        'mozconfig_dir': 'mozilla-central',
        'enable_nightly': True,
        'pgo_strategy': 'periodic',
    },
    'graphics': {
        'enable_talos': False,
    },
    'ionmonkey': {
        'mozconfig_dir': 'mozilla-central',
        'enable_nightly': True,
        'create_snippet': True,
        'create_partial': True,
        'pgo_strategy': 'periodic',
    },
    'jaegermonkey': {
        'mozconfig_dir': 'jaegermonkey',
        'enable_nightly': True,
        'create_snippet': True,
        'create_partial': True,
    },
    'mozilla-inbound': {
        'repo_path': 'integration/mozilla-inbound',
        'enable_perproduct_builds': True,
        'mozconfig_dir': 'mozilla-central',
        'enable_nightly': False,
        'enable_weekly_bundle': True,
        'pgo_strategy': 'periodic',
        'periodic_pgo_interval': 3,
        'talos_suites': {
            'xperf': 1,
        },
        'platforms': {
            'linux64': {
                'nightly_signing_servers': 'nightly-signing',
            },
            'linux': {
                'nightly_signing_servers': 'nightly-signing',
            },
            'macosx64-debug': {
                'enable_leaktests': True,
                'nightly_signing_servers': 'mac-nightly-signing',
            },
            'macosx64': {
                'nightly_signing_servers': 'mac-nightly-signing',
            },
            'win32': {
                'nightly_signing_servers': 'nightly-signing',
            },
        },
    },
    # DISABLED because of builder limit problems - bug 721854
#    'places': {
#        'platforms': {
#            'linux64': {
#                'build_space': 6,
#            },
#            'linux': {
#                'build_space': 6,
#            },
#        },
#    },
    'profiling': {
        'pgo_strategy': 'periodic',
        'platforms': {
            'macosx64-debug': {
                'dont_build': True,
                'enable_debug_unittests': False,
                'nightly_signing_servers': 'mac-nightly-signing',
            },
            'macosx64': {
                'nightly_signing_servers': 'mac-nightly-signing',
            },
            'linux': {
                'nightly_signing_servers': 'nightly-signing',
            },
            'linux64': {
                'nightly_signing_servers': 'nightly-signing',
            },
            'linux-debug': {
                'dont_build': True,
                'enable_debug_unittests': False,
            },
            'linux64-debug': {
                'dont_build': True,
                'enable_debug_unittests': False,
            },
            'win32-debug': {
                'dont_build': True,
                'enable_debug_unittests': False,
            },
            'win32': {
                'nightly_signing_servers': 'nightly-signing',
            },
            'win64': {
                'nightly_signing_servers': 'nightly-signing',
            },
        },
        'mobile_platforms': {
            'android-debug': {
                'dont_build': True,
                'enable_debug_unittests': False,
            },
        },
    },
    'services-central': {
        'repo_path': 'services/services-central',
        'enable_weekly_bundle': True,
        'pgo_strategy': 'periodic',
    },
    'ux': {
        'branch_name': 'UX',
        'mobile_branch_name': 'UX',
        'build_branch': 'UX',
        'tinderbox_tree': 'UX',
        'mobile_tinderbox_tree': 'UX',
        'packaged_unittest_tinderbox_tree': 'UX',
        'enabled_products': ['firefox'],
        'mozconfig_dir': 'ux',
        'enable_nightly': True,
        'create_snippet': True,
        'create_partial': True,
        'enable_unittests': False,
        'enable_talos': False,
        'platforms': {
            'macosx64-debug': {
                'dont_build': True,
                'enable_debug_unittests': False,
                'nightly_signing_servers': 'mac-nightly-signing',
            },
            'macosx64': {
                'nightly_signing_servers': 'mac-nightly-signing',
            },
            'linux': {
                'nightly_signing_servers': 'nightly-signing',
            },
            'linux64': {
                'nightly_signing_servers': 'nightly-signing',
            },
            'linux-debug': {
                'dont_build': True,
                'enable_debug_unittests': False,
            },
            'linux64-debug': {
                'dont_build': True,
                'enable_debug_unittests': False,
            },
            'win32-debug': {
                'dont_build': True,
                'enable_debug_unittests': False,
            },
            'win64': {
                'dont_build': True,
            },
        },
    },
    #####  TWIGS aka RENTABLE BRANCHES
    # customizations while booked for bug 687570 - WebRTC project
    'alder': {
        'platforms': {},
        'mobile_platforms': {
            'android': {
                'enable_opt_unittests': False,
                'enable_debug_unittests': False,
                'enable_talos': False,
                'tegra_android': {},
            },
            'android-armv6': {
                'enable_opt_unittests': False,
                'enable_debug_unittests': False,
                'enable_talos': False,
                'tegra_android': {},
            },
        },
    },
    'ash': {
        'mozharness_repo_path': 'users/asasaki_mozilla.com/ash-mozharness',
        'mozharness_repo': 'http://hg.mozilla.org/users/asasaki_mozilla.com/ash-mozharness',
        'mozharness_tag': 'default',
        'mozharness_talos': True,
        'lock_platforms': True,
        'platforms': {
            'linux': {},
            'linux64': {},
            'win32': {},
            'win64': {},
            'macosx64': {},
            'linux-debug': {},
            'linux64-debug': {},
            'macosx64-debug': {},
            'win32-debug': {},
        },
        'mobile_platforms': {
            'android': {
                'slave_platforms': ['panda_android'],
            },
        },
    },
    'birch': {
        'enable_talos': False,
        'enabled_products': ['firefox'],
    },
    'cedar': {
        'mozharness_talos': True,
        'mozharness_tag': 'default',
        'lock_platforms': True,
        'platforms': {
            'linux': {},
            'linux64': {},
            'win32': {},
            'win64': {},
            'macosx64': {},
            'linux-debug': {},
            'linux64-debug': {},
            'macosx64-debug': {},
            'win32-debug': {},
        },
        'mobile_platforms': {
            'android': {
                'slave_platforms': ['panda_android'],
            },
        },
    },
    # Customizations for b2g 1.1 work (bug 822783 & bug 819368)
    'date': {
        'lock_platforms': True,
        'platforms': {
            'linux': {},
            'linux64': {},
            'win32': {},
            'macosx64': {},
            'linux-debug': {},
            'linux64-debug': {},
            'macosx64-debug': {},
            'win32-debug': {},
        },
        'mobile_platforms': {
            'android-noion': {},
        },
    },
    # customizations for windows update service changes (bug 481815)
    'elm': {
        'enable_nightly': True,
        'enable_weekly_bundle': True,
        'create_snippet': True,
        'create_partial': True,
        'enable_talos': False,
        'lock_platforms': True,
        'platforms': {
            'linux': {},
            'linux-debug': {},
            'linux64': {},
            'linux64-debug': {},
            'macosx64-debug': {},
            'macosx64': {},
            'win32': {
                'nightly_signing_servers': 'nightly-signing',
            },
            'win32-debug': {},
        },
        'mobile_platforms': {
            'android': {},
            'android-debug': {},
            'android-armv6': {},
            'android-x86': {},
        },
    },
    'fig': {},
    'gum': {},
    'holly': {},
    # Bug 848025 - disable android builds for jamun
    'jamun': {
        'lock_platforms': True,
        'platforms': {
            'linux': {},
            'linux-debug': {},
            'linux64': {},
            'linux64-debug': {},
            'macosx64-debug': {},
            'macosx64': {},
            'win32': {},
            'win32-debug': {},
        },
        'mobile_platforms': {},
    },
    'larch': {},
    'maple': {},
    # customizations for integration work for bugs 481815 and 307181
    'oak': {
        'enable_nightly': True,
        'create_snippet': True,
        'create_partial': True,
        'enable_talos': False,
        'platforms': {
            'linux': {
                'nightly_signing_servers': 'nightly-signing',
            },
            'linux64': {
                'nightly_signing_servers': 'nightly-signing',
            },
            'win32': {
                'nightly_signing_servers': 'nightly-signing',
            },
        },
    },
    'pine': {},
    # gaia-master is b2g only; no desktop platforms are needed
    'gaia-master': {
        'poll_repo': 'integration/gaia-central',
        'lock_platforms': True,
        'platforms': {}
    }
}

# All is the default
ACTIVE_PROJECT_BRANCHES = PROJECT_BRANCHES.keys()

# Load up project branches' local values
for branch in PROJECT_BRANCHES.keys():
    PROJECT_BRANCHES[branch]['tinderbox_tree'] = PROJECT_BRANCHES[branch].get('tinderbox_tree', branch.title())
    PROJECT_BRANCHES[branch]['mobile_tinderbox_tree'] = PROJECT_BRANCHES[branch].get('mobile_tinderbox_tree', branch.title())
    PROJECT_BRANCHES[branch]['packaged_unittest_tinderbox_tree'] = PROJECT_BRANCHES[branch].get('packaged_unittest_tinderbox_tree', branch.title())
