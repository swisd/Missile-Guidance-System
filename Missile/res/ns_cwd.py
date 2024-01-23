"""CWD File Handler"""
import os


def current_relative(internal):
    """Current working directory relative to the location of implementation"""
    cwd = str(os.getcwd())
    relative_cwd = cwd + internal
    return relative_cwd
