from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWebEngineWidgets import QWebEnginePage


class WebEnginePage(QWebEnginePage):
    def __init__(self, parent):
        super(WebEnginePage, self).__init__(parent)

    def acceptNavigationRequest(self, url, typ, ismainframe):
        if typ == QWebEnginePage.NavigationTypeLinkClicked:
            QDesktopServices.openUrl(url)
            return False
        return super(WebEnginePage, self).acceptNavigationRequest(url, typ, ismainframe)

