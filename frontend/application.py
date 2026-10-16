import gi

from gi.repository import GLib, Gtk

from .main_window import MainWindow
class Application(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="bluedev.SGDB_FETCHER")
        GLib.set_application_name("SGDB FETCHER")

    def do_activate(self) -> None:
        main_window = MainWindow(application=self)
        main_window.present()
