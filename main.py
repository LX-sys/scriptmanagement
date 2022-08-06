
'''

    入口
'''
import sys
from core.utility import QApplication
from core.open_load import OpenLoad


if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = OpenLoad()
    win.show()

    sys.exit(app.exec_())