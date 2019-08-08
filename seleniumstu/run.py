from utx import *
import sys
sys.path.append('D:\\')


"""运行测试用例主入口"""
setting.run_case = {Tag.ALL}  # 运行全部测试用例
# setting.run_case = {Tag.SMOKE}  # 只运行SMOKE标记的测试用例
# setting.run_case = {Tag.SMOKE, Tag.V1_0_0}   # 只运行SMOKE和V1_0_0标记的测试用例

setting.check_case_doc = True
setting.full_case_name = True
setting.max_case_name_len = 80  # 测试报告内，显示用例名字的最大程度
setting.show_error_traceback = True  # 执行用例的时候，显示报错信息
setting.sort_case = True  # 是否按照编写顺序，对用例进行排序(注意：如果用例中存在depend依赖，这个一定要是True)
setting.create_report_by_style_1 = True  # 测试报告样式1
setting.show_print_in_console = True

log.set_level_to_debug()     # 设置log级别

runner = TestRunner(retry=1, save_last_try=True)  # retry:失败重试次数 save_last_try:是否保存最后一次重试结果

runner.add_case_dir(r"testcase")
runner.run_test(report_title='WEB_UI自动化测试报告')


