import gi

from backend.image_manager import get_image
from backend.sqlite import get_games
gi.require_version("Gtk", "4.0")

from gi.repository import Gtk

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, **kargs):
        super().__init__(**kargs, title="SGDB FETCHER")
        #MainBox Created
        main_box:Gtk.Box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.set_child(main_box)
        #ToolBox Created
        tool_box:Gtk.Box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL,halign=Gtk.Align.END)
        main_box.append(tool_box)
        #ToolBox Buttons
        option_button:Gtk.Button = Gtk.Button(label="Options")
        tool_box.append(option_button)
        #Separator
        separator:Gtk.Separator = Gtk.Separator(orientation=Gtk.Orientation.HORIZONTAL)
        main_box.append(separator)
        #Scrolled Window and GameBox
        scrolled = Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        main_box.append(scrolled)
        self.game_box:Gtk.FlowBox = Gtk.FlowBox()
        scrolled.set_child(self.game_box)
        self.update_game_box()
    def update_game_box(self):
        games:list = get_games()
        for game in games:
            game_widget:Game = Game(game)
            self.game_box.append(game_widget)
class Game(Gtk.Box):
    def __init__(self,data,**kargs):
        super().__init__(**kargs,orientation=Gtk.Orientation.VERTICAL)
        self.set_vexpand(True)
        game_image:Gtk.Picture = get_image(data[2],0)
        self.append(game_image)
