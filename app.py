import gi
gi.require_version("Gtk", "4.0")
import sys

from frontend.application import Application


if __name__ == '__main__':
    app = Application()
    app.run(sys.argv)
