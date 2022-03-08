import pytest, os

if __name__ == '__main__':
    # pytest.main(['-vs', '--count=2', '--alluredir', '../outputs/reports/tmp', '--clean-alluredir'])
    pytest.main(['-vs','--alluredir', '../outputs/reports/tmp', '--clean-alluredir'])
    os.system('allure serve ../outputs/reports/tmp')
    os.system('allure generate ../outputs/reports/tmp')