import os
from textual.app import ComposeResult
from textual.containers import Horizontal
from textual.widget import Widget
from textual.widgets import Static

from termtyper.ui.widgets.label import Banner, NavItem


def get_username() -> str:
    try:
        username = os.getlogin()
    except OSError:
        uid = os.getuid()
        import pwd

        username = pwd.getpwuid(uid).pw_name

    return username


class Header(Widget):
    """
    Header which forms the top banner of the app
    """

    DEFAULT_CSS = """
    Header {
        layout: grid;
        grid-size: 3 1;
        grid-rows: 5;
        grid-columns: 1fr 8fr 1fr;
    }
    """

    def compose(self) -> ComposeResult:
        yield Static()

        with Horizontal():
            home = NavItem("󰌌 home", "typing")
            home.add_class("active")

            yield Banner("smassh")
            yield home
            yield NavItem(" about", "about")
            yield NavItem(" settings", "settings")
            yield NavItem("󰋗 help", "help")

        # yield NavItem("  " + get_username())
