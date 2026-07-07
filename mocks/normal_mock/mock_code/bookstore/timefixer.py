from datetime import datetime


class TimeFixer:
    def now(self) -> str:
        return datetime.now().strftime("%d.%m.%Y %H:%M")
