"""合同管理 - 添加合同 测试用例.

目标系统: SPMS (http://192.168.110.52:81)
流程: 登录 -> 进入合同管理 -> 点击添加 -> 填写合同名称 -> 确定 -> 校验列表出现新合同.
"""

from datetime import datetime

from playwright.sync_api import Page, expect

CONTRACT_LIST_URL = "http://192.168.110.52:81/console/asset/contract/list"


def _login_and_open_contract_list(page: Page) -> None:
    """确保已登录并停留在合同管理列表页."""
    # SPA 未认证时内联渲染登录表单（URL 可能仍是目标地址或 /login），
    # 故等待应用渲染，再按可见按钮判断是否需要登录
    page.goto(CONTRACT_LIST_URL, wait_until="domcontentloaded")
    page.wait_for_selector(
        "button:has-text('立即登录'), button:has-text('添加')", timeout=15000
    )
    login_btn = page.get_by_role("button", name="立即登录")
    if login_btn.is_visible():
        login_btn.click()
        login_btn.wait_for(state="hidden", timeout=15000)
        page.goto(CONTRACT_LIST_URL, wait_until="domcontentloaded")
        page.wait_for_selector("button:has-text('添加')", timeout=15000)


def test_contract_add(page: Page) -> None:
    """添加一条合同，校验列表出现该合同."""
    _login_and_open_contract_list(page)

    # 点击列表页的"添加"按钮，打开新增表单
    page.get_by_role("button", name="添加", exact=True).click()

    # 合同名称（唯一，避免重复）
    name = f"自动化测试合同-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    page.get_by_placeholder("请输入合同名称...").fill(name)

    # 其余字段使用表单默认值：
    #   合同类型 = 其他合同；开始时间 = 今天；终止时间 = 一年后；合同编码自动生成
    page.get_by_role("button", name="确定").click()

    # 断言提交成功提示
    expect(page.get_by_text("添加成功")).to_be_visible()

    # 断言新合同出现在列表中
    row = page.locator(".el-table__row", has_text=name)
    expect(row).to_be_visible()
