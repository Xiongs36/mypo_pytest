import  unittest

from HTMLTestRunner.HTMLTestRunner import HTMLTestRunner

suite=unittest.defaultTestLoader.discover('./case/',pattern='case_*.py')
with open('./report/rep.html', mode='w') as file:
    runner =HTMLTestRunner(stream=file)
    runner.run(suite)
