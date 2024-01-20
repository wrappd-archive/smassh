from textual.app import ComposeResult
from textual.containers import Container
from textual.widgets import Static
from termtyper.src.stats_tracker import StatsTracker
from termtyper.ui.widgets import BaseWindow
from termtyper.ui.widgets.result import ValueContainer, Value, ResultStrip


class AutoVertical(Static):
    DEFAULT_CSS = """
    AutoVertical {
        margin: 1;
        height: auto;
        width: auto;
        background: red;
    }
    """


class AutoHorizontal(Static):
    DEFAULT_CSS = """
    AutoVertical {
        layout: horizontal;
        margin: 1;
        height: auto;
        width: auto;
    }
    """


class ResultScreen(BaseWindow):
    """
    This screen will show the result of the typing test.
    E.g. Typing Chart, Accuracy, WPM etc.
    """

    DEFAULT_CSS = """
    ResultScreen {
        layout: grid;
        grid-size: 1 4;
        grid-rows: 1fr auto 1 1fr;
        align: center middle;
    }
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.wpm = Value()
        self.accuracy = Value()

    def compose(self) -> ComposeResult:
        yield Container()
        yield ValueContainer()
        yield ResultStrip()
        yield Container()

    def set_results(self, stats: StatsTracker):
        self.stats = stats
        self.query_one(ValueContainer).update_stats(stats)
