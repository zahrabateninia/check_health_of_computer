#!/usr/bin/env python3

import os

def check_reboot():
    """Returns True if the computer needs a pending reboot."""
    return os.path.exists("/run/reboot-required")
def main():
    pass
main()