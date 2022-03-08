import os

project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   #获取目录路径
common_path = os.path.join(project_path, 'common\\')
config_path = os.path.join(project_path, 'config\\')
testDatas_path = os.path.join(project_path, 'testDatas\\')
outputs_path = os.path.join(project_path, 'outputs\\')
logs_path = os.path.join(outputs_path, 'logs\\')
jietus_path = os.path.join(outputs_path, 'jietus\\')
reports_path = os.path.join(outputs_path, 'reports\\')
report_path = os.path.join(project_path,'report\\tmp')


if __name__ == '__main__':
    print(report_path)