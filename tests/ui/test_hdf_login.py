import re
from playwright.sync_api import Page, expect


def test_login(page: Page) -> None:
    page.goto("http://192.168.110.52:3006/manager/#/user/login")
    page.get_by_role("textbox", name="请输入用户名").click()
    page.get_by_role("textbox", name="请输入用户名").fill("admin")
    page.get_by_role("textbox", name="请输入密码").click()
    page.get_by_role("textbox", name="请输入密码").fill("admin")
    page.get_by_role("button", name="登 录").click()
    expect(page.locator("div").filter(has_text="登录成功").nth(4)).to_be_visible()


def test_login_wrong_password(page: Page) -> None:
    page.goto("http://192.168.110.52:3006/manager/#/user/login")
    page.get_by_role("textbox", name="请输入用户名").click()
    page.get_by_role("textbox", name="请输入用户名").fill("admin")
    page.get_by_role("textbox", name="请输入密码").click()
    page.get_by_role("textbox", name="请输入密码").fill("admin123")
    page.get_by_role("button", name="登 录").click()
    expect(page.locator("div").filter(has_text="密码错误").nth(4)).to_be_visible()

    
def test_mes_wllr(page: Page) -> None:
    # 使用录制的方式生成脚本的时候，一定要注意很多情况下我们需要自行进行修改，让脚本可以满足我们的需求
    page.goto("http://192.168.110.52:81/")
    page.goto("http://192.168.110.52:81/home")
    page.get_by_role("link", name="Login").click()
    page.get_by_role("button", name="立即登录").click()
    page.locator("div").filter(has_text=re.compile(r"^资产管理$")).click()
    page.get_by_role("menuitem", name="物料管理").click()
    page.get_by_role("button", name="添加").click()
    page.get_by_role("textbox", name="* 物料名称").click()
    page.get_by_role("textbox", name="* 物料名称").fill("8888")
    page.locator("div").filter(has_text=re.compile(r"^自产品$")).nth(3).click()
    page.get_by_role("option", name="自产品").click()
    page.locator("div").filter(has_text=re.compile(r"^消耗品$")).nth(3).click()
    page.locator("#el-id-7147-28").get_by_text("消耗品").click()
    page.get_by_role("textbox", name="规格型号").click()
    page.get_by_role("textbox", name="* 计量单位").click()
    page.get_by_role("button", name="选择").click()
    page.get_by_text("箱UT0002 选择 1台UT0001 选择").click()
    page.get_by_role("spinbutton", name="* 采购单价").click()
    page.get_by_role("spinbutton", name="* 采购单价").fill("09")
    page.get_by_role("spinbutton", name="* 销售单价").click()
    page.get_by_role("spinbutton", name="* 销售单价").fill("90")
    page.get_by_role("button", name="确定").click()