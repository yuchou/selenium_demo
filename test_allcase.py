import unittest
from comm import html


if __name__ == '__main__':
    discover = unittest.defaultTestLoader.discover('tests', pattern='test_*.py')
    runner= html.HTMLTestRunner(output='html', report_title=u'测试')
    runner.run(discover)